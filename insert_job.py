#! /usr/bin/env python
# encoding: utf-8

from sql_test import sqls_select, msql_select, msql_executemany
from dict_ import dict_


def get_sqls_columns():
        columns_name = sqls_test("Select Name FROM SysColumns Where id=Object_Id('v_fc_basysj');")
        str_list = []
        #print columns_name
        for i in columns_name:
                #print i[0]
                column_ = i[0]
                if column_ == 'HCV-Ab':
                        column_ = "'HCV-Ab'"
                elif column_ == 'HIV-Ab':
                        column_ = "'HIV-Ab'"
                str_list.append(column_)
        print str_list
        return str_list

def get_mysql_columns():
        columns_name = sqls_test("Select Name FROM SysColumns Where id=Object_Id('v_fc_basysj');")
        columns_name = [i[0] for i in columns_name]
        str_list = [dict_[i.lower()] if i.lower() in dict_.keys() else i.lower() for i in columns_name]
        print str_list
        return str_list


def insert_data():
        columns_list = get_sqls_columns()
        add_string = ', '.join(columns_list)
        sql = 'select top 3 {} from v_fc_basysj;'.format(add_string)
        result = sqls_select(sql)     #[(),(),()]
        #print result
        insert_data_list = [list(i) for i in result]   #列表化[[],[],[]]
        print insert_data_list
        print len(insert_data_list)
        return result


def insert_to_mys(data):
        import pymysql
        add1 = '%s, '*344
        add1 = add1.rstrip(', ')
        sql = "INSERT INTO home_page () VALUES ({})".format(add1)
        result = msql_executemany(sql,data)
        print 'Insert row effect:',result
        check_result = msql_select('select count(*) from home_page;')
        print "Checking from mysql : ",check_result


if __name__ == '__main__':
        #get_sqls_columns()
        #create_sql()
        insert_to_mys()

