# python class module files with info as output
# ----------------------------------------------------------------
# objective:
# returns the informations of files such as:
# 1) .cvs files
# 2) .txt files
# 3) .xls files

# variables
# flenm = file path name with the file name
# shtcl = worksheet columns to be extracted
# numrw = worksheet rows to be extracted

import pandas as pd

class open_files():

    def __init__(self, flenm, shtnm, shtcl, numrw):
        self.flenm = flenm
        self.shtnm = shtnm
        self.shtcl = shtcl
        self.numrw = numrw
    
    def txtopen(self):
        try:
            with open(self.flenm) as f:
                t = f.readlines()
        except Exception as e:
            print('-' + e + '\n-With file: ' + self.flenm)
        else:
            return t

    def xlsopen(self):
        try:
            with pd.ExcelFile(self.flenm) as f:
                df = pd.read_excel(f,
                                   self.shtnm, 
                                   skiprows=0, 
                                   usecols=self.shtcl, 
                                   nrows=self.numrw)
        except Exception as e:
            print('-' + e + '\n-With file: ' + self.flenm)
        else:
            return df