# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class sqlserver(object):

    def __init__(self, host, user, pwd,):
        import pymssql
        # connstr = "host={},user={},password={},charset=utf8".format(host,user,pwd)
        self._conn = pymssql.connect(host='{}'.format(host),user='{}'.format(user),password='{}'.format(pwd),charset='utf8')
        self._cursor = self._conn.cursor()

    def execute(self, sql):
        self._cursor.execute(sql)
	return self._cursor.rowcount, self._cursor.fetchall()

    def close(self):
        self._cursor.close()
        self._conn.close()
#-----------------------------------------------------------------------------------------
class Mysql(object):
    '''
    Mysql连接
    '''
    def __init__(self, ip, user, pwd, db, port):
        import pymysql
        self._conn = pymysql.connect(host='{}'.format(ip),
            user='{}'.format(user),
            password='{}'.format(pwd),
	    db='{}'.format(db),
	    port=int('{}'.format(port)))
        self._cursor = self._conn.cursor()

    def execute(self, sql):
        self._cursor.execute(sql)
        self.result_list = []
        for i in self._cursor.fetchall():
            self.result_list.append(i[0])
        return self._cursor.rowcount, self.result_list

    def executemany(self, sql, data):
        self._cursor.executemany(sql, data)
        self._cursor.commit()
        return self._cursor.rowcount, self._cursor.fetchall()

    def close(self):
        self._cursor.close()
        self._conn.close()

#-----------------------------------------------------------------------------------------
class DB2(object):
    
    def __init__(self, db, host, port, user, pwd):
        import ibm_db
        connstr = "DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={};PWD={};".format(db,host,port,user,pwd)
        self._conn = ibm_db.connect(connstr,"","")

    def execute(self,sql):
        self._stmt = ibm_db.exec_immediate(self._conn,sql)
        self._result = ibm_db.fetch_tuple(self._stmt)
        self.result_list = []
        while(self._result):
            self.result_list.append(self._result)
            self._result = ibm_db.fetch_tuple(self._stmt)
        return self.result_list

    def close(self):
        ibm_db.close(self._conn)
#------------------------------------------------------------------------------------------
class Oracle(object):
    """
    Oracle 连接
    """

    def __init__(self, user, pwd, ip, port, database):
        import cx_Oracle
        connstr = '{}/{}@{}:{}/{}'.format(user, pwd, ip, port, database)
        self._conn = cx_Oracle.connect(connstr)
        self._cursor = self._conn.cursor()

    def execute(self, sql):
        self._cursor.execute(sql)
        return self._cursor.rowcount, self._cursor.fetchall()

    def close(self):
        self._cursor.close
        self._conn.close()
#------------------------------------------------------------------------------------------
'''
class Mysql(object):
    """
    Mysql 连接
    """
    def __init__(self, ip, port, user, pwd, database, charset="utf8", autocommit=1):
        import MySQLdb
        connjson = {}
        connjson["host"] = ip
        connjson["port"] = int(port)
        connjson["user"] = user
        connjson["passwd"] = pwd
        connjson["db"] = database
        connjson["charset"] = "utf8"
        self._conn = MySQLdb.connect(**connjson)
        self._conn.autocommit(autocommit)
        self._cursor = self._conn.cursor()

    def execute(self, sql):
        self._cursor.execute(sql)
        return self._cursor.rowcount, self._cursor.fetchall()

    def commit(self):
        self._conn.commit()

    def close(self):
        self._cursor.close
        self._conn.close()
'''
#-----------------------------------------------------------------------------------------
