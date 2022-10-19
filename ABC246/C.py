import numpy as np

def main():
    N, K, X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A = np.array(A)
    if sum(A//X) >= K:
        ans_total_cost = sum(A) - (K * X)
    else:
        new_list = A - X*(A//X)
        new_list = np.sort(new_list)[::-1]
        rest_qoupen = K - sum(A//X)
        for i in range(rest_qoupen):
            if i > len(new_list)-1:
                break
            else:
                new_list[i] = 0
        ans_total_cost = sum(new_list)

    print(ans_total_cost)



if __name__ == "__main__":
    main()
