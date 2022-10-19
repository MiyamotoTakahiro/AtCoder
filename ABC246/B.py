import math

def main():
    A, B = list(map(int, input().split()))
    distance = math.sqrt(A**2 + B**2)
    unit_vector_x = A/distance
    unit_vector_y = B/distance
    print(unit_vector_x, unit_vector_y)


if __name__ == "__main__":
    main()