

#Answer of question 1
str1="To check reverse"
print("Reversed order of the string;",str1[::-1])

#Answer of question 2
d=int(input("Enter the number, you want the numbers divisible by:"))
print("Enter the range of numbers divisible by given number")
r1=int(input("From: "))
r2=int(input("to: "))

for i in range(r1,r2) :
    if i%d==0:
        print(i)


 #Answer of question 3

import math
s1=int(input("Enter the length of a side of the triangle(cm):"))
s2=int(input("Enter the length of 2nd side of the triangle(cm):"))
s3=int(input("Enter the length of 3rd side of the triangle(cm):"))
s=(s1+s2+s3)/2
ar=(s*(s-s1)*(s-s2)*(s-s3))
if s1+s2>s3 or s2+s3>s1 or s1+s3>s2:
    print("Area of the triangle:",math.sqrt(ar),"cm2")

else :
    print("please enter proper side length!")



     #Answer of question 4


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')





#Answer of question 5

n=int(input("Enter the number of rows, you want for the triangle:"))

for i in range (65,65+n):
    alpha = i
   
    for j in range(65,i+1):
        print(chr(alpha),end="")
        alpha+=1
        
    print()
#Answer of question 6
lower_value = int(input("Enter the Lowest Range Value : "))  
upper_value = int(input("Enter the Upper Range Value : "))
print ("The Prime Numbers in this range are : ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print(number,end="")

    print("")



    
#Answer of quesion 7

for i in range(1,501):
    if i%7==0 and i%11==0:
        print(i)

#Answer of question 8

print("Enter the values of 10 integer:")
a1=int(input("i)"))
a2=int(input("ii)"))
a3=int(input("iii)"))
a4=int(input("iv)"))
a5=int(input("v)"))
a6=int(input("vi)"))
a7=int(input("vii)"))
a8=int(input("viii)"))
a9=int(input("ix)"))
a10=int(input("x)"))
num=(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)
odd=0
even=0
pos=0
neg=0
time=0
lst=[]
lst2=[]
#(c) and (d)
for x in num:
    
    if not x%2  :
        even+=1 
        
        lst.append(x)
        
      
    
    else  :
        odd+=1
        lst2.append(x)
print("odd numbers are :",lst2)
print("Even numbers are :",lst, end="")
print("\n Number of even numbers :",even)
print("Number of odd numbers :",odd)
#(a)and (b)
for x in num:
    if x>=0:
        pos+=1
    else:
        neg+=1
print("Number of positive number :",pos)
print("Number of negative number :",neg)

        


        
    


        


#Answer of question 9

string=str(input("Enter string:"))
word=str(input("Enter word:"))
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Count of the word is:")
print(count)
    
        
    
    
