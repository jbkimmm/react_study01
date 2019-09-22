import json
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.forms import CourseTargetForm, CoursePercentForm, CourseBookForm, CourseWeekForm
from api.forms import CourseConditionForm, CourseStructForm, CourseClassForm
from .models import (
    Professor, CourseClass, CoursePercent, CourseBook, CourseWeek, CourseCondition, CourseStruct,
    CourseTarget)

def index(request):
    return render(request, 'index/index.html')


def api_getProName(request, pro_num):
    prof = get_object_or_404(Professor, professor_number=pro_num)
    return JsonResponse({'result': prof.professor_name})


def api_getCourse(request):
    year = request.GET.get('year')
    season = request.GET.get('season')
    pro_num = request.GET.get('pro_num')
    auth_type = request.GET.get('auth_type')

    professor = get_object_or_404(Professor, professor_number=pro_num)

    qs = professor.course_set.all()
    qs = qs.filter(
        course_year = year,
        season = season,
        cert_type = auth_type)

    return JsonResponse({
        'result': [course.as_dict() for course in qs],
    })


def api_getClass(request, course_id):
    qs = CourseClass.objects.filter(course__id=course_id)
    return JsonResponse({
        'result': [cls.as_dict() for cls in qs],
    })


def api_getProList(request, class_id):
    course_class = get_object_or_404(CourseClass, id=class_id)

    main_professor = course_class.course.professor
    sub_professor = course_class.professor

    professor_list = [
        main_professor.as_dict(),
        sub_professor.as_dict(),
    ]

    return JsonResponse({'result': professor_list})


def api_getTime(request, class_id):
    klass = get_object_or_404(CourseClass, id=class_id)

    qs = klass.coursesubject_set.all()

    result = [subject.as_dict() for subject in qs]
    content = klass.content

    return JsonResponse({
        'result': result,
        'content': content,
    })


def api_getCheck(request, class_id):
    course_class = get_object_or_404(CourseClass, id=class_id)

    qs = course_class.coursetarget_set.all()

    result = [
        subject.as_dict(cnt=cnt)
        for cnt, subject in enumerate(qs, 1)]

    return JsonResponse({'result': result})


def api_getWeek(request, class_id):
    course_class = get_object_or_404(CourseClass, id=class_id)
    result = course_class.courseweek.as_dict()
    return JsonResponse({'result': [result]})


def api_getTwoTab(request, class_id):
    course_class = get_object_or_404(CourseClass, id=class_id)
    qs = course_class.coursecore_set.all()
    result = [
        core.as_dict(cnt=cnt)
        for cnt, core in enumerate(qs, 1)]

    return JsonResponse({
        'pre_content': course_class.pre_content,
        'test_content': course_class.test_content,
        'left_list': course_class.coursepercent.as_dict(),
        'right_list': course_class.coursebook.as_dict(),
        'bottom_list': result,
    })


def api_getFourTab(request, class_id):
    course_class = get_object_or_404(CourseClass, id=class_id)

    design_content = course_class.design_content
    check_content = course_class.check_content
    report_content = course_class.report_content
    exe_content = course_class.exe_content

    qs = course_class.coursecondition_set.all()
    condition_list = [cond.as_dict() for cond in qs]

    qs = course_class.coursestruct_set.all()
    struct_list = [struct.as_dict() for struct in qs]

    return JsonResponse({
        'design_content': course_class.design_content,
        'check_content': course_class.check_content,
        'report_content': course_class.report_content,
        'exe_content': course_class.exe_content,
        'condition_list': condition_list,
        'struct_list': struct_list
    })


def boolToYN(n):
    if n == True:
        return 'Y'
    elif n == False:
        return 'N'


@csrf_exempt
def api_saveData(request):
    try:
        request.json = json.loads(request.body)
    except BaseException:
        return JsonResponse({"result": 800})  # json 로드 오류

    tabIdx = request.json['tabIdx']

    if tabIdx == 1:
        dump_truck = request.json['dump_truck']
        one_top = request.json['one_top']
        select_id = request.json['select_id']

        CourseClass.objects.filter(pk=select_id).update(
            content=one_top
        )

        # 교과목 목표별 교육방법 및 평가방법 수정
        for data in dump_truck:
            pk = data.pop('id')
            instance = get_object_or_404(CourseTarget, pk=pk)
            form = CourseTargetForm(data, instance=instance)
            print(form.is_valid())
            if form.is_valid():
                form.save()

    elif tabIdx == 2:
        select_id = request.json['select_id']

        tcc = CourseClass.objects.get(id=select_id)
        tcc.pre_content = request.json['two_top']
        tcc.test_content = request.json['two_bot']
        tcc.save()

        tcp = CoursePercent.objects.get(class_id=select_id)
        # t1부터 순차적으로 적용
        data = {}
        form = CoursePercentForm(data, instance=tcp)
        form.is_valid()  # FIXME: raise_for_valid()를 써보면 어떨까?
        form.save()

        tcb = CourseBook.objects.get(class_id=select_id)
        data = {}  # t10부터 순차적으로 적용
        form = CourseBookForm(data, instance=tcb)
        form.is_valid()  # FIXME:
        form.save()

    elif tabIdx == 3:
        select_id = request.json['select_id']
        wc_list = request.json['wc_list']
        wp_list = request.json['wp_list']

        print('select_id -> ', select_id)
        print('wc_list -> ', wc_list)
        print('wp_list -> ', wp_list)

        tcw = CourseWeek.objects.get(class_id=select_id)
        # wc_list[0] ... wc_list[15]를 week1_course에 매핑
        # wp_list[0] ... wp_list[15]를 week1_practice에 매핑
        data = {}
        form = CourseWeekForm(data, instance=tcw)
        form.is_valid()  # FIXME:
        form.save()

    elif tabIdx == 4:
        select_id = request.json['select_id']

        dump_truck1 = request.json['dump_truck1']
        dump_truck2 = request.json['dump_truck2']

        tcc2 = CourseClass.objects.get(id=select_id)
        data = {}  # FIXME: fff1 ~ fff4
        form = CourseClassForm(data, instance=tcc2)
        form.is_valid()  # FIXME
        form.save()

        for d in dump_truck1:
            print('d -> ', d)
            tcc = CourseCondition.objects.get(id=d['id'])
            data = {}  # c_code, c_method, c_content 순서대로 xx1, xx2, xx3
            form = CourseConditionForm(data, instance=tcc)
            form.is_valid()  # FIXME
            form.save()

            tcc.c_code = d['xx1']
            tcc.c_method = d['xx2']
            tcc.c_content = d['xx3']
            tcc.save()

        for d in dump_truck2:
            print('d -> ', d)
            tcs = CourseStruct.objects.get(id=d['id'])
            data = {}  # c_code, c_method, c_content 순서대로 xxx1, xxx2, xxx3
            form = CourseStructForm(data, instance=tcs)
            form.is_valid()  # FIXME
            form.save()

    return JsonResponse({'result': 200})
