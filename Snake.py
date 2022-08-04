
from turtle import Turtle

from Constants import SCREEN, WIDTH, HEIGHT, LEFT, RIGHT, UP, DOWN


class Snake():

    def __init__(self) -> None:
        self.body = []
        for _ in range(3):
            self.extend_body()

    def extend_body(self):
        # if only head is in place
        if len(self.body) == 1:
            prev_segment = self.body[-1]
            self.body.append(
                Turtle(shape="square", visible=False))
            self.body[-1].penup()
            if prev_segment.heading() == RIGHT:
                self.body[-1].goto(prev_segment.position()[0] -
                                   20, prev_segment.position()[1])
            elif prev_segment.heading() == LEFT:
                self.body[-1].goto(prev_segment.position()[0] +
                                   20, prev_segment.position()[1])
            elif prev_segment.heading() == UP:
                self.body[-1].goto(prev_segment.position()
                                   [0], prev_segment.position()[1] - 20)
            elif prev_segment.heading() == DOWN:
                self.body[-1].goto(prev_segment.position()
                                   [0], prev_segment.position()[1] + 20)
            self.body[-1].st()
        # makes sure that new segments are added in correct orientation, assuming there are two in place
        elif len(self.body) > 1:
            prev_segment = self.body[-1].position()
            prev_prev_segment = self.body[-2].position()
            self.body.append(
                Turtle(shape="square", visible=False))
            self.body[-1].penup()
            if prev_prev_segment[0] == prev_segment[0]:
                if prev_prev_segment[1]+20 == prev_segment[1]:
                    self.body[-1].goto(prev_segment[0], prev_segment[1]+20)
                else:
                    self.body[-1].goto(prev_segment[0], prev_segment[1]-20)
            else:
                if prev_prev_segment[0] == prev_segment[0]+20:
                    self.body[-1].goto(prev_segment[0]+20, prev_segment[1])
                else:
                    self.body[-1].goto(prev_segment[0]-20, prev_segment[1])
            self.body[-1].st()
        # initializes head
        else:
            self.body.append(Turtle(shape="square"))
            SCREEN.onkeypress(self.T_Right, "d")
            SCREEN.onkeypress(self.T_Left, "a")
            SCREEN.onkeypress(self.T_Up, "w")
            SCREEN.onkeypress(self.T_Down, "s")
        self.body[-1].fillcolor("white")

    def forward(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].goto(self.body[i-1].position()[0],
                              self.body[i-1].position()[1])
        if self.body[0].heading() == RIGHT:
            self.body[0].goto(self.body[0].position()[
                0]+20, self.body[0].position()[1])
        elif self.body[0].heading() == LEFT:
            self.body[0].goto(self.body[0].position()[
                0]-20, self.body[0].position()[1])
        elif self.body[0].heading() == UP:
            self.body[0].goto(self.body[0].position()[
                0], self.body[0].position()[1]+20)
        elif self.body[0].heading() == DOWN:
            self.body[0].goto(self.body[0].position()[
                0], self.body[0].position()[1]-20)

    def T_Right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)

    def T_Left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def T_Up(self):
        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def T_Down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def wall_collision(self) -> bool:
        pos = self.body[0].position()
        if pos[0] > WIDTH//2 or pos[0] < -WIDTH//2 or pos[1] > HEIGHT//2 or pos[1] < -HEIGHT//2:
            return True
        return False

    def tail_collision(self) -> bool:
        for i in range(1, len(self.body)):
            if self.body[i].isvisible() and self.body[0].distance(self.body[i]) < 18:
                self.body[i].color("red")
                return True
        return False
