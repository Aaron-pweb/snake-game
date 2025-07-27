from turtle import Turtle

FONT = ("courier", 20, "bold")
ALIGNMENT = "center"
MOVE = False

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} highest score: {self.high_score}", move=MOVE, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', "w") as file:
                file.write(f'{self.score}')

        self.score = 0
        self.display_score()
    def increase_score(self):
        self.score += 1
        self.display_score()




