import json
from django.shortcuts import render
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
    tp = TblProfessor.objects.get(professor_number=pro_num)
    
    return JsonResponse({'result': tp.professor_name})


def api_getCourse(request):

    year = request.POST.get('year')
    season = request.POST.get('season')
    pro_num = request.POST.get('pro_num')
    auth_type = request.POST.get('auth_type')

    print('year -> ', year)
    print('season -> ', season)
    print('pro_num -> ', pro_num)
    print('auth_type -> ', auth_type)

    tp = TblProfessor.objects.get(
        professor_number = pro_num
    )

    tc = TblCourse.objects.filter(
        course_year = year,
        season = season,
        cert_type = auth_type,
        main_professor = tp.id
    )

    res = []
    for t in tc:
        tmp = {}
        tmp['id'] = t.id
        tmp['display_name'] = t.display_name
        res.append(tmp)

    return JsonResponse({'result': res})


def api_getClass(request):

    course_id = request.POST.get('course_id')

    tcc = TblCourseClass.objects.filter(
        course_id=course_id
    )
    
    res = []
    for t in tcc:
        tmp = {}
        tmp['id'] = t.id
        tmp['class_code'] = t.class_code
        tmp['cert_type'] = t.cert_type
        tmp['base_type'] = t.base_type
        tmp['auth_type'] = t.auth_type
        tmp['design_type'] = t.design_type
        tmp['design_point'] = t.design_point
        res.append(tmp)

    return JsonResponse({'result': res})


def api_getProList(request):

    class_id = request.POST.get('class_id')

    tcc = TblCourseClass.objects.get(
        id=class_id
    )
    tc = TblCourse.objects.get(
        id=tcc.course_id
    )

    main_professor = tc.main_professor
    sub_professor = tcc.sub_professor
    
    tpfm = TblProfessor.objects.get(
        id=main_professor
    )
    tpfs = TblProfessor.objects.get(
        id=sub_professor
    )

    res = [
        {
            'professor_type': tpfm.professor_type,
            'professor_number': tpfm.professor_number,
            'professor_name': tpfm.professor_name,
            'department_name': tpfm.department_name,
            'school_number': tpfm.school_number,
            'email': tpfm.email,
        },
        {   
            'professor_type': tpfs.professor_type,
            'professor_number': tpfs.professor_number,
            'professor_name': tpfs.professor_name,
            'department_name': tpfs.department_name,
            'school_number': tpfs.school_number,
            'email': tpfs.email,
        }
    ]

    return JsonResponse({'result': res})


def api_getTime(request):

    class_id = request.POST.get('class_id')

    tcs = TblCourseSubject.objects.filter(
        class_id = class_id
    )

    res = []
    for t in tcs:
        tmp = {}
        tmp['grade'] = t.grade
        tmp['subject_type'] = t.subject_type
        tmp['subject_code'] = t.subject_code
        tmp['subject_name'] = t.subject_name
        tmp['subject_day'] = t.subject_day
        tmp['full_time'] = t.start_time + ' ~ ' + t.end_time
        tmp['building'] = t.building
        tmp['class_name'] = t.class_name
        tmp['make_department'] = t.make_department
        tmp['subject_point'] = t.subject_point
        res.append(tmp)

    content = TblCourseClass.objects.get(
        id = class_id
    ).content

    return JsonResponse({'result': res, 'content': content})


def api_getCheck(request):

    class_id = request.POST.get('class_id')

    tct = TblCourseTarget.objects.filter(
        class_id = class_id
    )

    res = []
    cnt = 1
    for t in tct:
        tmp = {}
        tmp['cnt'] = str(cnt)
        tmp['id'] = t.id
        tmp['target_name'] = t.target_name
        tmp['core_point'] = t.core_point
        tmp['e_course'] = t.e_course
        tmp['e_discussion'] = t.e_discussion
        tmp['e_experiment'] = t.e_experiment
        tmp['e_online'] = t.e_online
        tmp['e_presentation'] = t.e_presentation
        tmp['e_art'] = t.e_art
        tmp['e_seminar'] = t.e_seminar
        tmp['e_study'] = t.e_study
        tmp['e_design'] = t.e_design
        tmp['e_other'] = t.e_other
        tmp['w_attendance'] = t.w_attendance
        tmp['w_middle_exam'] = t.w_middle_exam
        tmp['w_final_exam'] = t.w_final_exam
        tmp['w_project'] = t.w_project
        tmp['w_quiz'] = t.w_quiz
        tmp['w_presentation'] = t.w_presentation
        tmp['w_report'] = t.w_report
        tmp['w_practical'] = t.w_practical
        tmp['w_other'] = t.w_other
        res.append(tmp)
        cnt += 1
    
    return JsonResponse({'result': res})


