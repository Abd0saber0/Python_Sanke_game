from turtle import Turtle


# Game score board
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.up()
        self.color("white") #defult black
        self.goto(0,250)
        self.hideturtle()
        self.score_update()
    def get_high_score(self):
        with open('data.txt') as file:
            return int(file.read())   # الملف مخزن نصوص
    def update_high_score(self):
        with open('data.txt','w') as file:
            file.write(str(self.high_score)) 
    def score_update(self):
        self.write(f"النقاط: {self.score}   أعلى أسكور {self.high_score}",font=('arial',26,'bold'),align='center')
    def increase_score(self):
        self.clear()
        self.score +=1
        self.score_update()
    def game_over(self):
        # self.getscreen().bgcolor('red')
        self.home() # 0,0
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.write(f"____انتهت اللعبة____ \n\nالنقاط النهائية هي : {self.score}\n أعلى النقاط: {self.high_score}",
                   font=('arial',26,'bold'), 
                   align='center')