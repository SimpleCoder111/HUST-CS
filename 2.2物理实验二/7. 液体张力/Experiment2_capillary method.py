import utils_2 as utils

print("find average d")
outter_heihgts = [12.868, 12.865, 12.862, 12.858, 12.860]
inner_heights = [13.748, 13.772, 13.771, 13.765, 13.760]
print(f"inner_height: {inner_heights}")
print(f"outter_height: {outter_heihgts}")
d = utils.fnd_average_d(outter_heihgts, inner_heights)
print(f"D: {d}")

print("\nfind average h")
capillary_heights = [50.458, 50.518, 50.521, 50.410, 50.423]
water_heights = [18.305, 18.292, 18.138, 18.428, 18.235]
print(f"capillary_heights: {capillary_heights}")
print(f"water_heights: {water_heights}")
h = utils.fnd_average_h(capillary_heights, water_heights)
print(f"H: {h}")


print("\nfind sigma")
p = 997.638
g = 9.79338

sigma = utils.find_sigma(p=p, g=g, h=h, d=d)
print(sigma)

print("\nfind error")
actual_sigma = 72.28
Ur = utils.find_error(actual_sigma, sigma)
print(f"Error rate: {Ur}%")
