import numpy as np
import math

def vector_field_1(point):
    x, y, z = point
    try:
        return np.array(eval(input("Enter vector field 1 as a Python expression (e.g., [sin(x), cos(y), tan(z)]): ")))
    except Exception as e:
        print("Error:", e)
        return None

def vector_field_2(point):
    x, y, z = point
    try:
        return np.array(eval(input("Enter vector field 2 as a Python expression (e.g., [sin(x)**2, cos(y)**2, tan(z)**2]): ")))
    except Exception as e:
        print("Error:", e)
        return None

def lie_bracket(point):
    v1 = vector_field_1(point)
    v2 = vector_field_2(point)
    if v1 is None or v2 is None:
        return None
    jac_v1 = np.gradient(v1)
    jac_v2 = np.gradient(v2)
    bracket = np.cross(v1, jac_v2, axis=0) - np.cross(v2, jac_v1, axis=0)
    return bracket

def main():
    try:
        point = np.array(eval(input("Enter the point in the manifold as a Python expression (e.g., [1.0, 2.0, 3.0]): ")))
    except Exception as e:
        print("Error:", e)
        return
    result = lie_bracket(point)
    if result is not None:
        print("Lie bracket at point {}: {}".format(point, result))

if __name__ == "__main__":
    main()
