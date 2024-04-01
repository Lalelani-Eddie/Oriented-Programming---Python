# -*- coding: utf-8 -*-
"""
Created on Sat May 29 09:44:04 2021

@author: LALELANI EDDIE
"""
from vpython import *
##Objects
 
ball = sphere(pos=vector(-5,0,0), radius=0.5, color = color.cyan)
ball.trail = curve(color=ball.color)
wallR = box(pos=vector(6,0,0), size= vector(0.2,12,12), color=color.green)
wallL = box(pos=vector(-6,0,0), size= vector(0.2,12,12), color=color.green)
wallT = box(pos=vector(0,-6,0), size= vector(12,0.2,12), color=color.green)
wallB = box(pos=vector(0,6,0), size= vector(12,0.2,12))
##initial values
ball.velocity = vector(25,5,0)
vscale = 0.1
deltat = 0.005
t = 0

##Calculations
while t < 3:
    varr = arrow(pos=ball.pos)
    rate(10)
    if ball.pos.x > (wallR.pos.x):
        ball.velocity.x = -ball.velocity.x
    ball.pos = ball.pos + ball.velocity*deltat
    varr = arrow(pos=ball.pos)
    ball.trail.append(pos=ball.pos)
    t = t + deltat
