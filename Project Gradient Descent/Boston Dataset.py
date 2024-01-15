import numpy as np
from sklearn import preprocessing
from sklearn import model_selection
training=np.loadtxt('0000000000002417_training_boston_x_y_train.csv', delimiter=',')
testing=np.loadtxt('0000000000002417_test_boston_x_test.csv', delimiter=',')


def step_gradient(X, Y, m, learning_rate):
    m_slope=np.zeros(len(X[0]))
    for i in range(len(X)):
        x=X[i]
        y=Y[i]
        for j in range(len(x)):
            m_slope[j]+=(-2/len(X))*(y-sum(m*x))*x[j]
    new_m=m-(learning_rate*m_slope)
    return new_m


def cost(m, x, y):
    cost=0
    for i in range(len(x)):
        cost+=(1/len(x))*((y[i]-sum(m*x[i]))**2)
    print(cost)


def gd(x, y, learning_rate, iterations):
    m=np.zeros(len(x[0]))
    for i in range(iterations):
        m=step_gradient(x, y, m, learning_rate)
        print("itr= ", i, "cost=", end=' ')
        cost(m, x, y)
    return m


def gradient_descent(x, y):
    iterations=300
    learning_rate=0.005
    x=np.append(x, np.ones(len(x)).reshape(-1, 1), axis=1)
    m=gd(x, y, learning_rate, iterations)
    return m


x=training[:, :-1]
y=training[:, -1]
#adding squared values of each column
sq=[]
for i in range(len(x[0])):
    for j in range(i, len(x[0])):
        for k in range(j, len(x[0])):
            sq.append(x[:, i]*x[:, j]*x[:, k])
sq=np.array(sq)
for i in sq:
    x=np.append(x, i.reshape(-1, 1), axis=1)
#scaling
scaler=preprocessing.StandardScaler()
scaler.fit(x)
x=scaler.transform(x)
m=gradient_descent(x, y)


sq=[]
for i in range(len(testing[0])):
    for j in range(i, len(testing[0])):
        for k in range(j, len(testing[0])):
            sq.append(testing[:, i]*testing[:, j]*testing[:, k])
sq=np.array(sq)
for i in sq:
    testing=np.append(testing, i.reshape(-1, 1), axis=1)

testing1=scaler.transform(testing)
x_test=np.append(testing1, np.ones(len(testing1)).reshape(-1, 1), axis=1)
ans=[]
for i in x_test:
    ans.append(sum(i*m))
for i in ans:
    print(i)
ans=np.array(ans)
np.savetxt(X=ans,fname='dataa.csv' , delimiter=',', fmt='%.5f')
