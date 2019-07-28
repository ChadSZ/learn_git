# 输入三条边的长度，如果能构成三角形就计算周长和面积。

# 下面是错误的float基本类型不能对list直接操作
# tri_edge1,tri_edge2,tri_edge3 = float(input("分别输入三条边长：").split(','))

import math
#输入三边长
a,b,c = map(float,input("请依次输入三边边长，以逗号隔开：").split(","))
#判断三边长是否满足三角形条件
if a > 0 and b > 0 and c > 0 :
    if a+b>c and a+c>b and b+c>a :
        perimeter = a + b + c
        s2 = perimeter*(perimeter-a)*(perimeter-b)*(perimeter-c)
        #调用math方法，获取面积s
        s = math.sqrt(s2)
        # print(type(s))
        # 保留后两位
        s = ("%.2f" %s)
        print("三角形周长为：",perimeter,"三角形面积为：",s)
    else:
        print("不能构成三角形")
else:
    print("输入的边长不满足三角形构成条件")
    