var = str(input("Hi what's your name?"))
print("Hi {}!".format(var))

var2 = int(input("How old are you?")

try:
	if var2 > 30:
		return("you should get a job")
	else:
		return("you should finish your study")
except ValueError:
	print("This is not a number")
	break
else:
	return("Hi {}, so your age is {}. Confirm?"(var, var2))


