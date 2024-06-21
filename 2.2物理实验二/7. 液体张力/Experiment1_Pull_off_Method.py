import utils_1 as utils
# def find_F(x):
#     size = len(x)
#     g = 9.79338
#     for i in range(size):
#         x[i] = round(x[i]*g, 3)
#     return x


# Experiment 1.1
print(f"Experiment 1.1")
m = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]
f = utils.find_F(m)
U = [0.0, 10.5, 20.7, 37.3, 44.1, 51.8, 63.9, 73.2]
# U = [0.0, 11.6, 23.4, 35.5, 47.9, 59.4, 72.0, 83.3]
# g.pop(0)
# U.pop(0)
print(f"m(g) : {m}")
print(f"F(N): {f}")
print(f"U(mV): {U}")

print(f"find slope k and intercept b")
K, b = utils.find_slope_and_intercept(x=f, y=U)
print(f"y = {K}x + {b}")

print(f"\nExperiment 1.2")
D1 = 3.310
D2 = 3.496
U1 = [21.7, 22.8,20.6,20.3,21.8,21.9]
U2 = [-10.5, -10.5, -10.3, -10.4, -10.6, -10.6]
delta_U = [u1 - u2 for u1, u2 in zip(U1, U2)]
average_delta_U = sum(delta_U) / len(delta_U)

print(f"U1(mV): {U1}")
print(f"U2(mV): {U2}")
print(f"U1-U2: {delta_U}")
print(f"average_delta_U: {average_delta_U}")

print(f"\nfind sigma")
sigma = utils.find_sigma(average_delta_U, D1, D2, K)
print(f"experiment sigma: {sigma}")

print(f"Analyst Error")
real_sigma = 72.28
Ur = utils.find_error(real_sigma, sigma)
print(f"Error rate: {Ur}%")

print(f"X = 10 y = ?")
x = 15
y = K*x + b
print(y)