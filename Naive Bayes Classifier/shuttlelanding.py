f=open("shuttle-landing-control.txt")
a=f.readline()
attr=[]
length=0
while a:
	attr.append(a[0:-1].split(","))
	a=f.readline()
	length+=1
f.close()
temp=0
correct=0
while temp<length:
	testdata=attr[temp][1:]
	traindata=attr[0:temp]+attr[temp+1:]
	testresult=attr[temp][0]
	noof1=0
	noof2=0
	prob1=1
	prob2=1
	for i in traindata:
		if i[0]=="1":
			noof1+=1
		elif i[0]=="2":
			noof2+=1
	for i in range(len(testdata)):
		attr1=0
		attr2=0
		for j in traindata:
			if testdata[i]=="*" and j[0]=="1":
				attr1+=1
			elif testdata[i]=="*" and j[0]=="2":
				attr2+=1
			elif j[i+1]=="*" and j[0]=="1":
				attr1+=1
			elif j[i+1]=="*" and j[0]=="2":
				attr2+=1
			elif j[i+1]==testdata[i] and j[0]=="1":
				attr1+=1
			elif j[i+1]==testdata[i] and j[0]=="2":
				attr2+=1
		prob1*=(attr1/noof1)
		prob2*=(attr2/noof2)
	prob1*=(noof1/length)
	prob2*=(noof2/length)
	if prob1!=prob2:
		if prob1>prob2 and testresult[0]=="1":
			correct+=1
		elif prob2>prob1 and testresult[0]=="2":
			correct+=1
	temp+=1
print ("Shuttle-landing-control Classification Accuracy : "+str(correct*100/length))


