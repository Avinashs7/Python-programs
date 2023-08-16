def number(sentence):
    l,u,w,d=0,0,1,0
    for letter in sentence:
        if letter==' ':
            w+=1
        elif letter>='A' and letter<='Z':
            u+=1
        elif letter>='a' and letter<='z':
            l+=1
        elif letter>='0' and letter<='9':
            d+=1
    print("Uppercase: ",u,"Lowercase: ",l,"Digit: ",d,"word: ",w)
sentence=input("Enter a sentence\n")    
number(sentence)         