import numpy as np
import random

class DataEngine:

    def __init__(self):
        print "Initializing the Data Engine Object . . ."

        # Linear Refression Parameters:
        self.SizeOfRawData = 0;
        self.TotalNumberofFeatures = 0;
        self.FeatureSize = 0;
        self.YSet = [];
        self.TrainingSet = [];
        self.LRWeights = [];


    # This method takes in the raw data, in the format of dataframes and some config data to set up the Linear Regression parameters.
    # input_RawData -> Is the raw data in the form of data frames
    # input_Features -> An array containing indecies from the raw that which should be used as the features
    # input_Y -> The index, containing the y for the Linear Regression
    # input_SizeOfPracticeSet -> Defines what fraction of the input should be used for practice
    def DataMassage(self,input_RawData,input_Features,input_Y,input_SizeOfPracticeSet):
        self.SizeOfRawData = len(input_RawData);
        self.TotalNumberofFeatures = len(input_RawData.values[0]);
        # The +1 is added to account for the intercept feature which is always 1
        self.FeatureSize = len(input_Features)+1;

        if (input_SizeOfPracticeSet > self.SizeOfRawData):
            print "The size of the training set is bigger than the data size!"
            exit(1);
        if (input_Y > self.TotalNumberofFeatures):
            print "The Y can not be chosen from the set!"
            exit(1);

        RandomArrayOfIndecies = range(self.SizeOfRawData);
        random.shuffle(RandomArrayOfIndecies);
        RandomArrayOfIndecies = RandomArrayOfIndecies[0:input_SizeOfPracticeSet+1];

        for i in RandomArrayOfIndecies:
            self.YSet.append(input_RawData.values[i][input_Y]);
            TempArray = [];
            # The first feature is always 1, to account for the intercept point, w_0 weight
            TempArray.append(1);
            for j in input_Features:
                TempArray.append(input_RawData.values[i][j]);
            self.TrainingSet.append(TempArray);


    # This method initializes the Linear Regression weights
    # Int_Type defines how the initialization should be done
    # It supports ['random','zeros','read']
    # If read is selected, then it will expect a file path to read the weights
    def Initialize_LRWeights(self,Int_Type,input_File=""):
        print "Initializing the Linear Regression weights using: "+ Int_Type +" weights . . ."
        if(self.FeatureSize == 0):
            print "You have to first initialize the data sets using the DataMassage method."
            exit(1);
        else:
            self.LRWeights = [];
            if(Int_Type == 'random'):
                for i in range(0 , self.FeatureSize):
                    self.LRWeights.append(random.uniform(-1,1));

            elif(Int_Type == 'zeros'):
                for i in range(0 , self.FeatureSize):
                    self.LRWeights.append(0);

            else:
                for i in range(0 , self.FeatureSize):
                    self.LRWeights.append(random.uniform(-1,1));









    # File End
