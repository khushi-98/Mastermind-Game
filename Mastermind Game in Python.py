import random 

print("Welcome to Mastermind game!!")

num=random.randint(1000,10000)
#print(num)

print("Enter your number:-")
num1=int(input())

if num==num1:
    print("Congratulation,You are the true mastermind")
else:
    
    result=['x']*4
    r=str(result)
    while(num1!=num):
         r1=str(num)
         r2=str(num1)
         count=0

        #  print(r1)
         list=[]

         for i in range(0,4):
                if r1[i]==r2[i]:
                    result[i]=r1[i]
                    count=count+1
                    list.append(r1[i])
                else:
                    
                     continue
           
         print("You have ",count," correct digits")
         print(list)
         num1=int(input("Enter another number of your choice"))
         print("\n")

         if(count==0):
                print("None of numbers has matched")
                num1=int(input("Enter your next choice:-"))

    if num==num1:
         print("You have cracked it!!!")
         print("Yeah!!You have became a Mastermind")


    



    
    