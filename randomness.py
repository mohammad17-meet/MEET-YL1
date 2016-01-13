import random
if (input("please enter n") == "n"):
	x=int(input("enter probability of H"))
	if (random.randint(1,100) <= x):
		print("H")		
	else:
		print ("T")
		
		

	
