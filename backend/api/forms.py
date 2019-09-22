from django import forms
from .models import CourseClass, CourseTarget, CoursePercent, CourseBook, CourseWeek
from .models import CourseCondition, CourseStruct


class CourseClassForm(forms.ModelForm):
    class Meta:
        model = CourseClass
        fields = ('design_content', 'check_content', 'report_content', 'exe_content')


class CourseTargetForm(forms.ModelForm):
    class Meta:
        model = CourseTarget
        fields = (
            'e_course', 'e_discussion', 'e_experiment', 'e_online', 'e_presentation',
            'e_art', 'e_seminar', 'e_study', 'e_design', 'e_other', 'w_attendance',
            'w_middle_exam', 'w_final_exam', 'w_project', 'w_quiz', 'w_presentation',
            'w_report', 'w_practical', 'w_other',
        )


class CoursePercentForm(forms.ModelForm):
    class Meta:
        model = CoursePercent
        fields = (
            'task', 'final_exam', 'other', 'presentation', 'report',
            'practical', 'middle_exam', 'attendance', 'quiz',
        )

    def clean(self):
        data = self.cleaned_data
        if sum(data.values()) != 100:
            raise forms.ValidationError('총합이 100이어야 합니다.')
        return data


class CourseBookForm(forms.ModelForm):
    class Meta:
        model = CourseBook
        fields = (
            'consult_time', 'pre_knowledge', 'main_note', 'sub_note1', 'sub_note2',
            'sub_note3', 'ref_web', 'select_book',
        )


class CourseWeekForm(forms.ModelForm):
    class Meta:
        model = CourseWeek
        fields = tuple(
            ['week%d_course' % i for i in range(1, 16+1)] +
            ['week%d_practice' % i for i in range(1, 16+1)]
        )


class CourseConditionForm(forms.ModelForm):
    class Meta:
        model = CourseCondition
        fields = ('c_code', 'c_method', 'c_content')


class CourseStructForm(forms.ModelForm):
    class Meta:
        model = CourseStruct
        fields = ('s_code', 's_method', 's_content')
