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
        'final_exam': tcp.task,
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