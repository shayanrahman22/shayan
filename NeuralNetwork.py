import sys
import numpy as np
import matplotlib

inputs = [1.2,5.1,2.1,1.5]
weight1,weight2,weight3 = [3.1,2.1,8.7,2.4],[2.3,4.6,2.6,1.8],[5.3,7.3,1.5,3.6]

bias1,bias2,bias3 =2,3,0.5

output =[0,0,0]
for i in range(len(inputs)):
    output[0]+=inputs[i]*weight1[i]
output[0] += bias1

for i in range(len(inputs)):
    output[1]+=inputs[i]*weight2[i]
output[1] += bias2

for i in range(len(inputs)):
    output[2]+=inputs[i]*weight3[i]
output[2] += bias3

print(output)
