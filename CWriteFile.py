# python class module files with info as output
# ----------------------------------------------------------------
# objective:
# write and save files such as:
# 1) .cvs files
# 2) .txt files
# 3) .xls files

# variables
# flenm = file path name with the file name
# shtcl = worksheet columns to be extracted
# numrw = worksheet rows to be extracted

import pandas as pd

class write_files():

    def __init__(self, flenm, datfm, shtnm, numcl, numrw):
        self.flenm = flenm
        self.datfm = datfm
        self.shtnm = shtnm
        self.numcl = numcl
        self.numrw = numrw
    
    def xlswrite(self):
        try:
            with pd.ExcelWriter(self.flenm) as writer:
                self.datfm.to_excel(writer,
                                    sheet_name=self.shtnm,
                                    startrow=self.numcl,
                                    startcol=self.numrw)
        except Exception as e:
            print('-' + e)