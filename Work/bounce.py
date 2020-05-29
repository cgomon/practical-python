# bounce.py
#
# Exercise 1.5

def bounce_ball(num_bounces, init_height, elasticity):
    height = init_height
    for i in range(num_bounces):
        print(i+1, round(height, 4))
        height *= elasticity