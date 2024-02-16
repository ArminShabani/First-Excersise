from game import Game

def main():
    number = int(input("Enter length of the array list: "))
    game = Game(number)
    array = game.make_array()
    print(array)
    array.sort()
    print(array)
    return game.win_or_lose(array[-1])

if __name__ == "__main__":
    print(main())