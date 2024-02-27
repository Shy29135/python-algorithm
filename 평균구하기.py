""" 백준온라인 저지 1546번 
     1번째 줄에 시험을 본 과목의 갯수가 주어짐!(해당값은 1000보다 작거나 같다.)
     2번째 줄 세준이의 현재성적! (해당값은 100보다 작거나 같고, 음이 아닌 정수)
     적어도 1개의 값은 0보다 크다. """

''' 문제 분석하기 
    최고점수를 기준으로 전체 점수를 다시 계산, 모든 점수를 입력 받은 후, 최고점을 별도로 지정!
    n에 과목의 수 입력,mylist에 점수 정보 저장, mymax에 정보 중 최대값 저장, sum에 mylist 모든 데이터 값 더하기'''

n=int(input()) #과목 수
test_list=list(map(int,input().split()))
max_score=max(test_list)

new_list=[]
for score in test_list :
    new_list.append(score/max_score*100)  
  #새로운 점수 생성 
#(append는 list에 새로운 부분(append뒤에 다가 작성)을 더해서 출력!)
test_avg=sum(new_list)/n
print(test_avg)    
  
