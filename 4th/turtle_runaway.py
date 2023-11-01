# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import tkinter as tk
import turtle, random, time

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=50):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2
        self.start_time = None

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()

        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()

        self.screen = turtle.Screen()

        # Instantiate an another turtle for drawing
        self.drawer = turtle.RawTurtle(self.screen)
        self.drawer.hideturtle()
        self.drawer.penup()

        self.result_displayed = False

    def is_catched(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, init_dist=400, ai_timer_msec=100):
        self.runner.setpos((-init_dist / 2, -init_dist / 2))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, +init_dist / 2))
        self.chaser.setheading(180)

        # TODO) You can do something here and follows.
        self.ai_timer_msec = ai_timer_msec
        self.start_time = time.time()
        self.update_timer()
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def update_timer(self):
        if self.start_time is not None:
            elapsed_time = int(time.time() - self.start_time)
            self.drawer.clear()
            self.drawer.penup()
            self.drawer.setpos(-300, 300)
            self.drawer.write(f'경과 시간: {elapsed_time} 초', align='left', font=('Arial', 12, 'normal'))
            self.canvas.ontimer(self.update_timer, 100)

        if self.is_catched() and not self.result_displayed:
            end_time = round(time.time() - self.start_time, 1)
            self.drawer.clear()
            self.drawer.penup()
            self.drawer.setpos(0, 0)
            if end_time < 5:
                self.drawer.write(f'Excellent!!', align='center', font=('Arial', 20, 'bold'))
                self.quit()
            elif end_time < 15:
                self.drawer.write(f'Good!', align='center', font=('Arial', 20, 'bold'))
                self.quit()
            elif end_time < 20:
                self.drawer.write(f'Not Bad', align='center', font=('Arial', 20, 'bold'))
                self.quit()
            elif end_time < 30:
                self.drawer.write(f'Bad', align='center', font=('Arial', 20, 'bold'))
                self.quit()
            else:
                self.drawer.write(f'Have you ever played other game before?', align='center', font=('Arial', 20, 'bold'))
                self.quit()
            self.result_displayed = end_time
            self.show_result(end_time)

    def step(self):
        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())

        # TODO) You can do something here and follows.
        is_catched = self.is_catched()
        
        # Note) The following line should be the last of this function to keep the game playing
        self.canvas.ontimer(self.step, self.ai_timer_msec)

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass

class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=15, step_turn=15):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn
        self.canvas_width = canvas.window_width() // 2
        self.canvas_height = canvas.window_height() // 2

    def run_ai(self, opp_pos, opp_heading):
        mode = random.randint(0, 2)
        if mode == 0:
            # Calculate the new position
            new_x, new_y = self.xcor() + self.step_move, self.ycor() + self.step_move

            # Check if the runner is out of bounds
            if new_x < self.canvas_width and new_x > -self.canvas_width and new_y < self.canvas_height and new_y > -self.canvas_height:
                self.forward(self.step_move)
            else:
                self.setx(0)
                self.sety(0)
        elif mode == 1:
            self.left(self.step_turn)
        elif mode == 2:
            self.right(self.step_turn)

if __name__ == '__main__':
    # Use 'TurtleScreen' instead of 'Screen' to prevent an exception from the singleton 'Screen'
    root = tk.Tk()
    screen = turtle.Screen()
    canvas = screen.getcanvas()
    canvas.config(width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    # TODO) Change the follows to your turtle if necessary
    runner = RandomMover(screen)
    chaser = ManualMover(screen)

    game = RunawayGame(screen, runner, chaser)
    game.start()
    root.mainloop()