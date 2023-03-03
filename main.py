from art import logo, vs
import random
from game_data import data



def playagain():
    again = input("Wanna play again? Y N: ").lower()
    if again == "y":
        return False
    elif again == "n":
        return True
    else:
        print("i did not understand could you please type it again?")
def choose():
    while True:
        choice = input("a or b: ")
        if choice == "a":
            return True
        elif choice == "b":
            return False
        else:
            print("i did not understand could you please say it again?")


def randomchoose(first=-1):
    while True:
        number = random.randint(0, 49)
        if number == first:
            continue
        else:
            return number


def main():
    print(logo)
    score = 0
    gameover = False
    while not gameover:
        if score == 0:
            first = randomchoose()
        second = randomchoose(first=first)
        print(f"Compare A: {data[first]['name']}, {data[first]['description']}, {data[first]['country']}")
        print(vs)
        print(f"Compare A: {data[second]['name']}, {data[second]['description']}, {data[second]['country']}")
        choice = choose()
        if choice:
            if data[first]['follower_count'] > data[second]['follower_count']:
                score += 1
                first = second
            else:
                gameover = True

        else:
            if data[second]['follower_count'] > data[first]['follower_count']:
                score += 1
                first = second
            else:
                gameover = True
    print(f"Sorry that's wrong. Your score: {score}")


if __name__ == '__main__':
    stop = False
    while not stop:
        main()
        stop = playagain()
