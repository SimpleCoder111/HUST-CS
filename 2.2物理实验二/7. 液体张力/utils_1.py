import math
import numpy as np

def find_F(x):
    size = len(x)
    g = 9.79338
    for i in range(size):
        x[i] = round(x[i]*g, 3)
    return x


# def find_slope_by_mean_square(x, y):
#     sigma_x = 0
#     sigma_y = 0
#     sigma_xy = 0
#     sigma_x_square = 0
    
#     loop = len(x)
    
#     for i in range(loop):
#         sigma_x += x[i]
#         sigma_y += y[i]
#         sigma_xy += x[i]*y[i]
#         sigma_x_square += pow(x[i], 2)

#     # print(sigma_x)
#     # print(sigma_y)
#     # print(sigma_xy)
#     # print(sigma_x_square)

#     n_sigma_xy = 10 * sigma_x * sigma_y
#     # print(n_sigma_xy)

#     fun1 = sigma_xy - (10*sigma_x/10*sigma_y/10)
#     fun2 = sigma_x_square - (10*pow(sigma_x/10, 2))

#     b = fun1/fun2

#     # print(b)

#     k = sigma_y/10 - b*sigma_x/10
#     # print(k)
#     return k

def find_sigma(delta_U, D1, D2, K):
    numerator = delta_U
    denominator = math.pi * (D1 + D2) * K 
    sigma = round(numerator/denominator*100, 3)
    return sigma

def find_error(actual_value, experiment_value):
    numerator = abs(actual_value - experiment_value)
    denominator = actual_value
    Ur = numerator/denominator * 100
    return Ur
    


def find_slope_and_intercept(x, y):
    # Use polyfit with degree 1 to find the slope and intercept
    k, b = np.polyfit(x, y, 1)
    k = round(k, 3)
    b = round(b, 3)
    return k, b

# # Example usage:
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# k, b = find_slope_and_intercept(x, y)
# print(f"Slope (k): {k}")
# print(f"Intercept (b): {b}")