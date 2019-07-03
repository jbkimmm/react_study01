# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblCourse(models.Model):
    course_year = models.CharField(max_length=10)
    season = models.CharField(max_length=10)
    display_name = models.CharField(max_length=255)
    cert_type = models.CharField(max_length=10)
    main_professor = models.IntegerField()

    class Meta:
        db_table = 'tbl_course'


class TblCourseBook(models.Model):
    class_id = models.IntegerField()
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


class TblCourseClass(models.Model):
    course_id = models.IntegerField()
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
    sub_professor = models.IntegerField()

    class Meta:
        db_table = 'tbl_course_class'


class TblCourseCondition(models.Model):
    class_id = models.IntegerField()
    c_code = models.CharField(max_length=255, blank=True, null=True)
    c_method = models.CharField(max_length=255, blank=True, null=True)
    c_content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_course_condition'


class TblCourseCore(models.Model):
    class_id = models.IntegerField()
    content = models.CharField(max_length=255, blank=True, null=True)
    percnet = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'tbl_course_core'


class TblCoursePercent(models.Model):
    class_id = models.IntegerField()
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


class TblCourseStruct(models.Model):
    class_id = models.IntegerField()
    s_code = models.CharField(max_length=255, blank=True, null=True)
    s_method = models.CharField(max_length=255, blank=True, null=True)
    s_content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_course_struct'


class TblCourseSubject(models.Model):
    class_id = models.IntegerField()
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


class TblCourseTarget(models.Model):
    class_id = models.IntegerField()
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


class TblCourseWeek(models.Model):
    class_id = models.IntegerField()
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


class TblProfessor(models.Model):
    professor_type = models.CharField(max_length=10)
    professor_number = models.CharField(max_length=255)
    professor_name = models.CharField(max_length=255)
    department_name = models.CharField(max_length=255)
    school_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_professor'
