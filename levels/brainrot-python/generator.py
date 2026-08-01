flag = 'd4rk{sk1b1d1_r1zz_4m1r173}'

x = [1, 2]

for i in range(16000):
    # print(i)
    x.append(x[-1] + x[-2])

skibidi = []
for f in flag:
    skibidi.append(x[ord(f)])
    # print(ord(f) * ord(f))

print(skibidi)