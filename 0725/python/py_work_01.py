#华氏温度转换为摄氏温度
#公式：华氏温度(F_Temp)=摄氏温度(C_Temp)*9/5+32
#公式：摄氏温度(C_Temp) = (华氏温度(F_Temp)-32)*5/9

#输入float类型的数据
F_Temp = float(input("请输入华氏温度："));
#输出之前输入的华氏温度
print("当前输入华氏温度：",F_Temp,type(F_Temp));
#计算输入的数据
C_Temp = float((F_Temp-32)*5/9);
#输出摄氏温度
print("未变化小数位摄氏温度：",C_Temp,type(C_Temp));
#输出小数位为两位的摄氏温度
print("转换后的摄氏温度为:",round(C_Temp,2));
print("转换后的摄氏温度为:",("%.2f" %C_Temp));
#使用Decimal函数
from decimal import Decimal;
print(Decimal(C_Temp).quantize(Decimal("0.00")));




