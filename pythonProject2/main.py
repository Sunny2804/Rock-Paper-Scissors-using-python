import random
options=("rock","paper","scissors")
player=None
playing = True
while playing:
    computer = random.choice(options)
    player = input("chose an option(rock,paper,scissors)")
    while player not in options:
             player=input("chose an option(rock,paper,scissors)")

    print("your choise",player)
    print("computer's chose",computer)

    if player==computer:
        print("TIE!")
    elif player=="rock" and computer=="paper":
        print("you LOOSE!")
    elif player=="scissors" and computer=="rock":
        print("you LOOSE!")
    elif player=="paper" and computer=="scissors":
        print("you LOOSE!")
    else:
        print("YOU WIN!!!!")
    play_again=input("wanna play again(y/n)").lower()
    if not play_again=="y":
        playing=False
print("^_^thanks for playing^_^")

