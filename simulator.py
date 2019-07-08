from random import randint


d3 = 0
d4 = 0
d5 = 0
d6 = 0
d7 = 0
d8 = 0
d9p = 0

nm = 100000


def roll():
	return randint(1,10);

def count():
	num = 0
	n2 = 0;
	while(num<3):
		n2+=1
		r = roll()
		if r == 10:
			pass
		else:
			num+=1
	return n2

def avg_win_day():
	return (d3*3+d4*4+d5*5+d6*6+d7*7+d8*8+d9p*9)/nm

temp = 0
for i in range(nm):
	temp = count()
	if temp==3:
		d3+=1
	elif temp == 4:
		d4+=1
	elif temp == 5:
		d5+=1
	elif temp == 6:
		d6+=1
	elif temp == 7:
		d7+=1
	elif temp == 8:
		d8+=1
	elif temp >= 9:
		d9p+=1

print("Day 3: {} | {:.2f}%\nDay 4: {} | {:.2f}%\nDay 5: {} | {:.2f}%\nDay 6: {} | {:.2f}%\nDay 7: {} | {:.2f}%\nDay 8: {} | {:.2f}%\nDay 9+ {} | {:.2f}%".format(d3, d3/nm*100,d4, d4/nm*100,d5, d5/nm*100,d6, d6/nm*100,d7, d7/nm*100,d8, d8/nm*100,d9p, d9p/nm*100))
print("Win day average is: {}".format(avg_win_day()))


