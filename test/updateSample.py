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

for x in range(1, 9):
    sql = '''
        UPDATE `www`.`tbl_course_week` 
        SET 
        `week1_course` = '{c1}', 
        `week2_course` = '{c2}', 
        `week3_course` = '{c3}', 
        `week4_course` = '{c4}', 
        `week5_course` = '{c5}', 
        `week6_course` = '{c6}', 
        `week7_course` = '{c7}', 
        `week8_course` = '{c8}', 
        `week9_course` = '{c9}', 
        `week10_course` = '{c10}', 
        `week11_course` = '{c11}', 
        `week12_course` = '{c12}', 
        `week13_course` = '{c13}', 
        `week14_course` = '{c14}', 
        `week15_course` = '{c15}', 
        `week16_course` = '{c16}', 
        `week1_practice` = '{p1}', 
        `week2_practice` = '{p2}', 
        `week3_practice` = '{p3}', 
        `week4_practice` = '{p4}', 
        `week5_practice` = '{p5}', 
        `week6_practice` = '{p6}', 
        `week7_practice` = '{p7}', 
        `week8_practice` = '{p8}', 
        `week9_practice` = '{p9}', 
        `week10_practice` = '{p10}', 
        `week11_practice` = '{p11}', 
        `week12_practice` = '{p12}', 
        `week13_practice` = '{p13}', 
        `week14_practice` = '{p14}', 
        `week15_practice` = '{p15}', 
        `week16_practice` = '{p16}' 
        WHERE (`id` = '{x}');
    '''.format(
        x=x,
       c1=txtbox[random.randrange(0,20)],
       c2=txtbox[random.randrange(0,20)],
       c3=txtbox[random.randrange(0,20)],
       c4=txtbox[random.randrange(0,20)],
       c5=txtbox[random.randrange(0,20)],
       c6=txtbox[random.randrange(0,20)],
       c7=txtbox[random.randrange(0,20)],
       c8=txtbox[random.randrange(0,20)],
       c9=txtbox[random.randrange(0,20)],
       c10=txtbox[random.randrange(0,20)],
       c11=txtbox[random.randrange(0,20)],
       c12=txtbox[random.randrange(0,20)],
       c13=txtbox[random.randrange(0,20)],
       c14=txtbox[random.randrange(0,20)],
       c15=txtbox[random.randrange(0,20)],
       c16=txtbox[random.randrange(0,20)],
       p1=txtbox[random.randrange(0,20)],
       p2=txtbox[random.randrange(0,20)],
       p3=txtbox[random.randrange(0,20)],
       p4=txtbox[random.randrange(0,20)],
       p5=txtbox[random.randrange(0,20)],
       p6=txtbox[random.randrange(0,20)],
       p7=txtbox[random.randrange(0,20)],
       p8=txtbox[random.randrange(0,20)],
       p9=txtbox[random.randrange(0,20)],
       p10=txtbox[random.randrange(0,20)],
       p11=txtbox[random.randrange(0,20)],
       p12=txtbox[random.randrange(0,20)],
       p13=txtbox[random.randrange(0,20)],
       p14=txtbox[random.randrange(0,20)],
       p15=txtbox[random.randrange(0,20)],
       p16=txtbox[random.randrange(0,20)]
    )
    print(sql)
    curs.execute(sql)
conn.commit()
 
conn.close()