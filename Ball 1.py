from tkinter import *
import random, time

screen = Tk()
screen.title("Game")
screen.resizable(False, False)
screen.wm_attributes("-topmost", 1)
canvas = Canvas(screen, width=1200, height=800, bd=0, highlightthickness=0, bg="gray")
canvas.pack()
screen.update()



class Ball:
    def __init__(self, canvas, color, platform, score, money):
        self.canvas = canvas
        self.money = money
        self.platform = platform
        self.score = score
        start = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.id = canvas.create_oval(50, 50, 25, 25, fill=color)
        self.canvas.move(self.id, 393, 250)
        self.x = random.choice(start)
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_down = False




    def hit_platform(self, position):
        position_platform = self.canvas.coords(self.platform.id)
        if position[2] >= position_platform[0] and position[0] <= position_platform[2]:
            if position_platform[1] <= position[3] <= position_platform[3]:
                self.score.hit()
                self.money.hit()

                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position_ball = self.canvas.coords(self.id)
        if position_ball[1] <= 0:
            self.y = 3
        if position_ball[3] >= self.canvas_height:
            self.hit_down = True
            canvas.create_text(600, 400, text='Game ower!', font=('Courier', 100), fill='red')
        if position_ball[2] >= self.canvas_width:
            self.x = -3
        if position_ball[0] <= 0:
            self.x = 3
        if self.hit_platform(position_ball):
            self.y = -3
        if self.money.score == 20:
            self.money.score = 0




class Platform:
    def __init__(self, canvas, color):
        self.x = 0
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 200, 20, fill=color)
        self.canvas.move(self.id, 500, 600)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)


    def draw(self):

        self.canvas.move(self.id, self.x, 0)
        position_platform = self.canvas.coords(self.id)
        if position_platform[0] <= 0:
            self.x = 0
        if position_platform[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, event):
        self.x = -3

    def turn_right(self, event):
        self.x = 3


class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(1020, 60, text=self.score, font=('Courier', 50), fill=color)


    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)




class Money:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(60, 60, text=self.score, font=('Courier', 50), fill=color)


    def hit(self):
        self.score += random.randint(5, 15)
        self.canvas.itemconfig(self.id, text=self.score)





money = Money(canvas, 'orange')
score = Score(canvas, 'black')
platform = Platform(canvas, "yellow")
ball = Ball(canvas, "green", platform, score, money)
# second_ball = Ball(canvas, "red", platform)
# third_ball = Ball(canvas, "yellow", platform)
# fourth_ball = Ball(canvas, "blue", platform)
# fifth_ball = Ball(canvas, "purple", platform)
while True:
    if not ball.hit_down:
        ball.draw()
        platform.draw()
    else:
        time.sleep(1)
        break
    screen.update_idletasks()
    screen.update()
    time.sleep(0.01)







# third_ball.draw()
# fourth_ball.draw()
# fifth_ball.draw()
# second_ball.draw()
