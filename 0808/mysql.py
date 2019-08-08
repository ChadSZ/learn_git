import pymysql.cursors

# Connect to the database
# ahulock2018@47.96.175.196:3307
connection = pymysql.connect(host='47.96.175.196',
                             port= 3307,
                             user='root',
                             password='ahulock2018',
                             db='learning',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "insert into `shenzhang` (`id`,`fullname`,`age`, `card`,`school`) VALUES (%s,%s, %s,%s, %s)"
        # cursor.execute(sql, ('1','yoyo', '3','P000001',"萌萌幼儿园"))
        # cursor.execute(sql, ('2','lily', '7','P000002',"箐箐小学"))
        # cursor.execute(sql, ('3','handy', '11','P000003',"健壮小学"))
        # cursor.execute(sql, ('4','handy', '19','P000004',"神奇一中"))

        # delete a new record
        sql = "delete from `shenzhang` where id = '%s' "
        # for i in range(0,50):
        #     cursor.execute(sql,i)
        # cursor.execute(sql,4)

        # update 
        sql = "update `shenzhang` set fullname=%s,age=%s where school=%s "
        # cursor.execute(sql,('xiaoqiang','16','箐箐小学'))

        # select 
        sql = "select `fullname`,`school` from `shenzhang`"
        count = cursor.execute(sql,)
        for i in range(count):
            result=cursor.fetchone()
            print(result)

    # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()


finally:
    connection.close()
