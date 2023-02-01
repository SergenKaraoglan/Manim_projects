from manim import *
from math import sin, cos, pi

class DoublePendulum(Scene):
    def construct(self):
        # pendulum variables
        g = 5
        length1, length2 = 1, 1
        mass1, mass2 = 1, 1
        self.theta1, self.theta2 = pi/2, 0
        self.v1, self.v2 = 0, 0

        dotRadius = 0.16

        # positions
        x1, y1, x2, y2 = self.get_position(length1, length2,)

        # pendulum 1
        l1 = Line([0,0,0], [x1,y1,0])
        p1 = Dot(point=[x1, y1, 0], radius=dotRadius)

        # pendulum 2
        l2 = Line([x1,y1,0], [x2, y2,0])
        p2 = Dot(point=[x2, y2, 0], radius=dotRadius)

        # pendulum animation
        def pendulum_updater(mobj, dt):
            a1, a2 = self.calc(g, length1, length2, mass1, mass2)
            #print(a1, a2)
            self.v1 += a1
            self.v2 += a2
            print(self.v1, self.v2)
            self.theta1 += self.v1
            self.theta2 += self.v2
            print(self.theta1)
            x1, y1, x2, y2 = self.get_position(length1, length2)
            l1.put_start_and_end_on([0,0,0], [x1, y1,0])
            p1.move_to([x1,y1,0])
            l2.put_start_and_end_on([x1,y1,0], [x2,y2,0])
            p2.move_to([x2,y2,0])

        originPoint = Dot(point=[0, 0, 0])
        pendulum = VGroup(l1, p1, l2, p2)
        self.add(pendulum, originPoint)
        pendulum.add_updater(pendulum_updater)
        self.wait(5)


    def calc(self, g, length1, length2, mass1, mass2):
        numerator1 = -g * (2*mass1 + mass2) * sin(self.theta1) - mass2 * g * sin(self.theta1 - 2 * self.theta2)
        - 2 * sin(self.theta1 - self.theta2)
        numerator2 = numerator1 * mass2 * (self.v2**2 * length2 + self.v1**2 * length1 * cos(self.theta1-self.theta2))
        denominator = length1 * (2 * mass1 + mass2 - mass2 * cos(2 * self.theta1 - 2 * self.theta2))
        theta_pp1 = numerator2 / denominator

        numerator = 2 * sin(self.theta1 - self.theta2) * (self.v1**2 * length1 * (mass1 + mass2) + g * (mass1 + mass2) 
        * cos(self.theta1) + self.v2**2 * length2 * mass2 * cos(self.theta1 - self.theta2))
        denominator = length2 * (2 * mass1 + mass2 - mass2 * cos(2 * self.theta1 - 2 * self.theta2))
        theta_pp2 = numerator/ denominator

        return theta_pp1, theta_pp2


    def get_position(self, length1, length2):
        x1 = length1 * sin(self.theta1)
        y1 = -length1 * cos(self.theta1)
        x2 = x1 + (length2 * sin(self.theta2))
        y2 = y1 - (length2 * cos(self.theta2))

        return x1, y1, x2, y2