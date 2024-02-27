"""N개의 숫자가 공백없이 써 있다!, 이 숫자를 
   모두 합해 출력하는 프로그램을 구하시오."""
n=input()
numbers=list(input())
sum=0

for i in numbers:
    sum=sum+int(i)

print(sum)