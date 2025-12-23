def givenresult(s1,s2,s3):
    if s1<s2:
        return "Good"
    elif s1>=s2 and s1<=s3:
        return "Best"
    else:
        return "Can do better"
s1=int(input("enter s1:"))
s2=int (input("enter s2:"))
s3=int(input("enter s3:"))
print(givenresult(s1,s2,s3))
