import pymysql

import __init__

try:
    MYSQL = pymysql.connect(
        host=__init__.MYSQL_HOST,
        port=__init__.MYSQL_PORT,
        user=__init__.MYSQL_USER,
        password=__init__.MYSQL_PASSWORD,
        db=__init__.MYSQL_DBNAME,
        charset=__init__.MYSQL_CHARSET
    )
    CURSOR = MYSQL.cursor()
except BaseException:
    print('mysql连接失败')
