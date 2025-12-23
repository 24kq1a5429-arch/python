def calculate(m,n):
    sum=0
    for i in range(m,n+1):
        if(i%3==0 and i%5==0):
            sum=sum+i
    return sum
m=int(input("m:"))
n=int(input("n:"))
result=calculate(m,n)
print(result)
