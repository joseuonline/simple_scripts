"""
Jose Uzcategui
May 4, 2019 (JST)
Classes to help the ParseCSV class inputs
"""

import sys
import os.path

class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass


def fileChecker(filename):
    if not filename:
        print("Nothing entered. Bye!")
        sys.exit()
    elif os.path.isfile(filename) is False:
        print("The file doesn't seem to exist.\n" +\
              "Re-check the file name and try again.")
        sys.exit()


def colInputVal(prompt2, colLen):
    while True:
        colInput = input(prompt2)

        if not colInput:
            print("Nothing was entered. Bye.")
            print()
            raise SystemExit

        cols = colInput.split(",")

        try:
            for i, col in enumerate(cols):
                cols[i] = int(col)
                if cols[i] not in range (0, colLen):
                    raise ValueTooLargeError
                
 #               if col not in range (0,len(header)+1):
 #                   print("Column", col, "is out of range.\n" + \
 #                         "Try again or just hit Enter to exit.")
            return cols
            break
        except ValueTooLargeError:
            print("An entered column index is out of bounds. Try again.")
        except Exception as e:
            print(e)
            print("I need an whole number.", \
                  "Try again or just hit Enter to exit.")
   

         
def sampleSizeValidate():
    while True:
        size = input("Enter desired sample size as percentage of original file: ")

        if not size:
            print("Nothing was entered. Bye.")
            print()
            raise SystemExit

        try:
            size = int(size)
            if size < 1 or size >= 100:
                raise ValueTooLargeError
            else:
                return size
                break
        except ValueTooLargeError:
            print("Sample size needs to be bewteen 1 and 99.")
        except Exception as e:
            print(e)
            print("I need an whole number.", \
                  "Try again or just hit Enter to exit.") 
