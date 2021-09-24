import numpy as np

def KNN_test(X, Y, a, b, K):
    accuracy = 0
    sample_size = len(b)
    for j in range(sample_size):
        distance = np.array([np.sum(np.square(abs(X[i] - a[j]))) for i in range(len(X))])
        print(distance)
        print(K)
        idx = np.argsort(distance)[:K]
        print(idx)
        knear = np.array([Y[i] for i in idx]).sum()
        print([distance[i] for i in idx], knear)
        label = 1 if knear > 0 else -1
        if label == b[j]:
            accuracy = accuracy + 1
    return accuracy / float(sample_size)

def choose_K(X_train,Y_train,X_val,Y_val):
    best_accuracy=0
    best_k=0
    for i in range(10):
        accuracy=KNN_test(X_train,Y_train,X_val,Y_val,i)
        print(accuracy)
        if accuracy>best_accuracy:
            best_accuracy=accuracy
            best_k=i
    return best_k

