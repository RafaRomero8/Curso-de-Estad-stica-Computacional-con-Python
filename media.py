import random

def media(X):
    return sum(X)/ len(X)#len longitud de los valores



if __name__ == '__main__':
    X = [random.randint(1,21) for i in range(20)]
    mu = media(X)

    print(X)
    print(mu)