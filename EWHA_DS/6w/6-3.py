
#######################################################################################
#
#   3. 아래는 5개 도시의 월 평균 기온입니다.
#   도시 각각의 연평균 기온을 구한 후 cityTempAvg 리스트에 저장하시오.
#
#######################################################################################

cityTempDict = {}   #   5개 도시의 월 평균 기온들을 보관하는 딕셔너리

cityTempDict['서울'] = [-8, -4, 7, 13, 21, 29, 32, 33, 27, 19, 8, -5]
cityTempDict['춘천'] = [-14, -9, 3, 9, 19, 26, 31, 32, 24, 13, 2, -9]
cityTempDict['청주'] = [-5, -3, 9, 15, 23, 28, 30, 32, 29, 20, 12, -4]
cityTempDict['광주'] = [-5, -1, 8, 17, 23, 29, 32, 33, 25, 15, 6, -3]
cityTempDict['포항'] = [-4, 3, 12, 16, 24, 30, 33, 34, 28, 22, 11, -3]

cityTempAvg = []    #   5개 도시 각각의 연 평균 기온을 저장할 리스트

for key in cityTempDict.keys():
    #   각 도시의 연 평균 기온을 구한 후 cityTempAvg 리스트에 저장하시오.
    # 대상 도시의 월 평균 기온 리스트를 얻는다.
    target = cityTempDict[key]
    # 리스트의 평균을 구한다.
    avg = calcAverage(target)
    # 평균을 결과리스트 (cityTempDict)
    avg_temp = sum(cityTempDict[key])/len(cityTempDict[key])
    cityTempAvg.append(round(avg_temp,2))

print(cityTempAvg)  # 결과 확인


def calcAverage(target):
