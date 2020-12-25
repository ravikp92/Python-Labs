# Files 
f=open('Training\\sample.txt','r') # read mode- default
data=f.read()
print(data)
f.close()

f1=open('Training\\sample.txt','r')
data2=f1.read(5)
print(data2)
f1.close()

f2=open('Training\\sample.txt','r')
print(f2.readline()) # read a line at a time
print(f2.readline())  # read a line at a time
f2.close()

fwrite=open('Training\\sample2.txt','w')
fwrite.write("Please write this to file")
fwrite.close()

fappend=open('Training\\sample2.txt','a')
fappend.write("Please write this to file")
fappend.close()


with open('sample2.txt','w') as f:
    a=f.write("me")
print(a)

#  find number of times 'you' is written in file 

f= open('sample.txt')
t=f.read()
if 'you' in t:
    print("you is present")
else:
    print("you is not present")
    
f.close()


#  game high scorer of file 
def game():
    return 101

score=game()
with open("Training\\highscore.txt") as f:
        hiscore=f.read()
if(hiscore == ''):
    hiscore=0
if(int(hiscore)<score):
           with open("Training\\highscore.txt", 'w') as f1:
                f1.write(str(score))




# find some word in log file and also print line number 
content =True
i=1
with open("log.txt") as f:
    while(content):
        content=f.readline()
        if('python' in content.lower()):
            print(content)
            print(f" python is present in {i}")
        i=i+1
        

# rename a file 

import os
oldname='sample.txt'
newname='rename_sample.txt'

with open(oldname) as f:
    content=f.read()
with open(newname,'w') as f:
    f.write(content)

os.remove(oldname)