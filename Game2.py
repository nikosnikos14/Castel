import random
def func0(num):
    if num==1:
        a = "Rock"
    elif num==2:
        a = "Paper"
    else:
        a = "Sissors"
    return a
print("Lets play first to 3")
user_score =0
bot_score =0
while user_score<=3 or bot_score <=3:
    user=input("Rock Paper Sissors, Shoot! ")
    bot= func0(random.randint(1,3))
    if user == "Rock" and bot == "Paper":
        print("Hah you suck")
        bot_score +=1
    if user == "Rock" and bot == "Rock":
        print("ehh")
    if user == "Rock" and bot == "Sissors":
        print("Fuck")
        user_score += 1
    if user == "Paper" and bot == "Paper":
        print("ehh")
    if user == "Paper" and bot == "Rock":
        print("Fuck")
        user_score += 1
    if user == "Paper" and bot == "Sissors":
         print("Hah you suck")
         bot_score += 1
    if user == "Sissors" and bot == "Rock":
        print("Hah you suck")
        bot_score += 1
    if user == "Sissors" and bot == "Paper":
        print("Fuck")
        user_score += 1
    if user == "Sissors" and bot == "Sissors":
        print("Ehh")
    if user_score >= 3 and bot_score < 3:
        print("Meh you got lucky")
        answer=input("Wanna play again?")
        if answer == "yes":
            print("aight lets go")
            user_score = 0
            bot_score = 0
        else:
            print("Alrigt Byeee")
            break
    if user_score <3 and bot_score>= 3:
        print("Hah u got shit on !")
        answer=input("Wanna play again loser?")
        if answer == "Yes":
            print("Aight lets go")
            user_score = 0
            bot_score = 0
        else:
            print("Alright Byeee")
