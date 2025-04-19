for i in range(1,51):
	if(i%3==0 and i%5==0):
	# % is used for division
		print(str(i)+" = FizzBuzz")
	#str(i)=cnvrt variable into string
	else:
		if (i%3==0):
			print(str(i)+" = Fizz")
		if (i%5==0):
			print(str(i)+" = Buzz")
		else:
			print(str(i))