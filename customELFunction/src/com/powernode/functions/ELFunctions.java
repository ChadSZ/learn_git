package com.powernode.functions;

//�Զ��庯��
//�����Jspҳ��Ӧ�ã�
//���༰�亯������Ҫ��һ����չ��Ϊ.tld��XML�ļ��н���ע��
//tld,tag library definition,��ǩ�ⶨ��
//XML�ļ�����ҪԼ���ģ�����Ҫ�����ļ�ͷ�������ͷ���ļ����Դ������ļ��и��ƣ�
//��Tomcat��װĿ¼��;jsp2-example-taglib.tld
//���.tld��XML�ļ�����Ҫ�����ڵ�ǰweb��Ŀ��WEB-INFĿ¼��
public class ELFunctions {
//	���ַ���Сд���д
	public static String lowerToUpper(String source){
		return source.toUpperCase();	
	}
//	���ַ�����д��Сд
	public static String upperToLower(String source){
		return source.toLowerCase();	
	}
}
