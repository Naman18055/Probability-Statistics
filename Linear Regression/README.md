# MODEL :
1) We are given a file of Journals with H-index and Impact Factor written. The model is trained on 80% of the data using H-index and Impact Factor.
2) Now the model is tested on the remaining 20% of the data. We find the Impact Factor of the journals and hence calculate the Mean Square Error between the calculated Impact Factor and Given Impact Factor.

# HOW IT IS DONE : 
Using the H-index and Impact Factor as two variables, we calculate the values of a and b using correlation coefficient and covariance of the two variables. These values of a and b are then used to calculate impact factors of the remaining 20% data. 

# FILES :
1) main.py - Python file . On running the file , correlation coefficient between impact factor , h index and mean square error will be printed and regression line between h index and impact factor will be plotted. Also , it will create a new csv file with name of the conferences , h index and impact factor in it.
2) Conferences.txt - The text file which consists of name of the conference and h index only.
3) Conferencesfinal.csv - It is the file that will be created on running the python file. It will consists of name of the conference , h index and impact factor in it.
4) found.txt - The text file which consistes of name of journals , their h index and impact factor in it. 

# HOW TO RUN : 
1) Use the terminal to run the file. Make sure the modules csv and numpy are installed on the system.
2) To install numpy, run "pip3 install numpy" on the terminal window and similarly for csv module.
3) To run the file, run "python3 main.py". It will print the Mean Square Error and Plot the regression line for the two variables.
