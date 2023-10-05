def blank():
	print()
	print()
blank()

q1 = 5
print("numbers 5 through 50 counting by 3s")
for i in range(16):
	print(q1, end=" ")
	q1+=3
blank()

print("numbers 80 down to 10 counting down by 2s")
q2 = 80
for j in range(36):
	print(q2, end=" ")
	q2-=2
blank()
	
print("numbers 2 to 200 multiplying by 5s (c++ only) BUT IM DOING IT ANYWAY")
q3=2
for k in range(4):
	print(q3, end=" ")
	num4=q3*5
	q3=num4
blank()