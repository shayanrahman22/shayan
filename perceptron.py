import random 

class Perceptron:
    def __init__(self,n):
        self.weight = []
        self.learningConstant =0.01       
        self.n = n
        for i in range(n):
            self.weight.append(random.uniform(-1,1))
    def activation_function(self,sum):
        if sum>0:
            return 1
        else:
            return -1

    def feed_forward(self,inputs):
        sum = 0
        for i in range(self.n):
            sum += inputs[i]*self.weight[i]

        return self.activation_function(sum)

    def train(self,inputs,desired):
        guess = P.feed_forward(inputs)
        error = desired - guess

        for i in range(len(self.weight)):
            self.weight[i]=self.weight+error*inputs[i]*self.learningConstant

    def function(self,x):
        return 0.5 *x -1


P = Perceptron(3)
inputs=[50,-12,1]
for i in range(10):
    guess = P.feed_forward(inputs)
    print(guess)


