from manim import *
from math import sin, cos, pi

class DoublePendulum(Scene):
    def construct(self):
        # gravitational acceleration
        g = 9.8
        dotRadius = 0.16

        self.color = BLUE_E

        # create origin point
        originPoint = Dot(point=[0, 0, 0], color=self.color)
        self.add(originPoint)

        # first double pendulum
        # pendulum variables
        length1, length2 = 1, 1
        mass1, mass2 = 2, 2
        self.theta1, self.theta2 = pi/2, pi/4
        print(self.theta1)
        self.v1, self.v2 = 0, 0

        # get pendulum coordinates
        x1, y1, x2, y2 = self.get_position(length1, length2, self.theta1, self.theta2)
        # create double pendulum
        l1, p1, l2, p2 = self.create_double_pendulum(x1, y1, x2, y2, dotRadius)

        # plot pendulum and traced path
        trace = TracedPath(p2.get_center, dissipating_time=1, stroke_opacity=[0, 1])
        pendulum = VGroup(l1, p1, l2, p2)
        self.add(pendulum, trace)

        # pendulum animation
        def pendulum_updater(mobj, dt):
            a1, a2 = self.calc_accel(g, mass1, mass2, length1, length2, self.theta1, self.theta2, self.v1, self.v2)
            self.v1 = (self.v1+a1*dt)#*0.999
            self.v2 = (self.v2+a2*dt)#*0.999
            self.theta1 += self.v1*dt
            self.theta2 += self.v2*dt
            x1, y1, x2, y2 = self.get_position(length1, length2, self.theta1, self.theta2)
            
            # update pendulum position
            l1.put_start_and_end_on([0,0,0], [x1, y1,0])
            p1.move_to([x1,y1,0])
            l2.put_start_and_end_on([x1,y1,0], [x2,y2,0])
            p2.move_to([x2,y2,0])

        pendulum.add_updater(pendulum_updater)


        # second double pendulum
        # pendulum variables
        length3, length4 = 1, 1
        mass3, mass4 = 2, 2
        self.theta3, self.theta4 = pi/2-0.01, pi/4
        self.v3, self.v4 = 0, 0

        # get pendulum coordinates
        x3, y3, x4, y4 = self.get_position(length3, length4, self.theta3, self.theta4)
        # create double pendulum
        l3, p3, l4, p4 = self.create_double_pendulum(x3, y3, x4, y4, dotRadius)

        # plot pendulum and traced path
        trace2 = TracedPath(p4.get_center, dissipating_time=1, stroke_opacity=[0, 1])
        pendulum2 = VGroup(l3, p3, l4, p4)
        self.add(pendulum2, trace2)

        def pendulum_updater2(mobj, dt):
            a1, a2 = self.calc_accel(g, mass3, mass4, length3, length4, self.theta3, self.theta4, self.v3, self.v4)
            self.v3 = (self.v3+a1*dt)#*0.999
            self.v4 = (self.v4+a2*dt)#*0.999
            self.theta3 += self.v3*dt
            self.theta4 += self.v4*dt
            x3, y3, x4, y4 = self.get_position(length3, length4, self.theta3, self.theta4)
            
            # update pendulum position
            l3.put_start_and_end_on([0,0,0], [x3, y3,0])
            p3.move_to([x3,y3,0])
            l4.put_start_and_end_on([x3,y3,0], [x4,y4,0])
            p4.move_to([x4,y4,0])
        
        pendulum2.add_updater(pendulum_updater2)

        self.wait(10)

    def create_double_pendulum(self, x1, y1, x2, y2, dotRadius):
        # pendulum 1
        l1 = Line([0,0,0], [x1,y1,0], color=self.color)
        p1 = Dot(point=[x1, y1, 0], radius=dotRadius, color=self.color)

        # pendulum 2
        l2 = Line([x1,y1,0], [x2, y2,0], color=self.color)
        p2 = Dot(point=[x2, y2, 0], radius=dotRadius, color=self.color)

        return l1, p1, l2, p2

    # calculate acceleration
    def calc_accel(self, g, mass1, mass2, length1, length2, theta1, theta2, v1, v2):
        num1=-g*(2*mass1+mass2)*sin(theta1)-mass2*g*sin(theta1-2*theta2)
        num2=-2*sin(theta1-theta2)*mass2*(v2*v2*length2+v1*v1*length1*cos(theta1-theta2))
        denominator=2*mass1+mass2-mass2*cos(2*theta2-2*theta1)

        a1=(num1+num2)/(length1*denominator)

        num1=v1*v1*length1*(mass1+mass2)+g*(mass1+mass2)*cos(theta1)
        num2=v2*v2*length2*mass2*cos(theta1-theta2)
        
        a2=(2*sin(theta1-theta2)*(num1+num2))/(length2*denominator)

        return a1, a2
    
    # base x, y coordinates of pendulums
    def get_position(self, length1, length2, theta1, theta2):
        x1 = length1 * sin(theta1)
        y1 = -length1 * cos(theta1)
        x2 = x1 + (length2 * sin(theta2))
        y2 = y1 - (length2 * cos(theta2))

        return x1, y1, x2, y2