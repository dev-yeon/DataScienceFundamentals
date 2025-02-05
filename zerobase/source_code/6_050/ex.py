import mod

lottoNums = [[13, 23, 15, 5, 6, 39], [36, 13, 5, 3, 30, 16], [43, 1, 15, 9, 3, 38],
             [32, 42, 24, 45, 8, 31], [18, 39, 41, 11, 4, 9], [12, 39, 11, 38, 32, 5],
             [29, 25, 13, 6, 14, 8], [21, 33, 19, 20, 42, 7], [6, 28, 3, 45, 41, 24],
             [42, 15, 8, 5, 35, 4], [14, 4, 35, 24, 29, 3], [15, 20, 6, 37, 34, 39],
             [27, 5, 32, 15, 25, 19], [45, 25, 2, 8, 30, 43], [4, 19, 33, 10, 6, 24],
             [25, 26, 45, 23, 24, 16], [33, 28, 45, 21, 38, 24], [4, 30, 29, 28, 32, 38],
             [11, 28, 12, 2, 42, 3], [40, 29, 16, 8, 9, 28], [6, 9, 37, 30, 3, 35],
             [29, 18, 41, 28, 38, 15], [9, 31, 13, 44, 1, 36], [36, 1, 37, 32, 15, 12],
             [41, 32, 16, 6, 26, 33], [12, 43, 10, 29, 39, 9], [41, 9, 23, 35, 18, 17],
             [35, 38, 3, 28, 36, 31], [21, 44, 4, 29, 18, 7], [20, 23, 6, 2, 34, 44]]

lm = mod.LottoMode(lottoNums)
mList = lm.getLottoNumMode()
# print(f'mList: {mList}')

lm.printModeList()