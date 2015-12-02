from meet import *
import random 
num_cells=0

cells=[]
while num_cells<30:
	balls={'radius':random.randint(0,100) ,'x':random.randint(0,100),'y':random.randint(0,100) ,'dx':.2,'dy':.3}

	cells=[]
	num_cells+=1
	circle1 = create_cell(balls)
	cells.append(circle1)


def borders(cells):
	for cell in cells:
		cell.xcor()
		cell.ycor()		
		sw=get_screen_width()
		sh=get_screen_height()
		x=cell.xcor()
		y=cell.ycor()
		if (x > sw):	
			cell.set_dx(-cell.get_dx())
		if (y > sh):
			cell.set_dy(-cell.get_dy())
	for cell in cells:
		cell.xcor()
		cell.ycor()
		swn=-get_screen_width()
		shn=-get_screen_height()
		xn=cell.xcor()
		yn=cell.ycor()
		if (xn < swn):
			cell.set_dx(-cell.get_dx())
		if (yn < shn):
			cell.set_dy(-cell.get_dx())
				




while(True):
	move_cells(cells)
	borders(cells)
