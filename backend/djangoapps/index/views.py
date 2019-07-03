import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

from backend.djangoapps.common.views import *
from backend.models import *

def index(request):
    context = {}
    return render(request, 'index/index.html', context)


def api_getProName(request):
    pro_num = request.POST.get('pro_num')
    prof = get_object_or_404(Professor, professor_number=pro_num)
    return JsonResponse({'result': prof.professor_name})


def api_getCourse(request):
    year = request.POST.get('year')
    season = request.POST.get('season')
    pro_num = request.POST.get('pro_num')
    auth_type = request.POST.get('auth_type')

    professor = get_object_or_404(Professor, professor_number=pro_num)

    qs = professor.course_set.all()
    qs = qs.filter(
        course_year = year,
        season = season,
        cert_type = auth_type)

    return JsonResponse({
        'result': [course.as_dict() for course in qs],
    })


def api_getClass(request):
    course_id = request.POST.get('course_id')

    qs = CourseClass.objects.filter(course__id=course_id)
    return JsonResponse({
        'result': [cls.as_dict() for cls in qs],
    })


def api_getProList(request):
    course_class_id = request.POST.get('class_id')

    course_class = get_object_or_404(CourseClass, id=course_class_id)

    main_professor = course_class.course.professor
    sub_professor = course_class.professor

    professor_list = [
        main_professor.as_dict(),
        sub_professor.as_dict(),
    ]

    return JsonResponse({'result': professor_list})


def api_getTime(request):
    course_class_id = request.POST.get('class_id')
    course_class = get_object_or_404(CourseClass, id=course_class_id)

    qs = course_class.coursesubject_set.all()

    result = [subject.as_dict() for subject in qs]
    content = course_class.content

    return JsonResponse({'result': result, 'content': content})


def api_getCheck(request):
    course_class_id = request.POST.get('class_id')
    course_class = get_object_or_404(CourseClass, id=course_class_id)

    qs = course_class.coursetarget_set.all()

    result = [
        subject.as_dict(cnt=cnt)
        for cnt, subject in enumerate(qs, 1)]

    return JsonResponse({'result': result})


def api_getWeek(request):
    course_class_id = request.POST.get('class_id')
    course_class = get_object_or_404(CourseClass, id=course_class_id)
    result = course_class.courseweek.as_dict()
    return JsonResponse({'result': [result]})


def api_getTwoTab(request):
    course_class_id = request.POST.get('class_id')
    course_class = get_object_or_404(CourseClass, id=course_class_id)
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


def api_getFourTab(request):
    course_class_id = request.POST.get('class_id')
    course_class = get_object_or_404(CourseClass, id=course_class_id)

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

