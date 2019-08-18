<%@ page language="java" import="java.util.*,learn03.Student,learn03.School" contentType="text/html; charset=utf-8" pageEncoding="UTF-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
  <head>   
    <title>My JSP 'index.jsp' starting page</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >

  </head>
  
  <body>

     <!-- 当前请求路径(http://localhost:8080/testEL/)的资源路径(http://localhost:8080/testEL) -->
<%-- 	<form action="${pageContext.request.contextPath }/registerServlet" method="POST"> --%>	
 	<form action="${pageContext.request.contextPath }/show.jsp" method="POST">
		姓名：<input type="text" name="name"/><br/>
		年龄：<input type="text" name="age"/> <br/>
		爱好：<input type="checkbox" name="hobby" value="swimming"/>游泳
		<input type="checkbox" name="hobby" value="climbing"/>登山
		<input type="checkbox" name="hobby" value="reading"/>阅读
		<br/>
		<input type="submit" value="注册"/>
	</form>
  </body>
</html>
