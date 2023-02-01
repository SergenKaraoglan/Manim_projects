from manim import *
from math import sin, cos

class DoublePendulum(Scene):
    def construct(self):
        # pendulum variables
        g = 9.81
        length1, length2 = 1, 1
        mass1, mass2 = 1, 1
        theta1, theta2 = 100, 0
        dotRadius = 0.16
        v1, v2 = 0, 0
        a1, a2 = 0, 0

        # positions
        x1 = length1 * sin(theta1)
        y1 = -length1 * cos(theta1)
        x2 = x1 + (length2 * sin(theta2))
        y2 = y1 - (length2 * cos(theta2))

        originPoint = Dot(point=[0, 0.08, 0])
        # pendulum 1
        self.l1 = Line([0,0,0], [0,-length1,0])
        self.p1 = Dot(point=[0., -length1 - dotRadius, 0.],radius=dotRadius)
        

        # pendulum 2
        self.l2 = Line([0,-length1 - (dotRadius*2),0], [0,-(length1+length2) - (dotRadius*2),0])
        self.p2 = Dot(point=[0,-(length1 + length2) - (dotRadius*3),0], radius=dotRadius)

        # pendulum animation
        def pendulum_updater(mobj, dt):
            self.l1.put_start_and_end_on([0,0,0], [1,1,1])
            self.p1.move_to([0,0,0])
            self.l2.put_start_and_end_on([0,0,0], [1,1,1])
            self.p2.move_to([0,0,0])
            print('x')

        pendulum = VGroup(self.l1, self.p1, self.l2, self.p2)
        self.add(pendulum)
        pendulum.add_updater(pendulum_updater)
        self.wait(3)

        self.calc(g, length1, length2, mass1, mass2, theta1, theta2, v1, v2)


    def calc(g, length1, length2, mass1, mass2, theta1, theta2, v1, v2):
        numerator = -g(2*mass1 + mass2) * sin(theta1) - mass2 * g * sin(theta1 - 2 * theta2)
        - 2 * sin(theta1 - theta2) * mass2 * (v2**2 * length2 + v1**2 * length1 * cos(theta1-theta2))
        denominator = length1 * (2 * mass1 + mass2 - mass2 * cos(2 * theta1 - 2 * theta2))
        theta_pp1 = numerator / denominator

        numerator = 2 * sin(theta1 - theta2) * (v1**2 * length1 * (mass1 + mass2) + g * (mass1 + mass2) 
        * cos(theta1) + theta2**2 * length2 * mass2 * cos(theta1 - theta2))
        denominator = length2 * (2 * mass1 + mass2 - mass2 * cos(2 * theta1 - 2 * theta2))
        theta_pp2 = numerator/ denominator

        return theta_pp1, theta_pp2



