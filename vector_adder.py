import numpy as np

def vector_adder(v1_m, v1_a, v2_m, v2_a):
    v1_a, v2_a = (v1_a * np.pi)/180, (v2_a * np.pi)/180
    r_1 = (v1_m * np.cos(v1_a) + v2_m * np.cos(v2_a))
    r_2 = (v1_m * np.sin(v1_a) + v2_m * np.sin(v2_a))
    print("Calculating {} * {} + {} * {}.".format(v1_m, np.cos(v1_a) , v2_m , np.cos(v2_a)))
    print("Added({:.2f},{:.2f})".format(r_1, r_2))

v1_m, v1_a = float(input("v1_m:\n")),float(input("v1_a:\n"))
v2_m, v2_a = float(input("v2_m:\n")),float(input("v2_a:\n"))
vector_adder(v1_m, v1_a, v2_m, v2_a)