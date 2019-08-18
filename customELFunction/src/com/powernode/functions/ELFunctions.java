package com.powernode.functions;

//自定义函数
//如何在Jsp页面应用？
//该类及其函数，需要在一个扩展名为.tld的XML文件中进行注册
//tld,tag library definition,标签库定义
//XML文件是需要约束的，即需要配置文件头部。这个头部文件可以从以下文件中复制：
//在Tomcat安装目录中;jsp2-example-taglib.tld
//这个.tld的XML文件，需要定义在当前web项目的WEB-INF目录下
public class ELFunctions {
//	将字符串小写变大写
	public static String lowerToUpper(String source){
		return source.toUpperCase();	
	}
//	将字符串大写变小写
	public static String upperToLower(String source){
		return source.toLowerCase();	
	}
}
