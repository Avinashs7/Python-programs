def average(n1,n2,n3):
    if(n1==min(n1,n2,n3)):
        return (n2+n3)/2
    elif(n2==min(n1,n2,n3)):
        return (n1+n3)/2
    else:
        return (n1+n2)/2
n1=int(input("Enter two numbers\n"))
n2=int(input())
n3=int(input())
print(average(n1,n2,n3))