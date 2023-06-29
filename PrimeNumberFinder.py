import math

pnum = []
f = open("PrimeNumber.txt", 'a')
f1 = open("PrimeNumber.txt", 'r')
text = f1.read()
text = str(text)

befpnum = text.split("\n")                         #befpnum = ['2 3 5 7', '11 13'] 꼴
count_of_befpnum = len(befpnum)
for i in range(0, count_of_befpnum):               #count_of_befpnum은 여기서 2.
    Count_of_befpnum_i = len(befpnum[i].split(" ")) #Count_of_befpnum_i는 befpnum[i]를 띄어쓰기를 기준으로 나눴을때 문자의 개수.
    for j in range(0, Count_of_befpnum_i):
        pnum.append(befpnum[i].split(" ")[j])


print(pnum)

pnarrange = []
count_of_pnum = len(pnum)
print(pnum)
obj_num = int(pnum[count_of_pnum - 1]) + 1

def digit_num_count(num1):
    z = num1
    t = 0
    while True:

        if z >= 10:
            z = z/10
            t = t+1
        else:
            return t
            break

def num_is_divisable(num):
    print("확인 숫자: "+str(num))
    m = 0
    sqr = math.sqrt(num)
    for k in range(0, count_of_pnum):


        x = num/int(pnum[k])
        a = int(num/int(pnum[k]))
        print("x값: "+str(x)+", a 값: "+str(a))
        if x == a:
            print("소수가 아님")
            break
        if x != a:
            if int(pnum[k])>=sqr:
            #m = m + 1
            #if m == count_of_pnum:
                print("이것은 소수임")
                pnum.append(obj_num)
                print(pnum)
                if int(obj_num/100) == int(int(pnum[len(pnum)-2])/100)+1:
                    f.write("\n"+str(obj_num))
                else:
                    f.write(" "+str(obj_num))

                return obj_num


while True:
    num_is_divisable(obj_num)
    count_of_pnum = len(pnum)
    obj_num = obj_num + 1



#while True:
    #i = 2


#f.append()
f.close()
