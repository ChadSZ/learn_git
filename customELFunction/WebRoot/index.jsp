<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@
	taglib uri="http://www.powernode.com/jsp/el/functions" prefix="myFunction"
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>

  </head>
  
  <body>
    ${myFunction:myLowerToUpper("abc") }<br/>
    
    <!-- EL函数只能处理四大域中的属性值及String常量 -->
    <%
    	String username="tom";
    	pageContext.setAttribute("username", username);
     %>
     ${myFunction:myLowerToUpper(username) }<br/>
  </body>
</html>
