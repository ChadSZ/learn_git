#输入年份判断是否是闰年

#输入年份
year_n = int(input("请输入年份："),10);

if year_n % 100 == 0:
    if year_n % 400 == 0:
        print("该年份是闰年");
    else:
        print("该年份不是闰年");
else:
    if year_n %4 == 0:
        print("该年份是闰年");
    else:
        print("该年份不是闰年");