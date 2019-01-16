#!/usr/bin/env python
# encoding: utf-8
import DAL
import json

def show_china(s):
	print json.dumps(s, indent = 0,ensure_ascii = False)

#----------------------------------------------------------------------------------------------------
def sqls_select(sql):
	con_sqls = DAL.sqlserver('','','')
	if con_sqls:
		print "connected"
		#sql = "Select Name FROM SysColumns Where id=Object_Id('');"
		#sql = "SELECT TOP 1 * FROM "
		rowcount, result = con_sqls.execute(sql)
		print result
		print len(result)
	con_sqls.close()
	return result

def msql_select(sql):
	con_msql = DAL.Mysql('127.0.0.1','root','','', )
	if con_msql:
		print "connected"
		rowcount, result = con_msql.execute(sql)
		print result
	con_msql.close()
	return result

def msql_executemany(sql,data):
	con_msql = DAL.Mysql('127.0.0.1','root','','', )
	if con_msql:
		print "connected"
		effect_row = con_msql.executemany(sql,data)
		print result
		print '-'*80
	con_msql.close()
	return effect_row

 
if __name__ == '__main__':
	#select_id_list_from_sqls(False)
	#select_path_from_db2(select_id_list_from_sqls(False))
	#msql_test()
	sqls_test()
	#check_lock()

