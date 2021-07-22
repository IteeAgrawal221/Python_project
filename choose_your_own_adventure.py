name = input('Type your name: ')
print("Welcome", name, "to this adventure!")

answer = input("you are on a dirt road it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == 'left':
    answer = input('you come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across: ').lower()

    if answer == "swim":
        print("You swam across and were eaten by an aligator ")

    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game")

    else:
        print("Not a valid option. You Lose.")


elif answer == 'right':
    answer = input("you come to a bridge, it looks woobly, you want to cross it or head back (cross/back): ").lower()

    if answer == "back":
        print("if you go back you lose. ")

    elif answer == "cross":
        answer = input("you crossed bridge and meet a stranger. Do you talk to them (yes/no)? : ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")

        elif answer == "no":
            print("you ignored the stranger and they are offended and You lose!")

        else:
            print("Not a valid option. You Lose.")
    else:
        print("Not a valid option. You Lose.")


else:
    print("Not a valid option. You Lose.")

print("THANK YOU!")