## MySQL
### MySql数据库的安装

主机：47.96.175.196
端口：3307
数据库名：learning
密码：ahulock2018

2001:da8::666

### MySQL 优点：

    性能快捷、优化SQL语言
    容易使用
    多线程和可靠性
    多用户支持
    可移植性和开放源代码
    遵循国际标准和国际化支持
    为多种编程语言提供API

### MySQL 连接
1. 远程连接
连接mysql 	 格式： mysql -h主机地址 -u用户名 －p用户密码

2. 本地MySQL连接
mysql -u root -p

### MySQL 库的建立和使用
1. 显示当前数据库服务器中的数据库列表

    mysql> SHOW DATABASES;

2. 显示某个数据库中的数据表

    mysql> USE 库名；//使用某个库    
    mysql> SHOW TABLES；//列出库中所有的表   

3. 显示数据表的结构(表的定义)   

    mysql> DESCRIBE 表名
    或DESC 表名；

4．建立数据库    
 
    mysql> CREATE DATABASE 库名；

5．建立数据表

    mysql> USE 库名；
    mysql> CREATE TABLE 表名 (字段名 VARCHAR(20), 字段名 CHAR(1))；

6．删除数据库

    mysql> DROP DATABASE 库名；

7．删除数据表

    mysql> DROP TABLE 表名； 

### 遇见的小问题：
* [Err] 1055 - Expression #1 of ORDER BY clause is not in GROUP BY clause and contains nonaggregated column 'information_schema.PROFILING.SEQ' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by

[点击访问链接](https://www.cnblogs.com/xzjf/p/8466858.html)

    通过以下语句：SHOW VARIABLES LIKE '%sql_mode%'; 可以查到当前的sql模式

    严格的约束条件：ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION



### mysql语句：
1. 删除语句：
* delete from 表名 where id = 1;
* truncate 表名;

2. 更新语句：
* update from 表名 set 字段 = 值，字段 = 值，... where ...;

3. 查询语句：
* select * from 表名;
* select 字段1，字段2，... from 表名;
* select * from 表名 order by id desc / asc(降序和升序);

4. 添加语句：
* insert into 表名(字段1，字段2，...) values(数据1，数据2，...);

5. in / not in 

6. > <
* 条件功能

7. 嵌套语句：
* select * from 表名 where card in(select card from 表名 where fullName='xxx');

8. 用文本方式将数据装入数据表中
* mysql> LOAD DATA LOCAL INFILE “D:/mysql.txt” INTO TABLE 表名；

9. 导入.sql文件命令
* mysql> USE 数据库名；
* mysql> SOURCE d:/mysql.sql；

10. 显示use的数据库名
* mysql> SELECT DATABASE()；
。
11. 显示当前的user
* mysql> SELECT USER()；


### MySQL 注释语句：
* /**/ 注释多行
* '#' 注释单行