class Stats:
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open("highscores.txt", "r") as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        self.ship_life = 3
        self.score = 0
