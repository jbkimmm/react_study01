import pymysql
import random

conn = pymysql.connect(
    host='182.237.86.248', 
    user='cmsuser', 
    password='cmsuser',
    db='www', 
    charset='utf8'
)

yesno = ['Y', 'N']
txtbox = [
    'I want to enjoy things',
    'and have fun and live like every day is the last day',
    'Were the people that live',
    'They cant wipe us out, they cant lick us',
    'The only thing Im afraid of is wasting the rest',
    'When the Lore closes a door,somewher he opens a window',
    'Great power always comes',
    'if you get all tangled up, you just tango on',
    'To Sin By Silence When We Should Protest Makes Cowards Out Of Men',
    'What is it, major Lawrence, that attracts you personally to the desert?',
    'If you do not love me, I love you enough for both',
    'Love means never having to say youre sorry',
    'You always did look pretty, just pretty nigh good enough to eat',
    'Threr shouldt be bars. Behind bars, a man never reforms',
    "I pray thee, strengthen me, O God,strengthen me only this once.",
    "The only way youre gonna survive is to do what you think is right",
    "The time when there was no kindnessin the world",
    "Its awful not to be loved, itsthe worst thing in the world",
    "Have you got fed up with freedom?",
    "You could be happy here. I could take care of you"
]
print( random.randrange(0,2) )

curs = conn.cursor()

for x in txtbox:
    sql = '''
    insert into tbl_course_target(class_id, target_name, core_point, e_course, e_discussion, e_experiment, e_online, e_presentation, e_art, e_seminar, e_study, e_design, e_other, w_attendance, w_middle_exam, w_final_exam, w_project, w_quiz, w_presentation, w_report, w_practical, w_other)
    values(
    '{d}',
    '{x}',
    '{x1}',
    '{a1}',
    '{a2}',
    '{a3}',
    '{a4}',
    '{a5}',
    '{a6}',
    '{a7}',
    '{a8}',
    '{a9}',
    '{a10}',
    '{a11}',
    '{a12}',
    '{a13}',
    '{a14}',
    '{a15}',
    '{a16}',
    '{a17}',
    '{a18}',
    '{a19}');
    '''.format(
        x = x,
        d = str(random.randrange(1,9)),
        x1 = str(random.randrange(1,10)),
        a1 = yesno[random.randrange(0,2)],
        a2 = yesno[random.randrange(0,2)],
        a3 = yesno[random.randrange(0,2)],
        a4 = yesno[random.randrange(0,2)],
        a5 = yesno[random.randrange(0,2)],
        a6 = yesno[random.randrange(0,2)],
        a7 = yesno[random.randrange(0,2)],
        a8 = yesno[random.randrange(0,2)],
        a9 = yesno[random.randrange(0,2)],
        a10 = yesno[random.randrange(0,2)],
        a11 = yesno[random.randrange(0,2)],
        a12 = yesno[random.randrange(0,2)],
        a13 = yesno[random.randrange(0,2)],
        a14 = yesno[random.randrange(0,2)],
        a15 = yesno[random.randrange(0,2)],
        a16 = yesno[random.randrange(0,2)],
        a17 = yesno[random.randrange(0,2)],
        a18 = yesno[random.randrange(0,2)],
        a19 = yesno[random.randrange(0,2)],
    )
    print(sql)
    curs.execute(sql)
conn.commit()
 
conn.close()