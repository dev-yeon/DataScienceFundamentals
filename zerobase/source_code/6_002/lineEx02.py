nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
print(f'nums: {nums}')
print(f'nums length: {len(nums)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdxs = []

nums.append(searchData)

n = 0
while True:

    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdxs.append(n)
        else:
            break

    n += 1

print(f'nums: {nums}')
print(f'nums length: {len(nums)}')
print(f'searchResultIdxs: {searchResultIdxs}')
print(f'searchResultCnts: {len(searchResultIdxs)}')