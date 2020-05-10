# MODEL :
1) We are given Journals with 9 features. We train our model on 80% of the whole data for each combination of the features.
2) Now we calculate the values of the impact factor for the remaining 20% of the data for that combination of the features and hence calculate the value of the mean square error and absolute error.
3) The combination for which our model gives the least absolute error is reported.

# HOW IT IS DONE :
For a particular set of features, we calculate the matrix a and matrix b using matrix multiplication and inverse functions of the numpy module and using these matrices, we calculate the value of impact factor and compare with the given value by calculating the mean square error. It is then calculated for all possible sets of combination and minimum absolute error is reported.

# FILES :
1) main.py - Main Source of Code. On running the code, the code will print minimum mean square error and minimum mean absolute error possible for any combination.
2) found.txt - It contains the name of the journal along with the h index and impact factor. Total Data - 621
3) journal.csv - It conatins all the data of all the journals.
4) Combos.csv - It contains the mean square error and absolute error for each and every possible combination of features.

# HOW TO RUN :
1) Use the terminal to run the file. Make sure the modules csv and numpy are installed on the system.
2) To install numpy, run "pip3 install numpy" on the terminal window and similarly for csv module.
3) To run the file, run "python3 main.py". It will print the Combination of features and the minimum mean square error and minimum absolute error. It also writes the file Combos.csv.
