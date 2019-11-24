from include.IProcessUnit import IProcessUnit

class ProcessUnit(IProcessUnit):
    def __init__(self):
        IProcessUnit.__init__(self)

    def AddDataToTrain(self, matrix):
        self.train_data.append(matrix)
    
    def Train(self):
        buf = []
        for data in self.train_data:
            
            
            # print(data)
            (x_test, y_test) = data
           
            self.model.train_on_batch(x_test, y_test)

    def Evaluate(self, matrix):
        (x_test, y_test) = matrix
        return self.model.Evaluate(x_test, y_test, batch_size=128)
        
