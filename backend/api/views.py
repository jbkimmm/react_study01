from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from api.models import Professor, Course, CourseClass


def professor_list(request):
    qs = Professor.objects.all()
    query = request.GET.get('query', '')
    if query:
        qs = qs.filter(
            Q(number__icontains=query) |
            Q(name__icontains=query)
        )
    return qs


def course_list(request, professor_pk):
    # FIXME: year, season, cert_type을 QueryString으로 처리
    year = 2019
    season = 1
    cert_type = '공학교육인증'
    professor = get_object_or_404(Professor, pk=professor_pk)
    qs = Course.objects.all()
    qs = qs.filter(year=year, season=season, professor=professor,
                   cert_type=cert_type)
    return qs


def class_list(request, course_pk):
    qs = CourseClass.objects.filter(course__id=course_pk)
    return qs


def class_detail(request, pk):
    klass = get_object_or_404(CourseClass, pk=pk)
    subject_list = klass.coursesubject_set.all()
    target_list = klass.coursetarget_set.all()
    core_list = klass.coursecore_set.all()
    condition_list = klass.coursecondition_set.all()
    struct_list = klass.coursestruct_set.all()

    return klass.as_dict(
        professor_list=[
            klass.course.professor,
            klass.professor,
        ],
        percent=klass.coursepercent,
        book=klass.coursebook,
        subject_list=subject_list,  # .result
        target_list=target_list,   # .getCheck에서 .result 속성
        week=klass.courseweek,
        core_list=core_list,
        condition_list=condition_list,
        struct_list=struct_list,
    )

