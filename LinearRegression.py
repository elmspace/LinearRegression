
class LinearRegression:

    def __init__ (self,input_TrainingSet,input_YSet,input_Weights,input_LearningRate,input_ConvCondition):
        print "Initializing the Linear Regression Object . . ."
        self.X_training = input_TrainingSet;
        self.Y_training = input_YSet;
        self.W = input_Weights;
        self.W_temp = [0]*len(self.W);
        self.ConvCondition = input_ConvCondition;
        self.LearningRate = input_LearningRate;
        self.TrainingSetSize = len(self.Y_training);
        self.FeatureSetSize = len(self.X_training[0]);


    def Learn(self):
        w_old=0.0;
        ConvDelta = 1.0e10;
        counter = 0;

        while ConvDelta > self.ConvCondition or counter < 10:

            w_now = sum(map(abs,self.W))/len(self.W);
            for i in range (0,self.TrainingSetSize):
                Delta = self.Y_training[i] - self.Hypothesis(self.X_training[i],self.W);
                for j in range (0,self.FeatureSetSize):
                    self.W_temp[j] = self.W[j] + self.LearningRate*Delta*self.X_training[i][j];
                self.W = self.W_temp[:];

            ConvDelta = w_now-w_old;
            w_old = w_now;
            counter=counter+1;




    def Hypothesis(self,input_X,input_W):
        ReturnArg = 0.0;
        if(len(input_X)!=len(input_W)):
            print "The size of the input X and W do not match!"
            exit(1);
        else:
            for i in range(0,len(input_X)):
                ReturnArg += input_X[i]*input_W[i];
        return ReturnArg;
