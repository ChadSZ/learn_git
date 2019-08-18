<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'show.jsp' starting page</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->

  </head>
  
  <body>
 	<!-- 获取请求中的指定参数值,其底层实际调用的是：
 	request.getParameter()
 	-->
	name=${param.name }<br/>
	age=${param.age }<br/>
	<!-- 直接输出的是数组:hobby=[Ljava.lang.String;@3d06bc14 -->
	hobby=${paramValues.hobby[0] }<br/>
	hobby=${paramValues.hobby[1] }<br/>
	hobby=${paramValues.hobby[2] }<br/>
	
	<!-- 获取初始化参数,其底层实际调用的是：
	serletContext.getInitParameter -->
	company = ${initParam.company }<br/>
	address = ${initParam.address }<br/>
	
	<hr/>
	
	${"abc"+"def" }
  </body>
</html>
