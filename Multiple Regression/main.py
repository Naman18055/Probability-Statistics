# NAME - NAMAN TYAGI
# ROLL NO - 2018055
# SECTION - A
# BRANCH - CSE

import csv
import numpy

data=[]
combos=[]
with open('journal.csv') as journal:
	impfactor = []
	text=csv.reader(journal,delimiter=";") # Dividing the text file into columns between ";"
	j=0
	x=0
	for row in text: # For every row in the original journal file
		file=open("found.txt")
		line=file.readline()
		while line:	
			name=line[0:line.find(";")]		
			if row[2].find(",")==-1:
				if row[2].find(": ")==-1:
					namecsv=row[2]
				else:
					namecsv=row[2].replace(": ","-")
			else:
				namecsv=row[2].replace(",","")
				if row[2].find(": ")==-1:
					namecsv=namecsv
				else:
					namecsv=namecsv.replace(": ","-")
			if namecsv==name: # Matching names in found.txt with names in csv file.
				impfactor.append(line[line.rfind(";")+1:]) # Impactfactor from found.txt.
				data.append([]) # Nested list to store all the data
				sjr=row[5]
				if "," in row[5]:
					sjr=sjr.replace(",","")
					sjr=int(sjr)/1000
				elif ""==sjr:
					sjr=0
				else:
					sjr=int(sjr)/1000
				hindex=int(row[7])
				td2017=int(row[8])
				tdl3=int(row[9])
				tr=int(row[10])
				tc=int(row[11])
				cd=int(row[12])
				cpd=int(row[13].replace(",",""))/100
				rpd=int(row[14].replace(",",""))/100
				data[j].append(sjr)
				data[j].append(hindex)
				data[j].append(td2017)
				data[j].append(tdl3)
				data[j].append(tr)
				data[j].append(tc)
				data[j].append(cd)
				data[j].append(cpd)
				data[j].append(rpd)
				j+=1
				break
			else:
				line=file.readline()
		file.close()
file.close()
n=int(0.8*j) # For 80% data
minerror=100
minerror1=100
# For all combinations , we run loop till 511 and if 1 is present in the binary, it will represent if the variable has been taken or not
file = open("Combos.csv","w")
write = csv.writer(file)
write.writerow(["Combos Taken","Mean Square Error","Absolute Error"])
for i in range(1,512):
	matrixx=[[1] for q in range(n)] # Matrix X of 80%
	testdata=[[1] for q in range(j-n)] # Matrix X of 20%
	matrixy=[[0] for q in range(n)] # Matrix Y of 80%
	testdatay=[[0] for q in range(j-n)] # Original Matrix Y of 20%
	ans=[[0] for q in range(j-n)] # Calculated Matrix Y of 20%
	# To fill Matrix X and Matrix Y
	for k in range(n): 
		new_row=[""]
		if (int(i) & 256)==256: # For SJR
			matrixx[k].append(data[k][0])
			new_row[-1]+="SJR, "
		if (int(i) & 128)==128: # For h index
			matrixx[k].append(data[k][1])
			new_row[-1]+="H-Index, "
		if (int(i) & 64)==64:
			matrixx[k].append(data[k][2])
			new_row[-1]+="Total Docs(2017), "
		if (int(i) & 32)==32:
			matrixx[k].append(data[k][3])
			new_row[-1]+="Total Docs(3 Years), "
		if (int(i) & 16)==16:
			matrixx[k].append(data[k][4])
			new_row[-1]+="Total Refs, "
		if (int(i) & 8)==8:
			matrixx[k].append(data[k][5])
			new_row[-1]+="Total Cites(3 Years), "
		if (int(i) & 4)==4:
			matrixx[k].append(data[k][6])
			new_row[-1]+="Citable Docs(3 Years), "
		if (int(i) & 2)==2:
			matrixx[k].append(data[k][7])
			new_row[-1]+="Cites/Doc(2 Years), "
		if (int(i) & 1)==1:
			matrixx[k].append(data[k][8])
			new_row[-1]+="Ref/Doc, "
		new_row[-1]=new_row[-1][0:-2]
		matrixy[k][0]=float(impfactor[k][0:-2])
	# To fill Matrix X and Y of 20%
	for k in range(n,j):
		if (int(i) & 256)==256:
			testdata[k-n].append(data[k][0])
		if (int(i) & 128)==128:
			testdata[k-n].append(data[k][1])
		if (int(i) & 64)==64:
			testdata[k-n].append(data[k][2])
		if (int(i) & 32)==32:
			testdata[k-n].append(data[k][3])
		if (int(i) & 16)==16:
			testdata[k-n].append(data[k][4])
		if (int(i) & 8)==8:
			testdata[k-n].append(data[k][5])
		if (int(i) & 4)==4:
			testdata[k-n].append(data[k][6])
		if (int(i) & 2)==2:
			testdata[k-n].append(data[k][7])
		if (int(i) & 1)==1:
			testdata[k-n].append(data[k][8])
		testdatay[k-n][0]=float(impfactor[k][0:-2])
	# Coedfficient matrix B = ((X'X)-1)X'Y
	matrixxt=numpy.array(matrixx).T.tolist()
	temp=(numpy.matmul(matrixxt,matrixx)).tolist()
	temp=numpy.linalg.inv(temp).tolist()
	temp=numpy.matmul(temp,matrixxt).tolist()
	coefficients=numpy.matmul(temp,matrixy).tolist()
	abcd=0
	# To fill Calculated Matrix Y
	for k in range(n,j):
		for q in range(len(coefficients)):
			abcd+=(testdata[k-n][q]*coefficients[q][0]) 
		ans[k-n][0]=abcd
		abcd=0
	error=0
	abserror=0
	for k in range(j-n):
		error+=(testdatay[k][0]-ans[k][0])**2
		abserror+=abs(testdatay[k][0]-ans[k][0])
	new_row.append(error/(j-n))
	new_row.append(abserror/(j-n))
	if minerror>(error/(j-n)):
		minerror=error/(j-n)
		mincombo1=(i)
	if minerror1>(abserror/(j-n)):
		minerror1=abserror/(j-n)
		mincombo2=(i)
	write.writerow(new_row)
s1=""
s2=""
if int(mincombo1)&256==256:
	s1+="SJR, "
if int(mincombo1)&128==128:
	s1+="H-Index, "
if int(mincombo1)&64==64:
	s1+="Total Docs(2017), "
if int(mincombo1)&32==32:
	s1+="Total Docs(3years), "
if int(mincombo1)&16==16:
	s1+="Total Refs, "
if int(mincombo1)&8==8:
	s1+="Total Cites, "
if int(mincombo1)&4==4:
	s1+="Citable Docs, "
if int(mincombo1)&2==2:
	s1+="Cites/Doc, "
if int(mincombo1)&1==1:
	s1+="Ref/Doc, "
if int(mincombo2)&256==256:
	s2+="SJR, "
if int(mincombo2)&128==128:
	s2+="H-Index, "
if int(mincombo2)&64==64:
	s2+="Total Docs(2017), "
if int(mincombo2)&32==32:
	s2+="Total Docs(3years), "
if int(mincombo2)&16==16:
	s2+="Total Refs, "
if int(mincombo2)&8==8:
	s2+="Total Cites, "
if int(mincombo2)&4==4:
	s2+="Citable Docs, "
if int(mincombo2)&2==2:
	s2+="Cites/Doc, "
if int(mincombo2)&1==1:
	s2+="Ref/Doc, "
print ("Minimum mean square error is "+str(minerror)+" for "+s1[0:-2])
print ("Minimum absolute error is "+str(minerror1)+" for "+s2[0:-2])
	
