def roman_to_decimal(num):
    dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500}
    num=num[::-1]
    pre=num[0]
    sum=dict[pre]
    for digit in num[1:]:
        if(dict[pre]>dict[digit]):
            sum=sum-dict[digit]
        else:
            sum=sum+dict[digit]
        pre=digit
    return sum
print(roman_to_decimal("IX"))