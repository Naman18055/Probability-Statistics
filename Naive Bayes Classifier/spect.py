f=open("SPECTtrain.txt")
a=f.readline()
attr=[]
length1=0
while a:
	attr.append(a[0:-1].split(","))
	a=f.readline()
	length1+=1
f.close()
f=open("SPECT.txt")
a=f.readline()
testdata=[]
testresult=[]
length2=0
while a:
	testdata.append(a[0:-1].split(",")[1:])
	testresult.append(a[0:-1].split(",")[0])
	a=f.readline()
	length2+=1
f.close()
noof1=0
noof0=0
for i in range(len(attr)):
	if attr[i][0]=="1":
		noof1+=1
	else:
		noof0+=1
temp=0
correct=0
while temp<len(testdata):
	prob1=1
	prob0=1
	for i in range(len(testdata[temp])):
		attr1=0
		attr0=0
		for j in attr:
			if j[i+1]==testdata[temp][i] and j[0]=="1":
				attr1+=1
			elif j[i+1]==testdata[temp][i] and j[0]=="0":
				attr0+=1
		prob1*=(attr1/noof1)
		prob0*=(attr0/noof0)
	prob1*=(noof1/length1)
	prob0*=(noof0/length1)
	if (prob1>prob0 and testresult[temp][0]=="1"):
		correct+=1
	elif (prob0>prob1 and testresult[temp][0]=="0"):
		correct+=1
	temp+=1
print ("SPECT Classification Accuracy : "+str(correct*100/length2))





