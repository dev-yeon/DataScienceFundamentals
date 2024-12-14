
import pandas as pd

df = pd.read_csv('/Users/yeon/PycharmProjects/DataScienceFundamentals/EWHA_DS/11w/blood_pressure.csv')

#############################################################
# 
#   파일에서 읽은 데이터의 형태와 내용을 확인합니다.
# 
#############################################################

print('type(df):', type(df))
print('df.head(5):\n', df.head(5))
print('df.shape:', df.shape)
print('df.dtypes:', df.dtypes)

#############################################################
# 
#   1. 데이터의 49번째 행(row)부터 58번째 행을 읽고 그 데이터를 화면에 출력하시오.
# 
#############################################################
print('  1. 데이터의 49번째 행(row)부터 58번째 행을 읽고 그 데이터를 화면에 출력하시오.')
df2 = df.iloc[49:59, :]
print(df2)

#############################################################
# 
#   2. 데이터의 49번째 행(row)부터 58번째 행의 'bp_before', 'bp_after 열(column)을 읽고 화면에 출력하시오.
# 
#############################################################
print(" 2. 데이터의 49번째 행(row)부터 58번째 행의 'bp_before', 'bp_after 열(column)을 읽고 화면에 출력하시오.")
# print(df.loc[0:2, "val":"alias"])
df3 = df2.loc[49:59, ['bp_before', 'bp_after']]

print(df3)
#############################################################
#
#   3. 데이터에서 투약 이전 평균혈압(bp_before)이 170 이상인 실험군을 화면에 출력하시오. 
#
#############################################################
print('3. 데이터에서 투약 이전 평균혈압(bp_before)이 170 이상인 실험군을 화면에 출력하시오. ')
df4 = df[df['bp_before'] >= 170]
print(df4)


#############################################################
#
#   4. 데이터에서 투약 이전 평균혈압(bp_before)이 170 이상 190 이하인 실험군을 화면에 출력하시오.
#
#############################################################

print(' 4. 데이터에서 투약 이전 평균혈압(bp_before)이 170 이상 190 이하인 실험군을 화면에 출력하시오.')

df5 = df[(df['bp_before'] >= 170) & (df['bp_before'] <=190)]
print(df5)