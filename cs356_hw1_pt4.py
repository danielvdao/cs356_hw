from matplotlib import pyplot


x = [n for n in range(1, 21)]
y = [] 

for num in x:
  y.append(.001 + num * ( ((10000.0/20) + 100.0)/1000000 + .001 + .001))

print y

pyplot.plot(x,y)
pyplot.show()
