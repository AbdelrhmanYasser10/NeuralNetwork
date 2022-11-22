from Perceptron import Perceptron
class MLP:
    def __init__(self,hiddenlayers=0,neurons=0,epochs=0,lr=0.01,activation = 1, bias=True):
        self.HL = hiddenlayers
        self.neurons = neurons
        self.epochs = epochs
        self.eta = lr
        if activation==1 : 
            self.activation = "sigmoid"
        elif activation == 2: 
            self.activation = "tanh"

        self.bias = bias    