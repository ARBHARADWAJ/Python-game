import random 

o=["spiderman","avengers","captainamerica","ironman","thor","hulk","hockeye","blackpanther"]
tel=["alavikuntapuramulo","bahubali","rrr","shayamshingharoa","radhasayam","bheemlanayak"]
pas=o+tel
os=random.choice(pas)
#print(os)



def fun(s,i,os):
    lis=list(s)
    lis2=list(os)
    for j in range(len(lis)):
        if lis2[j]==i:
            lis[j]=i
    s="".join(lis)
    return s
        
def random_questioon_from():
    return "*"*len(os)

            

s=random_questioon_from()
print("\n"*2,s,"\n"*2)
#print(s)
if os in o:
    print("It is a famous hollywood movie")
if os in tel:
    print("It is the famous movie in tollywood ,it got famous recently")
    


ss=True
chance=9
#print(s)
score=0
print("You have 5 chances to guess the movie name:)")
while ss and (chance>0): 
    if  chance==1 and ("*" in s):   
        d=int(input("If you wnated to completed the movie name in single attempt ,type 1 .else type 0 "))
        if d==1 :
                name=input("Enter the movie name : ")
                if name==os:
                    print("You won the game with in ",chance,"chances")
                    ss=False
                else:
                    print("your chances are getting down ",chance) 
    else:            
        if "*" in s:
            i=input("Enter the character  of the maovie: ")
            if i in os and i not in s:
                s=fun(s,i,os)
                print(s)
                score+=1
                
            else:
                print("Try again")
                chance-=1
                print("your chances are getting down ",chance)
                
        else:
            print("Hurry , well done")
            ss=False
         
 