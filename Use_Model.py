from Perceptron import Perceptron
import Preprocessing as pre
import matplotlib.pyplot as plt

# draw the combinations
pre.DrawAllCombinations()

# Using model
# train and test the model from the Perceptron class
p = Perceptron(lr=pre.learning_rate, number_itration=pre.epochs, bais=pre.with_bias)
y_train = pre.y_train.to_numpy()
y_test = pre.y_test.to_numpy()
y_train[y_train == 0] = -1
y_test[y_test == 0] = -1

p.fit(pre.x_train.to_numpy(), y_train)
prediction = p.predict(pre.x_test.to_numpy())
print("accuracy : " + str(p.get_accuracy(y_test, prediction)*100)+"%")
tp, tn, fp, fn = p.confusion_Matrix(prediction, y_test)
p.print_Confusion_Matrix(tp, tn, fp, fn)


# plot perceptron line
all_first_feature_class1_points = []
all_first_feature_class2_points = []
all_second_feature_class1_points = []
all_second_feature_class2_points = []


for i in pre.x_train.columns:
    values_of_the_column = pre.x_train[i].to_numpy()
    for j in range(0, len(y_train)):
        if y_train[j] == -1 and i == pre.mainVariables.firstFeature:
            all_first_feature_class1_points.append(values_of_the_column[j])
        elif y_train[j] == 1 and i == pre.mainVariables.firstFeature:
            all_first_feature_class2_points.append(values_of_the_column[j])
        elif y_train[j] == -1 and i == pre.mainVariables.secondFeature:
            all_second_feature_class1_points.append(values_of_the_column[j])
        elif y_train[j] == 1 and i == pre.mainVariables.secondFeature:
            all_second_feature_class2_points.append(values_of_the_column[j])

plt.rcParams.update({'figure.figsize': (10, 8), 'figure.dpi': 100})
plt.scatter(all_first_feature_class1_points, all_second_feature_class1_points, color='red', label=pre.mainVariables.class1)
plt.scatter(all_first_feature_class2_points, all_second_feature_class2_points, color='blue', label=pre.mainVariables.class2)
plt.legend()
x_min = pre.x_train[pre.mainVariables.firstFeature].min()
x_max = pre.x_train[pre.mainVariables.firstFeature].max()
y_min, y_max = p.get_y_min_and_y_max(x_min,x_max)
plt.plot([x_min,x_max], [y_min, y_max])
plt.title("Perceptron Line")
plt.show()