from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.linfo = "Player 1 Score : "
        self.rscore = 0
        self.rinfo = "Player 2 Score : "
        self .updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-200, 200)
        self.write(self.linfo, align="center", font=("Times New Roman", 20, "normal"))
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Times New Roman", 20, "normal"))
        self.goto(180, 200)
        self.write(self.rinfo, align="center", font=("Times New Roman", 20, "normal"))
        self.goto(280, 200)
        self.write(self.rscore, align="center", font=("Times New Roman", 20, "normal"))

    def lpoint(self):
        self.lscore += 1
        self.updatescore()

    def rpoint(self):
        self.rscore += 1
        self.updatescore()