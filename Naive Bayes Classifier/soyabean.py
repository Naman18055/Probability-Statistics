f=open("soybean-small.txt")
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
	noofd1,noofd4=0,0
	noofd2,noofd3=0,0
	probd1,probd3=1,1
	probd2,probd4=1,1
	for i in traindata:
		if i[-1][0:-1]=="D1":
			noofd1+=1
		elif i[-1][0:-1]=="D2":
			noofd2+=1
		elif i[-1][0:-1]=="D3":
			noofd3+=1
		elif i[-1][0:-1]=="D4":
			noofd4+=1
	for i in range(len(testdata)):
		attrd1=0
		attrd2=0
		attrd3=0
		attrd4=0
		for j in traindata:
			if j[i]==testdata[i] and j[-1][0:-1]=="D1":
				attrd1+=1
			elif j[i]==testdata[i] and j[-1][0:-1]=="D2":
				attrd2+=1
			elif j[i]==testdata[i] and j[-1][0:-1]=="D3":
				attrd3+=1
			elif j[i]==testdata[i] and j[-1][0:-1]=="D4":
				attrd4+=1
		probd1*=attrd1/noofd1
		probd2*=attrd2/noofd2
		probd3*=attrd3/noofd3
		probd4*=attrd4/noofd4
	probd1*=noofd1/length
	probd2*=noofd2/length
	probd3*=noofd3/length
	probd4*=noofd4/length
	if probd1==probd2 and probd3==probd4:
		correct+=0
	else:
		if max(probd1,probd2,probd3,probd4)==probd1 and testresult[0:-1]=="D1":
			correct+=1
		elif max(probd1,probd2,probd3,probd4)==probd2 and testresult[0:-1]=="D2":
			correct+=1
		elif max(probd1,probd2,probd3,probd4)==probd3 and testresult[0:-1]=="D3":
			correct+=1
		elif max(probd1,probd2,probd3,probd4)==probd4 and testresult[0:-1]=="D4":
			correct+=1
	temp+=1
print ("SOYBEAN Classification Accuracy : "+str(correct*100/length))
