import math



#typ = input("사용하려는 용도 1. 밀도 구하기")
r = input("반지름(km) or type N : ")
r = r.replace(",","")
def v_clc(R):
    global v
    v = 4/3*3.14*r*r*r
pi = 3.14


if "N" in r:
    v = input("부피(km^3) : ")
    v = float(v)
else:
    r = float(r)
    v_clc(r)

print(v)

m = input("질량( × 10^n kg) : ")
a = m.split("^")
c = int(a[1])
b = a[0].split(" × ")
d = float(b[0])

for i in range(0, c):
    d = d*10

d = float(d)


def meal(V, M):
    k = M/V
    return k

rslt = meal(v, d)
print(str(rslt)+"kg/km^3입니다.")
for q in range(0, 12):
    rslt = rslt/10
print(str(rslt)+"g/cm^3입니다.")