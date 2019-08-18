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
     	School school = new School("清华大学","北京海淀");
    	Student student = new Student("张三",23,school);
    	pageContext.setAttribute("student", student);
     %>
    student = ${student}<br/>
	name = ${student.name }<br/>
	age = ${student.age }<br/>
	name = ${student['name'] }<br/>
	age = ${student['age'] }<br/>
	
	<!-- 若访问为Null的对象的属性，EL是不会抛出空指针异常的，其仅仅是不显示而已。 -->
	name5=${student5.name }<br/>
	
	schoolName = ${student.school.sname }<br/>
	schoolAddress = ${student.school.address }<br/>
  </body>
</html>
