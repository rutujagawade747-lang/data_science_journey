from sklearn.datasets import load_iris
iris= load_iris()
print(iris)
print(iris.feature_names)
print(iris.target_names)#the three species: setosa, versicolor, and virginica.
print(iris.data.shape)
print(iris.target.shape)