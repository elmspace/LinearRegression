# Imported classes:
import pandas as pd

#===============================================================================
class IO:

    # This method reads in a cvs file and return a dataframe object using pandas
    def DataIO_CSV(self,input_FilePath):
        try:
            return pd.read_csv(input_FilePath, sep=',');
        except Exception as e:
            print "Error while reading the csv file!"
            exit(1);
