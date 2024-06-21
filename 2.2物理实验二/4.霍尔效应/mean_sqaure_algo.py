import math

x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
y = [6.47, 12.69, 18.73, 25.12, 31.33, 37.53, 43.71, 50.07, 56.31, 62.64]

sigma_x = 0
sigma_y = 0
sigma_xy = 0
sigma_x_square = 0
for i in range(10):
    sigma_x += x[i]
    sigma_y += y[i]
    sigma_xy += x[i]*y[i]
    sigma_x_square += pow(x[i], 2)

print(sigma_x)
print(sigma_y)
print(sigma_xy)
print(sigma_x_square)

n_sigma_xy = 10 * sigma_x * sigma_y
print(n_sigma_xy)

fun1 = sigma_xy - (10*sigma_x/10*sigma_y/10)
fun2 = sigma_x_square - (10*pow(sigma_x/10, 2))

b = fun1/fun2

print(b)

k = sigma_y/10 - b*sigma_x/10
print(k)