## .gitignore文件的书写：
1. ）空行或者是以#开头的行会被忽略
2. ）在前边加上 / 表示递归子目录，比如目录结构是
4. ）可以使用!来否定忽略，即比如在前面用了*.apk，然后使用!a.apk，则这个a.apk不会被忽略。
5. ）*用来匹配零个或多个字符，如*.[oa]忽略所有以".o"或".a"结尾，*~忽略所有以~结尾的文件（这种文件通常被许多编辑器标记为临时文件）；[]用来匹配括号内的任一字符，如[abc]，也可以在括号内加连接符，如[0-9]匹配0至9的数；?用来匹配单个字符


## classpath和path路径的相对路径：
classpath：.;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar;

%JAVA_HOME%\bin
%JAVA_HOME%\JRE\bin

路径的绝对路径：
C:H:\java\myeclipes\bin
H:\java\myeclipes\jre\bin

java的应用：javaweb和安卓。客户端，大数据，AI，...

.dll文件是c++编译的文件
编译型语言：如C++，C，Delphi
解释型语音：如python，javascript
java语音：字节码文件，先编译后解释。

Javaweb学习，开始学习JSP和Servelet基础

## 补充：
JAVA中的length属性和length()方法和size()方法的区别
 首先length是在数组中获取数组的长度的属性，而length()是用来获取字符串的长度的方法！
（1. ）java中的length属性是针对数组说的，比如说你声明了一个数组，想知道这个数组的长度则用到了length这个属性。
（2. ）java中的length()方法是针对字符串String说的，如果想看这个字符串的长度则用到length()这个方法。
（3. ）java中的size()方法是针对泛型集合说的，如果想看这个泛型有多少个元素，就调用此方法来查看。
length是数组的属性；
length（）是字符串类的方法，本质上也是调用了数组的length属性。因为字符串底层也是char数组。


