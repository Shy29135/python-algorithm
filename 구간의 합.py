"""질의(1,3)=S[3]-S[0]
    suNo(숫자개수),quizNo(질의갯수)
    numbers 변수에 숫자 데이터 저장
    prefix_sum 합 배열 변수 선언
    temp 변수선언
    
    for 저장한 숫자 데이터 차례대로 탐색
    temp에 현재 숫자 데이터 더해주기
    합 배열에 temp값 저장
    
    for 질의 개수만큼 반복:
    질의 범위 받기(s~e) 
    구간 합 출력하기(perfix_sum[e]-perfix_sum[s-1])"""


''' ## 
import sys
for line in sys.stdin :	# 한줄로 입력된 얘들이 하나로 출력됨
	print(line)
    
##
import sys
for each in sys.stdin.readline() :	# 한줄로 입력한 얘들이  각각 출력됨
	print(each)


'''

import sys
input=sys.stdin.readline #시간절약 개행문자 "" 이것도 그대로 출력!
suNO,quizNo=map(int,input().split())
numbers=list(map(int,input().split()))
prefix_sum=[0]
temp=0

for i in numbers:
    temp=temp+i
    prefix_sum.append(temp) #합 배열 만들기

for i in range(quizNo):
 s,e=map(int,input().split())
 print(prefix_sum[e]-prefix_sum[s-1])

