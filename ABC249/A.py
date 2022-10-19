A,B,C,D,E,F,X = list(map(int, input().split()))

Taka = int(X/(A+C))
Ao = int(X/(D+F))

takahashi = Taka*A*B
if (X-Taka*(A+C)) <= A:
    takahashi += (X-Taka*(A+C))*B
else:
    takahashi += A*B

aoki = Ao*D*E
if (X-Ao*(D+F)) <= D:
    aoki += (X-Ao*(D+F))*E
else:
    aoki += D*E

if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")
