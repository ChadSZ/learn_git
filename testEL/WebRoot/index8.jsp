<%@ page language="java" import="java.util.*,learn03.Student,learn03.School" pageEncoding="utf-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'index.jsp' starting page</title>
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
  
	<%
     	String username = null;
     	String schoolName = "";
     	
     	List<Student> students = new ArrayList<Student>();
     	
     	pageContext.setAttribute("username", username);
     	pageContext.setAttribute("schoolName", schoolName);
     	pageContext.setAttribute("students", students);
     %>
     <!-- empty对于没有定义的变量的运算结果为：true -->
	empty name = ${empty name }<br/>
	
     <!-- empty对于为null的引用的运算结果为：true -->
	empty username = ${empty username }<br/>
	
     <!-- empty对于空串的引用的运算结果为：true -->
	empty schoolName = ${empty schoolName }<br/>
	
     <!-- empty对于没有元素的数组或集合的运算结果为：true -->
	empty students = ${empty students }<br/>
  </body>
</html>
