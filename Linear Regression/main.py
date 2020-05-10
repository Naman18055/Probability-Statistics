# Name - Naman Tyagi
# Roll no - 2018055
# Section - A
# Branch - CSE

import math
import csv


def avg(x): # To find the mean of the variable x
	s=0
	for i in x:
		s+=float(i)
	return s/(len(x))

def sd(x): # To find standard deviation of the variable x
	m=avg(x)
	s=0
	for i in x:
		s=s+((float(i)-m))**2
	return (s/len(x))**0.5

def var(x):
	return (sd(x))**2

def cor(x,y): # To find the corelation coefficient of the two variables x and y.
	sdx=sd(x)
	sdy=sd(y)
	mx=avg(x)
	my=avg(y)
	n=len(x)
	s=0
	for i in range(n):
		s+=((float(x[i])-mx)/sdx)*((float(y[i])-my)/sdy)
	return s/n

def cov(x,y): # To find the covariance of the two variables x and y
	r = cor(x,y)
	vx = sd(x)
	vy = sd(y)
	return r*vx*vy

file = open("found.txt")
line = file.readline()
hindex = [] # h index of whole data
impfactor = [] # impact factor of whole data
while line: # loop to append h index and impact factor to the list
	hindex.append(line[line.find(";")+1:(line.rfind(";"))])
	impfactor.append(line[line.rfind(";")+1:])
	line = file.readline()
n1=math.floor(0.8*len(hindex)) # length of training data
n2=len(hindex)-n1 # length of testing data
datah=[] # h index of training data
datai=[] # impact factor of training data
testdatah=[] # h index of testing data
testdatai=[] # impact factor of testing data
for i in range(n1):
	datah.append(hindex[i])
	datai.append(impfactor[i])
for i in range(n1+1,len(hindex)):
	testdatah.append(hindex[i])
	testdatai.append(impfactor[i])
a=cov(datah,datai)/var(datah) # Calculating value of a
b=avg(datai)-a*(avg(datah)) # Calculating value of b
error=0
for i in range(n2-1): 
	ans = a*float(testdatah[i])+b # Calculated value of impact factor on testing data
	error += (ans - float(testdatai[i]))**2 # square of difference between actual and calculated value
print ("Corelation coefficient between h index and impact factor on whole data is ",cor(hindex,impfactor))
print ("Corelation coefficient between h index and impact factor on 80% is ",cor(datah,datai))
print ("Mean Square Error is ",(error/n2))
temp1=list(range(300))
temp2=list(range(300))
print (testdatai)
for i in temp1:
	temp2[i]=a*temp1[i]+b
file.close()

# Writing to conferencesfinal.csv the values of impact factor 
file2=open("Conferences.txt")
file4=open("Conferencesfinal.csv","w")
writer = csv.writer(file4)
writer.writerow(('Name','H-index','Impact Factor'))
lines=file2.readline()
lines=file2.readline()
h=[] # h index of conferences
name=[] # name of the conference
impactf=[] # impact factor of the conference
while lines:
	index=lines.find(";-;")
	index2=lines.find('"')
	index3=lines.find('"',index2+1)
	name.append(lines[index2+1:index3])
	h.append(lines[index+3:lines.find(";",index+3)])
	lines=file2.readline()
for i in h: # Calculating impact factor
	impactf.append(a*float(i)+b)
for i in range(len(h)):
	writer.writerow((name[i],h[i],str(impactf[i]))) # Writing to the file
file2.close()
