korScore = int(input('국어 점수 입력: '))
engScore = int(input('영어 점수 입력: '))
matScore = int(input('수학 점수 입력: '))

totalScore = korScore + engScore + matScore
avgScore = totalScore / 3

maxScore = korScore
maxSubject = '국어'
if engScore > maxScore:
    maxScore = engScore
    maxSubject = '영어'
if matScore > maxScore:
    maxScore = matScore
    maxSubject = '수학'

minScore = korScore
minSubject = '국어'
if engScore < minScore:
    minScore = engScore
    minSubject = '영어'
if matScore < minScore:
    minScore = matScore
    minSubject = '수학'

difScore = maxScore - minScore

print('총점: {}'.format(totalScore))
print('평균: %.2f' % avgScore)
print('-' * 30)
print('최고 점수 과목(점수): {}({})'.format(maxSubject, maxScore))
print('최저 점수 과목(점수): {}({})'.format(minSubject, minScore))
print('최고, 죄저 점수 차이: {}'.format(difScore))
print('-' * 30)