def api_saveData(request):

    try:
        rjson = json.loads(request.body)
    except BaseException:
        return JsonResponse({"result": 800})  # json 로드 오류

    tabIdx = rjson['tabIdx']

    if tabIdx == 1:
        dump_truck = rjson['dump_truck']
        one_top = rjson['one_top']
        select_id = rjson['select_id']

        print('-----------------------------')
        print('dump_truck -> ', dump_truck)
        print('one_top -> ', one_top)
        print('select_id -> ', select_id)
        print('tabIdx -> ', tabIdx)
        print('-----------------------------')

        tcc = CourseClass.objects.get(id=select_id)

        print('tcc.content before-> ', tcc.content)
        tcc.content = one_top
        print('tcc.content after-> ', tcc.content)
        tcc.save()

        for d in dump_truck:
            print('d -> ', d)
            tct = CourseTarget.objects.get(id=d['id'])
            tct.e_course = boolToYN(d['x1'])
            tct.e_discussion = boolToYN(d['x2'])
            tct.e_experiment = boolToYN(d['x3'])
            tct.e_online = boolToYN(d['x4'])
            tct.e_presentation = boolToYN(d['x5'])
            tct.e_art = boolToYN(d['x6'])
            tct.e_seminar = boolToYN(d['x7'])
            tct.e_study = boolToYN(d['x8'])
            tct.e_design = boolToYN(d['x9'])
            tct.e_other = boolToYN(d['x10'])
            tct.w_attendance = boolToYN(d['x11'])
            tct.w_middle_exam = boolToYN(d['x12'])
            tct.w_final_exam = boolToYN(d['x13'])
            tct.w_project = boolToYN(d['x14'])
            tct.w_quiz = boolToYN(d['x15'])
            tct.w_presentation = boolToYN(d['x16'])
            tct.w_report = boolToYN(d['x17'])
            tct.w_practical = boolToYN(d['x18'])
            tct.w_other = boolToYN(d['x19'])
            tct.save()
    elif tabIdx == 2:
        select_id = rjson['select_id']
        two_top = rjson['two_top']
        two_bot = rjson['two_bot']
        t1 = rjson['t1']
        t2 = rjson['t2']
        t3 = rjson['t3']
        t4 = rjson['t4']
        t5 = rjson['t5']
        t6 = rjson['t6']
        t7 = rjson['t7']
        t8 = rjson['t8']
        t9 = rjson['t9']
        t10 = rjson['t10']
        t11 = rjson['t11']
        t12 = rjson['t12']
        t13 = rjson['t13']
        t14 = rjson['t14']
        t15 = rjson['t15']
        t16 = rjson['t16']
        t17 = rjson['t17']

        result = 0
        for n in range(1, 10):
            result += int(rjson['t' + str(n)])

        if result != 100:
            return JsonResponse({'result': 400})

        print('t1 -> ', t1)
        print('t2 -> ', t2)
        print('t3 -> ', t3)
        print('t4 -> ', t4)
        print('t5 -> ', t5)
        print('t6 -> ', t6)
        print('t8 -> ', t8)
        print('t9 -> ', t9)
        print('t10 -> ', t10)
        print('t11 -> ', t11)
        print('t12 -> ', t12)
        print('t13 -> ', t13)
        print('t14 -> ', t14)
        print('t15 -> ', t15)
        print('t16 -> ', t16)
        print('t17 -> ', t17)

        tcc = CourseClass.objects.get(id=select_id)
        tcc.pre_content = two_top
        tcc.test_content = two_bot
        tcc.save()

        tcp = CoursePercent.objects.get(class_id=select_id)
        tcp.task = t1
        tcp.final_exam = t2
        tcp.other = t3
        tcp.presentation = t4
        tcp.report = t5
        tcp.practical = t6
        tcp.middle_exam = t7
        tcp.attendance = t8
        tcp.quiz = t9
        tcp.save()

        tcb = CourseBook.objects.get(class_id=select_id)
        tcb.consult_time = t10
        tcb.pre_knowledge = t11
        tcb.main_note = t12
        tcb.sub_note1 = t13
        tcb.sub_note2 = t14
        tcb.sub_note3 = t15
        tcb.ref_web = t16
        tcb.select_book = t17
        tcb.save()

    elif tabIdx == 3:
        select_id = rjson['select_id']
        wc_list = rjson['wc_list']
        wp_list = rjson['wp_list']

        print('select_id -> ', select_id)
        print('wc_list -> ', wc_list)
        print('wp_list -> ', wp_list)

        tcw = CourseWeek.objects.get(class_id=select_id)
        tcw.week1_course = wc_list[0]
        tcw.week2_course = wc_list[1]
        tcw.week3_course = wc_list[2]
        tcw.week4_course = wc_list[3]
        tcw.week5_course = wc_list[4]
        tcw.week6_course = wc_list[5]
        tcw.week7_course = wc_list[6]
        tcw.week8_course = wc_list[7]
        tcw.week9_course = wc_list[8]
        tcw.week10_course = wc_list[9]
        tcw.week11_course = wc_list[10]
        tcw.week12_course = wc_list[11]
        tcw.week13_course = wc_list[12]
        tcw.week14_course = wc_list[13]
        tcw.week15_course = wc_list[14]
        tcw.week16_course = wc_list[15]

        tcw.week1_practice = wp_list[0]
        tcw.week2_practice = wp_list[1]
        tcw.week3_practice = wp_list[2]
        tcw.week4_practice = wp_list[3]
        tcw.week5_practice = wp_list[4]
        tcw.week6_practice = wp_list[5]
        tcw.week7_practice = wp_list[6]
        tcw.week8_practice = wp_list[7]
        tcw.week9_practice = wp_list[8]
        tcw.week10_practice = wp_list[9]
        tcw.week11_practice = wp_list[10]
        tcw.week12_practice = wp_list[11]
        tcw.week13_practice = wp_list[12]
        tcw.week14_practice = wp_list[13]
        tcw.week15_practice = wp_list[14]
        tcw.week16_practice = wp_list[15]

        tcw.save()
    elif tabIdx == 4:
        select_id = rjson['select_id']
        fff1 = rjson['fff1']
        fff2 = rjson['fff2']
        fff3 = rjson['fff3']
        fff4 = rjson['fff4']
        dump_truck1 = rjson['dump_truck1']
        dump_truck2 = rjson['dump_truck2']

        for d in dump_truck1:
            print('d -> ', d)
            tcc = CourseCondition.objects.get(id=d['id'])
            tcc.c_code = d['xx1']
            tcc.c_method = d['xx2']
            tcc.c_content = d['xx3']
            tcc.save()

        for d in dump_truck2:
            print('d -> ', d)
            tcs = CourseStruct.objects.get(id=d['id'])
            tcs.s_code = d['xxx1']
            tcs.s_method = d['xxx2']
            tcs.s_content = d['xxx3']
            tcs.save()

        tcc2 = CourseClass.objects.get(id=select_id)
        tcc2.design_content = fff1
        tcc2.check_content = fff2
        tcc2.report_content = fff3
        tcc2.exe_content = fff4
        tcc2.save()

    return JsonResponse({'result': 200})
