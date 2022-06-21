import pymysql

# 连接数据库
conn = pymysql.connect(user='root', password='199605', database='mysql')
cursor = conn.cursor()

# 创建user表
cursor.execute('create table text (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s
cursor.execute('insert into text (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount

conn.commit()
cursor.close()

# 查询
cursor = conn.cursor()
cursor.execute('select * from text where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()