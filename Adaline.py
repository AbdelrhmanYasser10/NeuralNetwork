import math

import numpy as np

class Adaline:
    def __init__(self, lr=0.01, number_itration=100, mse = 0.0,bais=True):
        self.lr = lr
        self.number_itration = number_itration
        self.with_bais = bais
        self.weight = None
        self.bais = None
        self.activation_function = self.__signum_Function
        self.mse = mse

    def fit(self, X, Y):
        m = X.shape[0]
        no_feature = X.shape[1]

        self.weight = np.random.rand(no_feature)
        self.bais = 0

        for _ in range(self.number_itration):
            all_predictions = []
            for index, x_i in enumerate(X):
                if self.with_bais:
                    net_value = np.dot(self.weight.T, x_i) + self.bais
                else:
                    net_value = np.dot(self.weight.T, x_i)
                y_prediction = net_value
                all_predictions.append(y_prediction)
                if Y[index] != y_prediction:
                    loss = Y[index] - y_prediction
                    dw = self.lr * loss

                    self.weight = self.weight + dw * x_i

                    if self.with_bais:
                        self.bais = self.bais + dw

            MSE = 1 / (2 * len(Y)) * sum((Y - all_predictions)**2)
            if MSE <= self.mse:
                break

    def predict(self, X):
        if self.with_bais:
            net_values = np.dot(X, self.weight) + self.bais
        else:
            net_values = np.dot(X, self.weight)

        Y_prediction = self.__signum_Function(net_values)
        return Y_prediction

    def __signum_Function(self, X):
        output = np.where(X > 0, 1, -1)
        return output

    def confusion_Matrix(self,y_prediction , y_actual):
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for i in range(0,len(y_prediction)):
            if y_prediction[i] == y_actual[i]:
                if y_actual[i] > 0:
                    tp += 1
                elif y_actual[i] < 0:
                    tn += 1
            else:
                if y_actual[i] > 0:
                    fp += 1
                elif y_actual[i] < 0:
                    fn += 1

        return tp, tn, fp, fn

    def print_Confusion_Matrix(self, tp, tn, fp, fn):
        print("""
                        |-------------------------------|
                        |         Actual Values         |
                        |-------------------------------|
                        |===============|===============|
                        |   positive    |   negative    |
                        |===============|===============|
        Predicted [+ve] |       """ + str(tp) + "    ""  |        """ + str(fp) + """      |
                        |===============|===============|
        Predicted [-ve] |       """ + str(fn) + "   ""    |       """ + str(tn) + """      |
                        |===============|===============|
        """)


    def get_accuracy(self,y_actual,y_prediction):
        return sum(1 for x, y in zip(y_actual, y_prediction) if x == y) / float(len(y_actual))


    def get_y_min_and_y_max(self,x_min , x_max):
        y_min = -1 * (self.bais + self.weight[0] * x_min) / self.weight[1]
        y_max = -1 * (self.bais + self.weight[0] * x_max) / self.weight[1]
        return y_min, y_max