aboutPython = '파이썬은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어이다.'

splitList = aboutPython.split()
print(splitList)

dic = {}
for idx, v in enumerate(splitList):
    dic[idx] = v

print(dic)



# words = {'꺼지다':'가다',
#          '쩔다':'엄청나다',
#          '짭새':'경찰관',
#          '꼽사리':'중간에 낀 사람',
#          '먹튀':'먹고 도망',
#          '지린다':'겁을 먹다',
#          '쪼개다':'웃다',
#          '뒷담 까다':'험담하다'}
#
# txt = '강도는 서로 쪼개다, 짭새를 보고 빠르게 따돌리며 먹튀했다.'
#
# keys = list(words.keys())
#
# txtMod = ''
# for key in keys:
#     if key in txt:
#         print('key: {}'.format(key))
#         print('words[{}]: {}'.format(key, words[key]))
#         txt = txt.replace(key, words[key])
#
# print(txt)