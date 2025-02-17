students = {'S21-0001':{'이름':'최성훈',
                        '성구분':'M',
                        '전공':'디자인',
                        '연락처':'010-1234-5678',
                        '메일':'hun@gmail.com',
                        '취미':['농구', '음악']},
            'S21-0002': {'이름': '탁영우',
                         '성구분': 'M',
                         '전공': '바리스타',
                         '연락처': '010-5678-9012',
                         '메일': 'yeong@gmail.com',
                         '취미': ['축구']},
            'S21-0003': {'이름': '황진영',
                         '성구분': 'W',
                         '전공': '음악',
                         '연락처': '010-9012-3456',
                         '메일': 'jin@gmail.com',
                         '취미': ['수영', '코딩']}
            }

for k1 in students.keys():
    print('-' * 40)
    print('회원번호 : {}'.format(k1))

    student = students[k1]
    for k2 in student.keys():
        print('{} : {}'.format(k2, student[k2]))


memNo = input('조회할 회원번호를 입력하세요.: ')
print('{} : {}'.format(memNo, students[memNo]))
