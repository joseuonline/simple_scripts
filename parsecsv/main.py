"""
Jose Uzcategui
May 4, 2019 (JST)
A class that reads a clean CSV and creates a simple random sample based on the orginal file. 
You can export the files to a different CSV.
"""

import statistics
from random import sample
from input_validator import colInputVal, sampleSizeValidate, fileChecker
import os.path



#fileVariable = open(filename)
print("\n")
print(">" * 25, " CS 521 FINAL PROJECT ", "<" * 25)
print("Initializing class ParseCSV...")


class ParseCSV:
    """Container for parsed CSV data"""

    #Class constructor.
    def __init__(self, filename = ""):
        self.filename = filename
        self.parse()

    #Class description.
    def __str__(self):
        return "Data container for file: " + filename

    def parse(self):
        """Function used in the constructor to read the provided
        CSV file and print basic instructions for the user"""

        #Checks if the provided file exists.
        fileChecker(self.filename)

        #Open the file for reading.
        infile = open (self.filename, "r")

        #Read the file.
        lines = infile.readlines()

        #Basic instructions for the user.
        print()
        print("An object containig \'", self.filename,\
              "\' is ready for use.", sep="")
        print("-" * 60)
        print("Methods of Interest:\n" + \
              "headerCols() - Prints the available column headers.\n" + \
              "describeCols() - Shows descriptive stats for selected columns.\n" + \
              "getSample() - Returns a tuple with two elements based on" +self.filename + \
                          "\n\t\tIndex[0] returns a random sample\n" + \
                          "\t\tIndex[1] returns the remaining table\n" + \
                          "\t\tPassing 'p' as an argument will create CSV files."
                          "\n")

    def getInfile(self):
        return open (self.filename, "r")

    def getHeader(self):
        #Read file into rows.
        rows = self.getInfile().readlines()

        #Parse column names.
        return rows[0].split(",")

    def getFirstRow(self):
        #Read file into rows.
        rows = self.getInfile().readlines()

        #Parse first row.
        return rows[1].split(",")

    def headerCols(self):
        #Specificy column names and create an index for easier user selection.
        print("-" * 30)
        print("Available columns for", self.filename, ":")
        print("-" * 30)
        col_indx = 0
        column_legend = []

        #iterate over each column and assing an index.
        for columnName in self.getHeader():
            #print each column and its corresponding index for user to chose.
            print(columnName, "=", col_indx)
            column_legend.append(columnName)
            col_indx += 1
        print("-" * 30)


    def describeCols(self):

        prompt2 = "What columns woudl you like to assess?\n"
        cols = colInputVal(prompt2,len(self.getHeader()))

        #Create empty lists
        row_values = []
        row_numeric = []
        rows = self.getInfile().readlines()

        for c in cols:
            duplicate_count = 0
            empty_values = 0
            values_dic = {}

            if self.getFirstRow()[c].isnumeric() == True:


        # ---- STATS FOR NUMERIC ----
                for row in rows:
                    value = row.split(",")[c]

                    #Count duplicates:
                    if value in row_values:
                        duplicate_count += 1
                    row_values.append(value)


                    #Convert value into float and add to a list for computation.
                    if value.isnumeric() == True:
                        row_numeric.append(float(value))

                    #Check for empty values.
                    elif not value:
                        empty_values += 1


                #Print stats for numeric.
                print("=========")
                print("Column Name:\t", self.getHeader()[c], "(NUMERIC)")
                print("Number of Rows:\t", len(rows)-1)
                print("Empty Values:\t", empty_values)
                print("Duplicates:\t", duplicate_count)
                print("Sum:\t\t", sum(row_numeric))
                print("Max:\t\t", max(row_numeric))
                print("Min:\t\t", min(row_numeric))
                print("Standard Dev:\t", format(statistics.stdev(row_numeric), "0.1f"))
                print("Average:\t", statistics.mean(row_numeric))
                print("Median:\t\t", statistics.median(row_numeric))
                print("=========")

         # ---- END FOR NUMERIC ----


            else:

        # ---- STATS FOR STRING ----
                for row in rows:

                    #Count duplicates:
                    value = row.split(",")[c]
                    if value in values_dic:
                        duplicate_count += 1
                        values_dic[value] +=1
                    else:
                        values_dic[value] = 1

                    #Check for empty values.
                    if not value:
                        empty_values += 1


                #Print stats for string.
                print("=========")
                print("Column Name:\t", self.getHeader()[c], "(STRING)")
                print("Number of Rows:\t", len(rows)-1)
                print("Top value: \t" , max(values_dic, key=values_dic.get))
                print("Empty Values:\t", empty_values)
                print("Duplicates:\t", duplicate_count)
                print("Unique values:\t", len(set(values_dic.keys()))-1)


     # ---- END FOR STRING ----


    def getSample(self, createFile = "n"):
        """Creates a sample table based on the relative size entered by the user
        and provides the option to print to a file."""

        self.__createFile = createFile

        #Prompt user for size of sample
        size = sampleSizeValidate()

        #Read lins from
        rows = self.getInfile().readlines()

        #Create header list to attach to the new table bodies.
        header = [rows[0]]

        #Create new table body without header.
        tableBody = rows+[]
        tableBody.pop(0)

        #Compute argument into an int.
        percent = round(size * len(tableBody) / 100)

        #Use sample module to create a sample table.
        sampleBody = sample(tableBody, percent)
        newBody = [row for row in tableBody if row not in sampleBody]

        #Create sample and remaining files.
        sampleTable = header + sampleBody
        remainTable = header + newBody

        print("\nA tuple with your random sample in index '0' has been created.\n" + \
              "The remaining data is in index '1'")

        #If parameter for prinintng is entered.
        if self.__createFile == "p":


            #Assign a default name for sample file.
            outFileSampleName = "sample_table.csv"
            i = 0

            #Update file name until it doesn't exist.
            while True:
                if os.path.isfile(outFileSampleName) is False:
                    break
                else:
                    i += 1
                    outFileSampleName = "sample_table (" + str(i) + ")" + ".csv"

            print("\nSample file created...")
            print("File name for sample table:", outFileSampleName)

            #Open file for writing
            outfileSample = open(outFileSampleName, "w")

            #Write to file
            for line in sampleTable:
                outfileSample.write(line)

            #Close file
            outfileSample.close()



            #Assign a default name for remaining table file.
            outFileRemainingName = "remaining_table.csv"
            i = 0

            #Update file name until it doesn't exist.
            while True:
                if os.path.isfile(outFileRemainingName) is False:
                    break
                else:
                    i += 1
                    outFileRemainingName = "remaining_table (" + str(i) + ")" + ".csv"

            print("\nSample file created...")
            print("File name for remaining table:", outFileRemainingName)

            #Open file for writing
            outfileRemaining = open(outFileRemainingName, "w")

            #Write to file
            for line in remainTable:
                outfileRemaining.write(line)

            #Close file
            outfileRemaining.close()


        return (sampleTable, remainTable)

print("Ready.")
print("\n")
