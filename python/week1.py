# week1 시간 복잡도

#=================================================
# 백준 2751번 수 정렬하기
# 1번 버블 정렬 이용하기(시간 초과로 틀림)

# n = int(input())
# data = []
# for i in range(n):
#     data.append(int(input()))


# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         if(data[j] > data[j+1]):
#             temp = data[j]
#             data[j] = data[j+1]
#             data[j+1] = temp

# for i in range(n):
#     print(data[i])

# 2번 파이썬 기본 정렬 함수 이용
# import sys
# n = int(input())
# data = []
# for i in range(n):
#     data.append(int(sys.stdin.readline()))
# data.sort()

# for i in range(n):
#     print(data[i])

#=================================================
# 11651 좌표 정렬하기
# res 부분 잘 생각하기
# x,y 중 y먼저 정렬인 것 생각하기
import sys
input = sys.stdin.readline
n = int(input())

data = []
for i in range(n):
    x, y = map(int, input().split())
    data.append([y,x])
res = sorted(data)
for i in range(n):
    print(res[i][1], res[i][0])