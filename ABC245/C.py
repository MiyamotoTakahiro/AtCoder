def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    x_1 = A[0]
    x_2 = B[0]

    for i in range(N-1):
        candidate1 = None
        candidate2 = None
        if abs(x_1 - A[i+1]) <= K:
            candidate1 = A[i+1]
        if abs(x_1 - B[i+1]) <= K:
            candidate2 = B[i+1]
        if abs(x_2 - A[i+1]) <= K:
            candidate1 = A[i+1]
        if abs(x_2 - B[i+1]) <= K:
            candidate2 = B[i+1]

        if candidate1 == None and candidate2 == None:
            return False
        elif candidate1 == None:
            x_1 = candidate2
            x_2 = candidate2
        elif candidate2 == None:
            x_1 = candidate1
            x_2 = candidate1
        else:
            x_1 = candidate1
            x_2 = candidate2
    return True

if __name__ == "__main__":
    if main():
        print("Yes")
    else:
        print("No")
