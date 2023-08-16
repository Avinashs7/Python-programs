#function to identify the phone number using regural expression
import re
def isPhone(num):
    pattern="^\+91[0-9]{10}$"
    result=re.match(pattern,num)
    if result:
        print("The phone number is",num)
    # else:
    #     print("Failure")
#function to identify the Gmail using regural expression
def isGmail(str):
    pattern="[0-9A-Za-z._]+@gmail.com$"
    result=re.match(pattern,str)
    if(result):
        print("The gmail is",str)
    # else:
    #     print("Failure")
with open ("avinash.txt","r+") as file:
    rd=file.read()
    for str in rd.split("\n"):
        for word in str.split(","):
            isPhone(word)
            isGmail(word)