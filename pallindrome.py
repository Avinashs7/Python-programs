def ispallindrome(num):
    num1=int(num)
    rev=0
    while num1>0:
        rem=num1%10
        rev=rev*10+rem
        num1=num1//10
    if(rev==int(num)):
        print("pallindrome")
def occurence(num):
    array=[int(x) for x in num]
    for x in set(array):
        print(x,"has repeated ",array.count(x),"number of times")
        array.remove(x)
num=input()
ispallindrome(num)
occurence(num)