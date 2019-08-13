import json
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
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

        for row in dump_truck:
            pk = row['id']
            field_names = (
                'e_course', 'e_discussion', 'e_experiment', 'e_online', 'e_presentation',
                'e_art', 'e_seminar', 'e_study', 'e_design', 'e_other', 'w_attendance',
                'w_middle_exam', 'w_final_exam', 'w_project', 'w_quiz', 'w_presentation',
                'w_report', 'w_practical', 'w_other',
            )

            course_target = get_object_or_404(CourseTarget, pk=pk)
            for i in range(1, 20):
                src_field_name = 'x{}'.format(i)
                dst_field_name = field_names[i-1]
                attr = 'Y' if row[src_field_name] else 'N'
                setattr(course_target, dst_field_name, attr)
            course_target.save()

    elif tabIdx == 2:
        select_id = request.json['select_id']
        two_top = request.json['two_top']
        two_bot = request.json['two_bot']
        t1 = request.json['t1']
        t2 = request.json['t2']
        t3 = request.json['t3']
        t4 = request.json['t4']
        t5 = request.json['t5']
        t6 = request.json['t6']
        t7 = request.json['t7']
        t8 = request.json['t8']
        t9 = request.json['t9']
        t10 = request.json['t10']
        t11 = request.json['t11']
        t12 = request.json['t12']
        t13 = request.json['t13']
        t14 = request.json['t14']
        t15 = request.json['t15']
        t16 = request.json['t16']
        t17 = request.json['t17']

        result = 0
        for n in range(1, 10):
            result += int(request.json['t' + str(n)])

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
        select_id = request.json['select_id']
        wc_list = request.json['wc_list']
        wp_list = request.json['wp_list']

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
        select_id = request.json['select_id']
        fff1 = request.json['fff1']
        fff2 = request.json['fff2']
        fff3 = request.json['fff3']
        fff4 = request.json['fff4']
        dump_truck1 = request.json['dump_truck1']
        dump_truck2 = request.json['dump_truck2']

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
