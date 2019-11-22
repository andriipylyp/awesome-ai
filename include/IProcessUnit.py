import keras
from keras.models import Sequential
from keras.layers import Dense

class IProcessUnit(object):
    def __init__(self):
        self.train_data = []
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_dim=10))
        self.model.add(Dense(10, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

    def AddDataToTrain(self, matrix):
        raise Exception("NotImplementedException")

    def Train(self):
        raise Exception("NotImplementedException")

    def Evaluate(self, file_name):
        raise Exception("NotImplementedException")