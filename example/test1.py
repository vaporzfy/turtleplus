import turtleplus as tp
from turtleplus import colors


p = tp.Pen()
s = tp.Screen()

p.pencolor(colors.PINK)
p.forward(100)
p.ellipse(50, 60)
s.bgcolor(colors.GREEN)

p.save('line')

tp.done()
