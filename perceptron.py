import random

class Perceptron:
    weights = [None, None]
    learning_rate = 0.1
    
    def __init__(self):
        for i in range(2):
            self.weights[i] = random.uniform(-1, 1)

    def guess(self, inputs):
        sum_weights = 0
        for i in range(len(self.weights)):
            sum_weights += inputs.arr[i] * self.weights[i]
        if sum_weights > 0: return 1
        else: return -1

    def guess_print(self, inputs):
        print(self.guess(inputs) == inputs.flag)
                    
    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        for i in range(len(self.weights)):
            self.weights[i] += inputs.arr[i] * error * self.learning_rate
            if (error != 0):
                print((p.weights[0], p.weights[1]))
        

class Coordinate:
    def __init__(self):
        self.x = random.randint(0, 100)
        self.y = random.randint(0, 100)
        if (self.x >= self.y): self.flag = 1
        else: self.flag = -1
        self.arr = [self.x, self.y]

init_arr = []
training_arr = []

p = Perceptron()

for i in range(50):
    init_arr.append(Coordinate())
    training_arr.append(Coordinate())
    training_arr.append(Coordinate())
    training_arr.append(Coordinate())
    training_arr.append(Coordinate())
    training_arr.append(Coordinate())
    training_arr.append(Coordinate())
    training_arr.append(Coordinate())
    training_arr.append(Coordinate())
    testing_arr.append(Coordinate())

print((p.weights[0], p.weights[1]))

print("\ntesting\n")
for c in init_arr:
    p.guess_print(c)

print("\ntraining\n")

for c in training_arr:
    p.train(c, c.flag)

print("\ntesting\n")
for c in init_arr:
    p.guess_print(c)

print((p.weights[0], p.weights[1]))
