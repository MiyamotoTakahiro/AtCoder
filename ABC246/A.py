import collections

def main():
    x1, y1 = list(map(int, input().split()))
    x2, y2 = list(map(int, input().split()))
    x3, y3 = list(map(int, input().split()))
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    x_counter = collections.Counter(x)
    y_counter = collections.Counter(y)
    for x_key in x_counter.keys():
        if x_counter[x_key] == 1:
            ans_x = x_key
        else:
            pass
    for y_key in y_counter.keys():
        if y_counter[y_key] == 1:
            ans_y = y_key
        else:
            pass

    print(ans_x, ans_y)


if __name__ == "__main__":
    main()
