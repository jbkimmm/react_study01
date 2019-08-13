# Generated by Django 2.2.3 on 2019-07-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_year', models.CharField(max_length=10)),
                ('season', models.CharField(max_length=10)),
                ('display_name', models.CharField(max_length=255)),
                ('cert_type', models.CharField(max_length=10)),
                ('main_professor', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_course',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CourseBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('consult_time', models.CharField(blank=True, max_length=255, null=True)),
                ('pre_knowledge', models.CharField(blank=True, max_length=255, null=True)),
                ('main_note', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_note1', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_note2', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_note3', models.CharField(blank=True, max_length=255, null=True)),
                ('ref_web', models.CharField(blank=True, max_length=255, null=True)),
                ('select_book', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_course_book',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CourseClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('class_code', models.CharField(max_length=100)),
                ('cert_type', models.CharField(max_length=100)),
                ('base_type', models.CharField(max_length=100)),
                ('auth_type', models.CharField(max_length=100)),
                ('design_type', models.CharField(max_length=100)),
                ('design_point', models.IntegerField()),
                ('content', models.TextField(blank=True, null=True)),
                ('pre_content', models.CharField(blank=True, max_length=100, null=True)),
                ('test_content', models.TextField(blank=True, null=True)),
                ('design_content', models.TextField(blank=True, null=True)),
                ('check_content', models.TextField(blank=True, null=True)),
                ('report_content', models.TextField(blank=True, null=True)),
                ('exe_content', models.TextField(blank=True, null=True)),
                ('sub_professor', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_course_class',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CourseCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('c_code', models.CharField(blank=True, max_length=255, null=True)),
                ('c_method', models.CharField(blank=True, max_length=255, null=True)),
                ('c_content', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_course_condition',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CourseCore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('percnet', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tbl_course_core',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CoursePercent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('task', models.IntegerField()),
                ('final_exam', models.IntegerField()),
                ('other', models.IntegerField()),
                ('presentation', models.IntegerField()),
                ('report', models.IntegerField()),
                ('practical', models.IntegerField()),
                ('middle_exam', models.IntegerField()),
                ('attendance', models.IntegerField()),
                ('quiz', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_course_percent',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CourseStruct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('s_code', models.CharField(blank=True, max_length=255, null=True)),
                ('s_method', models.CharField(blank=True, max_length=255, null=True)),
                ('s_content', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_course_struct',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CourseSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('subject_type', models.CharField(max_length=100)),
                ('subject_code', models.CharField(max_length=100)),
                ('subject_name', models.CharField(max_length=255)),
                ('subject_day', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('end_time', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
                ('make_department', models.CharField(max_length=100)),
                ('subject_point', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_course_subject',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CourseTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('target_name', models.CharField(max_length=255)),
                ('core_point', models.IntegerField()),
                ('e_course', models.CharField(blank=True, max_length=10, null=True)),
                ('e_discussion', models.CharField(blank=True, max_length=10, null=True)),
                ('e_experiment', models.CharField(blank=True, max_length=10, null=True)),
                ('e_online', models.CharField(blank=True, max_length=10, null=True)),
                ('e_presentation', models.CharField(blank=True, max_length=10, null=True)),
                ('e_art', models.CharField(blank=True, max_length=10, null=True)),
                ('e_seminar', models.CharField(blank=True, max_length=10, null=True)),
                ('e_study', models.CharField(blank=True, max_length=10, null=True)),
                ('e_design', models.CharField(blank=True, max_length=10, null=True)),
                ('e_other', models.CharField(blank=True, max_length=10, null=True)),
                ('w_attendance', models.CharField(blank=True, max_length=10, null=True)),
                ('w_middle_exam', models.CharField(blank=True, max_length=10, null=True)),
                ('w_final_exam', models.CharField(blank=True, max_length=10, null=True)),
                ('w_project', models.CharField(blank=True, max_length=10, null=True)),
                ('w_quiz', models.CharField(blank=True, max_length=10, null=True)),
                ('w_presentation', models.CharField(blank=True, max_length=10, null=True)),
                ('w_report', models.CharField(blank=True, max_length=10, null=True)),
                ('w_practical', models.CharField(blank=True, max_length=10, null=True)),
                ('w_other', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'tbl_course_target',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CourseWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('week1_course', models.TextField(blank=True, null=True)),
                ('week2_course', models.TextField(blank=True, null=True)),
                ('week3_course', models.TextField(blank=True, null=True)),
                ('week4_course', models.TextField(blank=True, null=True)),
                ('week5_course', models.TextField(blank=True, null=True)),
                ('week6_course', models.TextField(blank=True, null=True)),
                ('week7_course', models.TextField(blank=True, null=True)),
                ('week8_course', models.TextField(blank=True, null=True)),
                ('week9_course', models.TextField(blank=True, null=True)),
                ('week10_course', models.TextField(blank=True, null=True)),
                ('week11_course', models.TextField(blank=True, null=True)),
                ('week12_course', models.TextField(blank=True, null=True)),
                ('week13_course', models.TextField(blank=True, null=True)),
                ('week14_course', models.TextField(blank=True, null=True)),
                ('week15_course', models.TextField(blank=True, null=True)),
                ('week16_course', models.TextField(blank=True, null=True)),
                ('week1_practice', models.TextField(blank=True, null=True)),
                ('week2_practice', models.TextField(blank=True, null=True)),
                ('week3_practice', models.TextField(blank=True, null=True)),
                ('week4_practice', models.TextField(blank=True, null=True)),
                ('week5_practice', models.TextField(blank=True, null=True)),
                ('week6_practice', models.TextField(blank=True, null=True)),
                ('week7_practice', models.TextField(blank=True, null=True)),
                ('week8_practice', models.TextField(blank=True, null=True)),
                ('week9_practice', models.TextField(blank=True, null=True)),
                ('week10_practice', models.TextField(blank=True, null=True)),
                ('week11_practice', models.TextField(blank=True, null=True)),
                ('week12_practice', models.TextField(blank=True, null=True)),
                ('week13_practice', models.TextField(blank=True, null=True)),
                ('week14_practice', models.TextField(blank=True, null=True)),
                ('week15_practice', models.TextField(blank=True, null=True)),
                ('week16_practice', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_course_week',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_type', models.CharField(max_length=10)),
                ('professor_number', models.CharField(max_length=255)),
                ('professor_name', models.CharField(max_length=255)),
                ('department_name', models.CharField(max_length=255)),
                ('school_number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_professor',
                'managed': True,
            },
        ),
    ]