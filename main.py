import random



class Reel:
    def __init__ (self, max_value = 9)
    self.max_value = max_value

    def spin(self):
        return random.randint(0,9)


class Slotmachine:
    def _init__(self):
        self.r1 = Reel()
        self.r2 = Reel()
        self.r3 = Reel()
   
    def play_round(self):
        r1 = self.r1.spin()
        r2 = self.r2.spin()
        r3 = self.r3.spin()

        total = r1+r2+r3
        result = evaluate_spin(self,r1,r2,r3)
        return r1, r2, r3,total, result




    def evaluate_spin(self,r1, r2 ,r3)
        if r1 = 0 or r2 = 0 or r3 = 0:
            print("Lose") 
        elif r1 = r2 = r3:
            print("Win")
        else:
            print("spin Agian")

