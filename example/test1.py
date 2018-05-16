import turtleplus as tp
from turtleplus import colors


p = tp.Pen()
s = tp.Screen()

p.color(colors.GRAY)
p.pencolor(colors.PINK)

p.forward(100)
s.bgcolor(colors.GREEN)


p.save('line')

tp.done()