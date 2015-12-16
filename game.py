import meet
import random 

num_cells=0
colors=["purple",'blue','green','pink']
cells=[]
balls1={'radius':25,'x':0,'y':-220 , 'dx' : 0 , 'dy' : 0, 'color':'yellow'}
circle1 = meet.create_cell(balls1)
cells.append(circle1)
square_size=90

while num_cells<15:
	balls={'radius':random.randint(0
,80) ,'x':random.randint(-200+square_size,200),'y':random.randint(-180
+square_size,180) ,'dx':random.uniform(-1,1),'dy':random.uniform(-1,1),'color':random.choice(colors)}

	num_cells+=1
	circle = meet.create_cell(balls)
	cells.append(circle)


def borders(cells):
	for cell in cells:		
		sw=meet.get_screen_width()
		sh=meet.get_screen_height()
		x=cell.xcor()
		y=cell.ycor()
		if (x > sw):	
			cell.set_dx(-cell.get_dx())
		if (y > sh):
			cell.set_dy(-cell.get_dy())
		if (x < -sw):	
			cell.set_dx(-cell.get_dx())
		if (y < -sh):
			cell.set_dy(-cell.get_dy())
			

while True:
	x,y = meet.get_user_direction(circle1)
	circle1.set_dx(x)
	circle1.set_dy(y)
	borders(cells)	
	meet.move_cells(cells)
	for cell2 in cells:
		if(cell2 != circle1):
			a=circle1.xcor()
			b=circle1.ycor()
			r=circle1.radius
			c=cell2.xcor()
			d=cell2.ycor()
			r2=cell2.get_radius()
			if((a-c)**2 + (b-d)**2)**0.5 <= (r+r2)  :
				if(r>r2):
					cell2.goto(meet.get_random_x(),meet.get_random_y())
					circle1.set_radius(r+0.25*r2)
				else:
					exit()



meet.mainloop()
