import time
import random


def house():
    print("The closer you get the more details you see")
    print("It is just like you imagined the witch's house looked in Hansel and Gretel")
    print("You approach the house fast and then think better and slow down")


def end():
    print("The End")
    quit()


def cave():
    print("You hear water falling")
    print("Going further inside you see beautiful crystals reflecting light from an opening in the ceiling")
    print("You have discovered a hidden wonder")
    print("Exploring the cavern you find a beautiful intact ancient city")
    print("You decide not to tell anyone what you found so that it won't be pilfered by looters")


def the_island():
    print("Excitement makes you giddy and exertion makes you sweat")
    time.sleep(2)
    print("You gaze around in shock and amazement")
    print("To the left you see a cave and to the right a gingerbread house")


def boat():
    print("Being adventurous is over rated.")
    print("But hey, you live to see another day")


def the_window():
    print("You slow your pace and creep quietly up to the window")
    print("You gasp in surprise at what you see")


def the_door():
    print("You decide to knock on the door because you are a track star")
    print("You are more than confident you can outrun anyone")
    print("Confidently you swagger up to the door and knock")
    door_opens = ["Slowly the door opens to reveal an older woman and child",
                  "Slowly the door opens to reveal a haggard old lady",
                  "Slowly the door opens to reveal a group of children"]
    rand_door = random.choice(door_opens)
    print(rand_door)
    print("A little let down by their appearance you stumble back a step")
    print("Thinking you are ill, they invite you in for dinner")


def the_win():
    print("You Win")
    print("You are awesome and rise above your fear")
    repeat()


def the_loss():
    print("You Lose.")
    print("Your fear got the best of you, but there is always next time")


def game_over():
    print("GAME OVER!!")
    repeat()


def run_away():
    print("Quickly you turn and put your running skills to work")
    print("You make it back to the beach and almost miss your boat in your haste to get away")
    print("Finally in the boat you do your best impression of a one person rowing team")
    print("Well you didn't overcome your fear today, but you can try again another day!")


def in_the_boat():
    print("So there you are peacefully floating along in my boat...")
    print("Not a care in the world, when you notice...")
    print("Smoke billowing in the sky above an island")
    time.sleep(3)
    print("The smoke is not surprising, but the island sure is")
    print("That wasn't there yesterday!!")


in_the_boat()


def repeat():
    play = int(input("Would you like to play again? 1 for yes 2 for no: "))
    if play < 1 or play > 2:
        repeat()
    if play == 1:
        in_the_boat()
        stay_or_go()
        house_cave()
    if play == 2:
        print("GAME OVER")
        end()


def stay_or_go():

    go_or_stay = (int(input("Choose 1 to stay on the boat and 2 to be adventurous: ")))
    # This one works
    if go_or_stay < 1 or go_or_stay > 2:
        stay_or_go()
    if go_or_stay == 1:
        print("You didn't go to the island but you lived to see another day.")
        print("You lose.")
        boat()

        play_again = (int(input("Would you like to play again? Choose 1 for yes and 2 for no: ")))
        # this one works
        if play_again < 1 or play_again > 2:
            stay_or_go()
        if play_again == 1:
            in_the_boat()
            stay_or_go()
        elif play_again == 2:
            print("Game Over")
            end()

    elif go_or_stay == 2:
        print("You climb from the boat and pull it out of the water")
        print("Better safe than sorry. You have got to be ready for a quick get away")
        the_island()


stay_or_go()


def house_cave():
    cave_or_house = int(input("Type 1 for the house and 2 for the cave: "))
    # This one works
    if cave_or_house < 1 or cave_or_house > 2:
        house_cave()
    if cave_or_house == 1:
        print("Off you march to the house")
        house()
    elif cave_or_house == 2:
        print("It's a bit scary but YOLO")
        cave()
        the_win()
        game_over()
        repeat()


house_cave()


def window_or_door():
    print("As you draw closer to the house you see it has a large window and a very decorative door")
    door_or_window = int(input("Choose 1 to peek into a window and 2 to knock on the door: "))
    # This one works
    if door_or_window < 1 or door_or_window > 2:
        window_or_door()
    if door_or_window == 1:
        the_window()
        track = int(input("Will you knock on the door or run away? Type 1 for yes and 2 for run: "))
        # This one works
        if track < 1 or track > 2:
            window_or_door()
        if track == 2:
            run_away()
            game_over()
            repeat()
        elif track == 1:
            the_door()
            print("You have a wonderful time and are happy you chose to be friends")
            the_win()
    else:
        print("Go to the door and knock")
        go_in = int(input("Do you knock? Choose 1 for yes and 2 for no: "))
        if go_in < 1 or go_in > 2:
            window_or_door()
        if go_in == 1:
            the_door()
            invite = int(input("Do you accept? Type 1 for yes 2 for no: "))
            if invite == 1:
                print("You graciously accept the invitation and have a wonderful time")
                the_win()
            elif invite == 2:
                print("You shriek in fright")
                run_away()
                the_loss()
                repeat()
        elif go_in == 2:
            run_away()
            the_loss()


window_or_door()
