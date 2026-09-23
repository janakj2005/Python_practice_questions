
#Write a program which can compute the factorial of a given numbers.The
#results should be printed in a comma-separated sequence on a single
#line.Suppose the following input is supplied to the program:8
#Then, the output should be:40320*/

a=int(input())
fact=1
for i in range(1,a+1):
    fact*=i;
print("Factorial of the given number",a,"is:",fact)
    

#Write a Python program that accepts a sentence and calculate the number of
#letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

s=input()
dig=0
let=0
for i in s:
    if(i.isdigit()):
        dig+=1
    elif(i.isalpha()):
        let+=1
print("LETTERS:",let)
print("DIGITS:",dig)




#Write a Python program which accepts a sequence of comma separated 4 digit
#binary numbers as its input and then check whether they are divisible by 5 or not.
#The numbers that are divisible by 5 are to be printed in a comma separated
#sequence.
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010

s=input().split(",")
l=[]
for i in s:
    r=i[::-1]
    pow=0
    val=0
    for j in r:
        if(j=='1'):
            val+=2**pow
        pow+=1
    if(val%5==0):    
        l.append(i)
print(l)
        





























