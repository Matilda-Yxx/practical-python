# bounce.py
#
# Exercise 1.5

init_height = 100
bounce_ratio = 3/5
height = init_height
i = 1

while i < 11:
    height = height * bounce_ratio
    print(i, round(height,4))
    i = i + 1