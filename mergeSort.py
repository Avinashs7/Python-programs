def merge(rlist,llist):
    Nlist=[]
    left,right=0,0
    while(len(llist)>left and len(rlist)>right):
        if(llist[left]<rlist[right]):
            Nlist.append(llist[left])
            left+=1
        else:
            Nlist.append(rlist[right])
            right+=1
    while(len(llist)>left):
        Nlist.append(llist[left])
        left+=1
    while(len(rlist)>right):
        Nlist.append(rlist[right])
        right+=1
    return Nlist
def sort(list):
    if(len(list)<2):
        return list
    mid = len(list)//2
    rlist=list[0:mid]
    llist=list[mid:]
    rlist=sort(rlist)
    llist=sort(llist)
    return merge(rlist,llist)
list=[]
n=int(input("Enter size of array\n"))
print("Enter array elements\n")
for i in range (n):
    list.append(int(input()))
print(list)
print(sort(list))
