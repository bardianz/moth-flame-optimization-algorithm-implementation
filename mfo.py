import random

def objective_function(x):
    return x[0]**2 - 2 * x[0] * x[1] + x[1]**2

def moth_flame_optimization(x_min, x_max, max_iters, alpha, beta, gamma):
    x = [random.uniform(x_min[i], x_max[i]) for i in range(len(x_min))]

    for _ in range(max_iters):
        speed = alpha * random.uniform(0, 1)
        direction = beta * random.uniform(-1, 1)

        x_new = []
        for i in range(len(x)):
            x_new.append(x[i] + speed * direction)

        score_current = objective_function(x)
        score_new = objective_function(x_new)

        if score_new < score_current:
            x = x_new

    return x

if __name__ == "__main__":
    x_min = [-1, -1]
    x_max = [1, 1]
    max_iters = 1000
    alpha = 0.5
    beta = 0.7
    gamma = 0.1

    result = moth_flame_optimization(x_min, x_max, max_iters, alpha, beta, gamma)

    print("Optimized Point: ", result)
