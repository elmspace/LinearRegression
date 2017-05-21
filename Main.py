import matplotlib.pyplot as plt
import numpy as np
from IO import IO
from DataEngine import DataEngine
from LinearRegression import LinearRegression

# Get the Raw data from csv file
RawDataObject = IO();
RawData = RawDataObject.DataIO_CSV("./Data/MLB2008.csv");

# Send the data for formatting
DataMassageObject = DataEngine();
DataMassageObject.DataMassage(RawData,[5],12,50);
DataMassageObject.Initialize_LRWeights('zeros');

LinearRegressionObject = LinearRegression(DataMassageObject.TrainingSet,DataMassageObject.YSet,DataMassageObject.LRWeights,1.0e-5,1.0e-8);
LinearRegressionObject.Learn();

print LinearRegressionObject.W;
