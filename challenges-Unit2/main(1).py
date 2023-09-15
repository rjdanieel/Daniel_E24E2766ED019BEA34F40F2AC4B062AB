class Player:
    def play(self):
        print("The player is playing cricket")

class Batsman(Player):
    def play(self):
        print("The batsman is batting")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling")

# Create instances of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call their play methods
batsman.play()
bowler.play()