from manim import *
from math import sin, cos

class DoublePendulum(Scene):
    def construct(self):
        # pendulum variables
        g = 9.81
        length1, length2 = 1, 1
        mass1, mass2 = 1, 1
        theta1, theta2 = 0, 0
        dotRadius = 0.16
        v1, v2 = 0, 0

        # positions
        x1 = length1 * sin(theta1)
        y1 = -length1 * cos(theta1)
        x2 = x1 + (length2 * sin(theta2))
        y2 = y1 - (length2 * cos(theta2))

        originPoint = Dot(point=[0, 0.08, 0])
        # visualise pendulum 1
        l1 = Line([0,0,0], [0,-length1,0])
        m1 = Dot(point=[0., -length1 - dotRadius, 0.],radius=dotRadius)
        pendulum1 = VGroup(l1, m1)
        self.add(originPoint, pendulum1)

        print(l1.get_angel())

        # visualise pendulum 2
        l2 = Line([0,-length1 - (dotRadius*2),0], [0,-(length1+length2) - (dotRadius*2),0])
        m2 = Dot(point=[0,-(length1 + length2) - (dotRadius*3),0], radius=dotRadius)
        pendulum2 = VGroup(l2, m2)
        self.add(pendulum2)

        pendulum1.add_updater(self.pendulum_updater)




    def pendulum_updater(self, mobj, dt):
        .put_start_and_end_on()


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