def api_getWeek(request):

    class_id = request.POST.get('class_id')

    tcw = TblCourseWeek.objects.get(
        class_id = class_id
    )

    res = [
        {
            'week1_course': tcw.week1_course,
            'week2_course': tcw.week2_course,
            'week3_course': tcw.week3_course,
            'week4_course': tcw.week4_course,
            'week5_course': tcw.week5_course,
            'week6_course': tcw.week6_course,
            'week7_course': tcw.week7_course,
            'week8_course': tcw.week8_course,
            'week9_course': tcw.week9_course,
            'week10_course': tcw.week10_course,
            'week11_course': tcw.week11_course,
            'week12_course': tcw.week12_course,
            'week13_course': tcw.week13_course,
            'week14_course': tcw.week14_course,
            'week15_course': tcw.week15_course,
            'week16_course': tcw.week16_course,
            'week1_practice': tcw.week1_practice,
            'week2_practice': tcw.week2_practice,
            'week3_practice': tcw.week3_practice,
            'week4_practice': tcw.week4_practice,
            'week5_practice': tcw.week5_practice,
            'week6_practice': tcw.week6_practice,
            'week7_practice': tcw.week7_practice,
            'week8_practice': tcw.week8_practice,
            'week9_practice': tcw.week9_practice,
            'week10_practice': tcw.week10_practice,
            'week11_practice': tcw.week11_practice,
            'week12_practice': tcw.week12_practice,
            'week13_practice': tcw.week13_practice,
            'week14_practice': tcw.week14_practice,
            'week15_practice': tcw.week15_practice,
            'week16_practice': tcw.week16_practice
        }
    ]
    return JsonResponse({'result': res})


def api_getTwoTab(request):

    class_id = request.POST.get('class_id')

    tcc = TblCourseClass.objects.get(
        id = class_id
    )
    pre_content = tcc.pre_content
    test_content = tcc.test_content

    tcp = TblCoursePercent.objects.get(
        class_id = class_id
    )
    left_list = {
        'task': tcp.task,
        'final_exam': tcp.final_exam,
        'other': tcp.other,
        'presentation': tcp.presentation,
        'report': tcp.report,
        'practical': tcp.practical,
        'middle_exam': tcp.middle_exam,
        'attendance': tcp.attendance,
        'quiz': tcp.quiz
    }
    
    tcb = TblCourseBook.objects.get(
        class_id = class_id
    )
    right_list = {
        'consult_time': tcb.consult_time,
        'pre_knowledge': tcb.pre_knowledge,
        'main_note': tcb.main_note,
        'sub_note1': tcb.sub_note1,
        'sub_note2': tcb.sub_note2,
        'sub_note3': tcb.sub_note3,
        'ref_web': tcb.ref_web,
        'select_book': tcb.select_book
    }

    tcc = TblCourseCore.objects.filter(
        class_id = class_id
    )
    res = []
    cnt = 1
    for t in tcc:
        tmp = {}
        tmp['id'] = cnt
        tmp['content'] = t.content
        tmp['percnet'] = t.percnet
        res.append(tmp)
        cnt += 1
    
    return JsonResponse({
        'pre_content': pre_content,
        'test_content': test_content,
        'left_list': left_list,
        'right_list': right_list,
        'bottom_list': res,
    })


def api_getFourTab(request):

    class_id = request.POST.get('class_id')

    tcc = TblCourseClass.objects.get(
        id = class_id
    )
    design_content = tcc.design_content
    check_content = tcc.check_content
    report_content = tcc.report_content
    exe_content = tcc.exe_content

    tcc2 = TblCourseCondition.objects.filter(
        class_id = class_id
    )
    condition_list = []
    for x in tcc2:
        tmp = {}
        tmp['id'] = x.id
        tmp['c_code'] = x.c_code
        tmp['c_method'] = x.c_method
        tmp['c_content'] = x.c_content
        condition_list.append(tmp)

    tcs = TblCourseStruct.objects.filter(
        class_id = class_id
    )
    struct_list = []
    for x in tcs:
        tmp = {}
        tmp['id'] = x.id
        tmp['s_code'] = x.s_code
        tmp['s_method'] = x.s_method
        tmp['s_content'] = x.s_content
        struct_list.append(tmp)

    return JsonResponse({
        'design_content': design_content,
        'check_content': check_content,
        'report_content': report_content,
        'exe_content': exe_content,
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

        tcc = TblCourseClass.objects.get(id=select_id)

        print('tcc.content before-> ', tcc.content)
        tcc.content = one_top
        print('tcc.content after-> ', tcc.content)
        tcc.save()

        for d in dump_truck:
            print('d -> ', d)
            tct = TblCourseTarget.objects.get(id=d['id'])
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

        tcc = TblCourseClass.objects.get(id=select_id)
        tcc.pre_content = two_top
        tcc.test_content = two_bot
        tcc.save()

        tcp = TblCoursePercent.objects.get(class_id=select_id)
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

        tcb = TblCourseBook.objects.get(class_id=select_id)
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

        tcw = TblCourseWeek.objects.get(class_id=select_id)
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
            tcc = TblCourseCondition.objects.get(id=d['id'])
            tcc.c_code = d['xx1']
            tcc.c_method = d['xx2']
            tcc.c_content = d['xx3']
            tcc.save()

        for d in dump_truck2:
            print('d -> ', d)
            tcs = TblCourseStruct.objects.get(id=d['id'])
            tcs.s_code = d['xxx1']
            tcs.s_method = d['xxx2']
            tcs.s_content = d['xxx3']
            tcs.save()

        tcc2 = TblCourseClass.objects.get(id=select_id)
        tcc2.design_content = fff1
        tcc2.check_content = fff2
        tcc2.report_content = fff3
        tcc2.exe_content = fff4
        tcc2.save()

    return JsonResponse({'result': 200})