from NeuralNetwork import NN

layers = [3, 4, 5, 2]
nn = NN(layers)
nn.train([(1, 4), (2, 3), (3, 6)],50, 10, 0.1)
y = nn.predict([1, 2, 3])
correct_num = nn.evaluate([(1, 4), (2, 3), (3, 6)])
