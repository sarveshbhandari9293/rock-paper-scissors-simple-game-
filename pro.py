import random
'''
1 for rock
0 for paper
-1 for scissor
'''
computer=random.choice([1,0,-1])
youstr=input("enter your choice(r:rock,p:paper,s:scissor):")
youDict={"r":1,"p":0,"s":-1}
reverseDic={1:"rock",0:"paper",-1:"scissor"}

if youstr not in youDict:
    print("worng input! please enter correct input")
else:
   you=youDict[youstr]
   print(f"you choice: {reverseDic[you]}\ncomputer choice: {reverseDic[computer]}")

   if(computer==you):
      print("---its a draw---")
   else:
     if(computer==-1 and you==0):
        print("---you lose!---")
     elif(computer==-1 and you==1):
        print("---you win!----")
     elif(computer==1 and you==-1):
        print("---you lose---")
     elif(computer==1 and you==0):
        print("---you win---")
     elif(computer==0 and you==1):
        print("---you lose---")
     elif(computer==0 and you==-1):
        print("---you win---")
     
