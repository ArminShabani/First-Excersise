import numpy
class Game:
    def __init__(self,number):
        self.number = number
    
    def make_array(self):
        return numpy.random.randint(0, 100, self.number)

    def win_or_lose(self, number):
        if number > 70:
            return "Win"
        else:
            return "Fail"