from django.db import models


class Course(models.Model):
    year = models.CharField(max_length=10, db_column='course_year')
    season = models.CharField(max_length=10)
    display_name = models.CharField(max_length=255)
    cert_type = models.CharField(max_length=10)
    professor = models.ForeignKey('Professor', db_column='main_professor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_course'

    def as_dict(self):
        return {
            'pk': self.pk,
            'key': self.pk,
            'display_name': self.display_name,
        }


class CourseBook(models.Model):
    course_class = models.OneToOneField('CourseClass', db_column='class_id', on_delete=models.CASCADE)
    consult_time = models.CharField(max_length=255, blank=True, null=True)
    pre_knowledge = models.CharField(max_length=255, blank=True, null=True)
    main_note = models.CharField(max_length=255, blank=True, null=True)
    sub_note1 = models.CharField(max_length=255, blank=True, null=True)
    sub_note2 = models.CharField(max_length=255, blank=True, null=True)
    sub_note3 = models.CharField(max_length=255, blank=True, null=True)
    ref_web = models.CharField(max_length=255, blank=True, null=True)
    select_book = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_course_book'

    def as_dict(self):
        return {
            'pk': self.pk,
            'key': self.pk,
            'consult_time': self.consult_time,
            'pre_knowledge': self.pre_knowledge,
            'main_note': self.main_note,
            'sub_note1': self.sub_note1,
            'sub_note2': self.sub_note2,
            'sub_note3': self.sub_note3,
            'ref_web': self.ref_web,
            'select_book': self.select_book
        }


class CourseClass(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_code = models.CharField(max_length=100)
    cert_type = models.CharField(max_length=100)
    base_type = models.CharField(max_length=100)
    auth_type = models.CharField(max_length=100)
    design_type = models.CharField(max_length=100)
    design_point = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    pre_content = models.CharField(max_length=100, blank=True, null=True)
    test_content = models.TextField(blank=True, null=True)
    design_content = models.TextField(blank=True, null=True)
    check_content = models.TextField(blank=True, null=True)
    report_content = models.TextField(blank=True, null=True)
    exe_content = models.TextField(blank=True, null=True)
    professor = models.ForeignKey('Professor', db_column='sub_professor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_course_class'

    def as_dict(self, **kwargs):
        return dict({
            'pk': self.pk,
            'key': self.pk,
            'class_code': self.class_code,
            'cert_type': self.cert_type,
            'base_type': self.base_type,
            'auth_type': self.auth_type,
            'design_type': self.design_type,
            'design_point': self.design_point,
            'content': self.content,
            'pre_content': self.pre_content,
            'test_content': self.test_content,
            'design_content': self.design_content,
            'check_content': self.check_content,
            'report_content': self.report_content,
            'exe_content': self.exe_content,
        }, **kwargs)


class CourseCondition(models.Model):
    course_class = models.ForeignKey('CourseClass', db_column='class_id', on_delete=models.CASCADE)
    c_code = models.CharField(max_length=255, blank=True, null=True)
    c_method = models.CharField(max_length=255, blank=True, null=True)
    c_content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_course_condition'

    def as_dict(self):
        return {
            'pk': self.pk,
            'key': self.pk,
            'c_code': self.c_code,
            'c_method': self.c_method,
            'c_content': self.c_content,
        }



class CourseCore(models.Model):
    course_class = models.ForeignKey('CourseClass', db_column='class_id', on_delete=models.CASCADE)
    content = models.CharField(max_length=255, blank=True, null=True)
    percent = models.CharField(max_length=100, blank=True, null=True, db_column='percnet')  # FIXME: 오타?

    class Meta:
        db_table = 'tbl_course_core'

    def as_dict(self, **kwargs):
        return dict({
            'pk': self.pk,
            'key': self.pk,
            'content': self.content,
            'percent': self.percent,
        }, **kwargs)


class CoursePercent(models.Model):
    course_class = models.OneToOneField('CourseClass', db_column='class_id', on_delete=models.CASCADE)
    task = models.IntegerField()
    final_exam = models.IntegerField()
    other = models.IntegerField()
    presentation = models.IntegerField()
    report = models.IntegerField()
    practical = models.IntegerField()
    middle_exam = models.IntegerField()
    attendance = models.IntegerField()
    quiz = models.IntegerField()

    class Meta:
        db_table = 'tbl_course_percent'

    def as_dict(self):
        return {
            'pk': self.pk,
            'key': self.pk,
            'task': self.task,
            'final_exam': self.final_exam,
            'other': self.other,
            'presentation': self.presentation,
            'report': self.report,
            'practical': self.practical,
            'middle_exam': self.middle_exam,
            'attendance': self.attendance,
            'quiz': self.quiz,
        }


class CourseStruct(models.Model):
    course_class = models.ForeignKey('CourseClass', db_column='class_id', on_delete=models.CASCADE)
    s_code = models.CharField(max_length=255, blank=True, null=True)
    s_method = models.CharField(max_length=255, blank=True, null=True)
    s_content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_course_struct'

    def as_dict(self):
        return {
            'pk': self.pk,
            'key': self.pk,
            's_code': self.s_code,
            's_method': self.s_method,
            's_content': self.s_content,
        }


class CourseSubject(models.Model):
    course_class = models.ForeignKey('CourseClass', db_column='class_id', on_delete=models.CASCADE)
    grade = models.IntegerField()
    subject_type = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=255)
    subject_day = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    make_department = models.CharField(max_length=100)
    subject_point = models.IntegerField()

    class Meta:
        db_table = 'tbl_course_subject'

    def as_dict(self):
        return {
            'pk': self.pk,
            'key': self.pk,
            'grade': self.grade,
            'subject_type': self.subject_type,
            'subject_code': self.subject_code,
            'subject_name': self.subject_name,
            'subject_day': self.subject_day,
            'full_time': self.start_time + ' ~ ' + self.end_time,
            'building': self.building,
            'class_name': self.class_name,
            'make_department': self.make_department,
            'subject_point': self.subject_point,
        }


class CourseTarget(models.Model):
    course_class = models.ForeignKey('CourseClass', db_column='class_id', on_delete=models.CASCADE)
    target_name = models.CharField(max_length=255)
    core_point = models.IntegerField()
    e_course = models.CharField(max_length=10, blank=True, null=True)
    e_discussion = models.CharField(max_length=10, blank=True, null=True)
    e_experiment = models.CharField(max_length=10, blank=True, null=True)
    e_online = models.CharField(max_length=10, blank=True, null=True)
    e_presentation = models.CharField(max_length=10, blank=True, null=True)
    e_art = models.CharField(max_length=10, blank=True, null=True)
    e_seminar = models.CharField(max_length=10, blank=True, null=True)
    e_study = models.CharField(max_length=10, blank=True, null=True)
    e_design = models.CharField(max_length=10, blank=True, null=True)
    e_other = models.CharField(max_length=10, blank=True, null=True)
    w_attendance = models.CharField(max_length=10, blank=True, null=True)
    w_middle_exam = models.CharField(max_length=10, blank=True, null=True)
    w_final_exam = models.CharField(max_length=10, blank=True, null=True)
    w_project = models.CharField(max_length=10, blank=True, null=True)
    w_quiz = models.CharField(max_length=10, blank=True, null=True)
    w_presentation = models.CharField(max_length=10, blank=True, null=True)
    w_report = models.CharField(max_length=10, blank=True, null=True)
    w_practical = models.CharField(max_length=10, blank=True, null=True)
    w_other = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'tbl_course_target'

    def as_dict(self, **kwargs):
        return dict({
            'pk': self.pk,
            'key': self.pk,
            'target_name': self.target_name,
            'core_point': self.core_point,
            'e_course': self.e_course,
            'e_discussion': self.e_discussion,
            'e_experiment': self.e_experiment,
            'e_online': self.e_online,
            'e_presentation': self.e_presentation,
            'e_art': self.e_art,
            'e_seminar': self.e_seminar,
            'e_study': self.e_study,
            'e_design': self.e_design,
            'e_other': self.e_other,
            'w_attendance': self.w_attendance,
            'w_middle_exam': self.w_middle_exam,
            'w_final_exam': self.w_final_exam,
            'w_project': self.w_project,
            'w_quiz': self.w_quiz,
            'w_presentation': self.w_presentation,
            'w_report': self.w_report,
            'w_practical': self.w_practical,
            'w_other': self.w_other,
        }, **kwargs)


class CourseWeek(models.Model):
    course_class = models.OneToOneField('CourseClass', db_column='class_id', on_delete=models.CASCADE)
    week1_course = models.TextField(blank=True, null=True)
    week2_course = models.TextField(blank=True, null=True)
    week3_course = models.TextField(blank=True, null=True)
    week4_course = models.TextField(blank=True, null=True)
    week5_course = models.TextField(blank=True, null=True)
    week6_course = models.TextField(blank=True, null=True)
    week7_course = models.TextField(blank=True, null=True)
    week8_course = models.TextField(blank=True, null=True)
    week9_course = models.TextField(blank=True, null=True)
    week10_course = models.TextField(blank=True, null=True)
    week11_course = models.TextField(blank=True, null=True)
    week12_course = models.TextField(blank=True, null=True)
    week13_course = models.TextField(blank=True, null=True)
    week14_course = models.TextField(blank=True, null=True)
    week15_course = models.TextField(blank=True, null=True)
    week16_course = models.TextField(blank=True, null=True)
    week1_practice = models.TextField(blank=True, null=True)
    week2_practice = models.TextField(blank=True, null=True)
    week3_practice = models.TextField(blank=True, null=True)
    week4_practice = models.TextField(blank=True, null=True)
    week5_practice = models.TextField(blank=True, null=True)
    week6_practice = models.TextField(blank=True, null=True)
    week7_practice = models.TextField(blank=True, null=True)
    week8_practice = models.TextField(blank=True, null=True)
    week9_practice = models.TextField(blank=True, null=True)
    week10_practice = models.TextField(blank=True, null=True)
    week11_practice = models.TextField(blank=True, null=True)
    week12_practice = models.TextField(blank=True, null=True)
    week13_practice = models.TextField(blank=True, null=True)
    week14_practice = models.TextField(blank=True, null=True)
    week15_practice = models.TextField(blank=True, null=True)
    week16_practice = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_course_week'

    def as_dict(self):
        obj = {}
        for i in range(1, 16+1):
            course_key = 'week{}_course'.format(i)
            course_value = getattr(self, course_key)
            practice_key = 'week{}_practice'.format(i)
            practice_value = getattr(self, practice_key)
            obj[course_key] = course_value
            obj[practice_key] = practice_value
        return obj


class Professor(models.Model):
    professor_type = models.CharField(max_length=10)
    number = models.CharField(max_length=255, db_column='professor_number')
    name = models.CharField(max_length=255, db_column='professor_name')
    department_name = models.CharField(max_length=255)
    school_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_professor'

    def as_dict(self):
        return {
            'pk': self.pk,
            'key': self.pk,
            'professor_type': self.professor_type,
            'number': self.number,
            'name': self.name,
            'department_name': self.department_name,
            'school_number': self.school_number,
            'email': self.email,
        }

