from utils import *
def app():
    while True:
        try:
            number = int(input("Enter length of the array list: "))
            array = make_array(number)
            print(array)
            array.sort()
            print(array)
            return win_or_lose(array[-1])
        except ValueError:
            print("Invalid input")
    
    
if __name__ == "__main__":
    print(app())
    
    

