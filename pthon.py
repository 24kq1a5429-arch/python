n=int(input("Enter a number"))
m=int(input("Enter a number"))
sum1 = 0
sum2 = 0

for i in range(1,m+1):
    if(i%n==0):
        sum1=sum1+i
    else:
        sum2=sum2+i
a=sum2-sum1
print(a)
