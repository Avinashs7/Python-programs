def sort(list):
    for i in range(1,len(list)):
        j=i-1
        k=list[i]
        while j>=0 and k<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=k
    print(list)
list=[]
n=int(input("Enter the size of array\n"))
for i in range (n):
    list.append(int(input()))
print(list)
sort(list)
