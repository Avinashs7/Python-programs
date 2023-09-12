fname=input("Enter the filename\n")
with open (fname,'r') as file:
    n=int(input("Enter number of lines need to be read from file\n"))
    for i in range(n):
        line=file.readline()
        print(f'{i+1} Line :{line}')
    file.seek(0)
    str=input("Enter a word\n")
    cnt=0
    for line in file:
        list=line.split()
        cnt=cnt+list.count(str)
    print("The word ",str," has occured ",cnt," Times")