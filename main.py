# Kevin Zheng 24792025


import random



class Reel:
    def __init__ (self, max_value = 9):
        self.max_value = max_value

    def spin(self):
        return random.randint(0,self.max_value)

   
   
  
class Slotmachine:
    def __init__(self):
        self.r1 = Reel()
        self.r2 = Reel()
        self.r3 = Reel()
    
    def evaluate_spin(self,r1, r2 ,r3):
        if r1 == 0 or r2 == 0 or r3 == 0:
            return "Lose" 
        elif r1 == r2 == r3:
            return "Win"
        else:
            return "spin Agian"

    def play_round(self):
        r1 = self.r1.spin()
        r2 = self.r2.spin()
        r3 = self.r3.spin()

        total = r1+r2+r3
        result = self.evaluate_spin(r1,r2,r3)
        return r1, r2, r3,total, result
  

def main():
    machine = Slotmachine()

    while True:
        print("1. Play a round")
        print("2. Exit")

        choice = input("Selection:")


        if choice =="1":

            r1,r2,r3,total,result = machine.play_round()
            print(f"Reels: {r1}, {r2}, {r3}")
            print(f"Total: {total}")
            print(f"Results: {result}")

        elif choice == "2":
            print("Exiting...")
            break

        else:
            print("invalid choice.")


main()
