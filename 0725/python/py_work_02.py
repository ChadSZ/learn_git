#输入圆的半径计算周长和面积
#周长公式：C = π * r *2, 面积 S = π * r * r

#定义PI
PI = 3.14;
#输入半径
r = float(input("请输入半径："));
#计算周长
C = PI * r * 2;
print(C,type(C));
#小数点二位
print("%.2f" %C);
print(round(C,2));
from decimal import Decimal;
print(Decimal(C).quantize(Decimal("0.00")));

#计算面积
S = PI * r * r;
#小数点二位
print("%.2f" %S);
print(round(S,2));
from decimal import Decimal;
print(Decimal(S).quantize(Decimal("0.00")));