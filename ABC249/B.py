from collections import Counter

def is_include_upper_and_lower(S):
    total_len = len(S)
    count_upper = 0
    count_lower = 0
    for s in S:
        if s.isupper():
            count_upper += 1
        if s.islower():
            count_lower += 1

    if count_upper == total_len:
        return False
    if count_lower == total_len:
        return False
    return True

def is_dabutteru(S):
    counter = Counter(S)
    value = counter.values()
    for v in value:
        if v==1:
            pass
        else:
            return False
    return True

def main():
    S = input()
    if is_include_upper_and_lower(S):
        pass
    else:
        return False

    if is_dabutteru(S):
        return True
    else:
        return False





if __name__ == "__main__":
    ret = main()
    if ret:
        print("Yes")
    else:
        print("No")
