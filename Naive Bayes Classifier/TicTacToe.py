f=open("tictactoe.txt")
a=f.readline()
attr=[]
length=0
while a:
	attr.append(a.split(","))
	a=f.readline()
	length+=1
f.close()
temp=0
correct=0
while temp<length:
	testdata=attr[temp][0:-1]
	traindata=attr[0:temp]+attr[temp+1:]
	testresult=attr[temp][-1]
	noofpos=0
	noofneg=0
	probpos=1
	probneg=1
	for i in traindata:
		if i[-1][0:-1]=="positive":
			noofpos+=1
		else:
			noofneg+=1
	for i in range(len(testdata)):
		attrp=0
		attrn=0
		for j in traindata:
			if j[i]==testdata[i] and j[-1][0:-1]=="positive":
				attrp+=1
			elif j[i]==testdata[i] and j[-1][0:-1]=="negative":
				attrn+=1
		probpos=probpos*(attrp)/noofpos
		probneg=probneg*(attrn)/noofneg
	probpos=probpos*noofpos/length
	probneg=probneg*noofneg/length
	if probpos>probneg and testresult[0:-1]=="positive":
		correct+=1
	elif probneg>probpos and testresult[0:-1]=="negative":
		correct+=1
	temp+=1
print ("Tic-Tac-Toe Classifiactionn Accuracy : "+str(correct*100/length))
