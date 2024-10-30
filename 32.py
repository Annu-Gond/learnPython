# import random
# def game():
#     print("Game has stared....")
#     score = random.randint(1,50)
#     with open("highscore.txt") as f:
#         if(highscore!=""):
#             highscore = int(highscore)
#         else:
#             highscore = 0 

#     print(f"Your score :{score}")
#     if(score>highscore):
#         with open("highscore.txt","w") as f:
#             f.write(str(score))
#     return score

# game()
import random

def game():
    print("Game has started....")
    score = random.randint(1, 50)
    
    try:
        with open("Highscore.txt", "r") as f:
            highscore = f.read()
            if highscore != "":
                highscore = int(highscore)
            else:
                highscore = 0
    except FileNotFoundError:
        # If Highscore.txt does not exist, set highscore to 0
        highscore = 0

    print(f"Your score: {score}")
    if score > highscore:
        with open("Highscore.txt", "w") as f:
            f.write(str(score))
        print("Congratulations! You set a new high score!")
    else:
        print("Try again to beat the high score.")

    return score

game()
