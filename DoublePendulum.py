from manim import *
from math import sin, cos, pi

class DoublePendulum(Scene):
    def construct(self):
        # pendulum variables
        g = 9.8
        length1, length2 = 1, 1
        mass1, mass2 = 2, 2
        self.theta1, self.theta2 = pi/2, pi/2
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
            a1, a2 = self.calc_accel(g, mass1, mass2, length1, length2)
            self.v1 = (self.v1+a1*dt)#*0.999
            self.v2 = (self.v2+a2*dt)#*0.999
            self.theta1 += self.v1*dt
            self.theta2 += self.v2*dt
            x1, y1, x2, y2 = self.get_position(length1, length2)
            

            # update pendulum position
            l1.put_start_and_end_on([0,0,0], [x1, y1,0])
            p1.move_to([x1,y1,0])
            l2.put_start_and_end_on([x1,y1,0], [x2,y2,0])
            p2.move_to([x2,y2,0])

        # plot pendulum and traced path
        trace = TracedPath(p2.get_center, dissipating_time=1, stroke_opacity=[0, 1])
        originPoint = Dot(point=[0, 0, 0])
        pendulum = VGroup(l1, p1, l2, p2)
        self.add(pendulum, originPoint, trace)
        pendulum.add_updater(pendulum_updater)
        self.wait(10)

    def calc_accel(self, g, mass1, mass2, length1, length2):
        num1=-g*(2*mass1+mass2)*sin(self.theta1)-mass2*g*sin(self.theta1-2*self.theta2)
        num2=-2*sin(self.theta1-self.theta2)*mass2*(self.v2*self.v2*length2+self.v1*self.v1*length1*cos(self.theta1-self.theta2))
        denominator=2*mass1+mass2-mass2*cos(2*self.theta2-2*self.theta1)

        a1=(num1+num2)/(length1*denominator)

        num1=self.v1*self.v1*length1*(mass1+mass2)+g*(mass1+mass2)*cos(self.theta1)
        num2=self.v2*self.v2*length2*mass2*cos(self.theta1-self.theta2)
        
        a2=(2*sin(self.theta1-self.theta2)*(num1+num2))/(length2*denominator)

        return a1, a2
    
    # base x, y coordinates of pendulums
    def get_position(self, length1, length2):
        x1 = length1 * sin(self.theta1)
        y1 = -length1 * cos(self.theta1)
        x2 = x1 + (length2 * sin(self.theta2))
        y2 = y1 - (length2 * cos(self.theta2))

        return x1, y1, x2, y2