def fnd_average_d(outter_height, inner_height):
    average = 0
    n = len(outter_height)
    for i in range(n):
        outter_height[i] = abs(outter_height[i] - inner_height[i])
        average += outter_height[i]
        # print(outter_height[i])
    
    print(f"D: {outter_height}")
    return average/n


def fnd_average_h(capillary_height, water_height):
    average = 0
    n = len(capillary_height)
    for i in range(n):
        capillary_height[i] = abs(capillary_height[i] - water_height[i])
        average += capillary_height[i]
        print(f"D: {round(capillary_height[i], 3)}")
    
   
    return average/n


def find_sigma(p, g, h, d):
    
    sigma = p * g * d * (h + d/6)
    sigma = sigma/4000
    
    return sigma


def find_error(actual_value, experiment_value):
    numerator = abs(actual_value - experiment_value)
    denominator = actual_value
    Ur = numerator/denominator * 100
    return Ur