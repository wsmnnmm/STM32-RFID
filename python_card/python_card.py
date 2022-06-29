import pymysql
import serial

UART_COM = "COM4"

# 数据库连接信息
SQL_user = "root"
SQL_passwd = "wsmnnmm"
SQL_db = "django_sql"
# 数据库全局变量
SQL_conn = ""
SQL_cur = ""
# 建立数据库连接
SQL_conn = pymysql.connect(host="localhost", port=3306,
                           user=SQL_user, passwd=SQL_passwd, db=SQL_db)
# 得到数据库操作游标
SQL_cur = SQL_conn.cursor(cursor=pymysql.cursors.DictCursor)

# 添加用户信息


def card_add(card):
    global SQL_conn, SQL_cur
    SQL_conn.ping(reconnect=True)
    print("刷新卡号")
    strsql = "update t_nowcard set card='%s' where id=1" % (card)
    SQL_cur.execute(strsql)
    SQL_conn.commit()


# 串口对象
ruart_obj = ""

# 调用开启串口函数
ruart_obj = serial.Serial(
    port=UART_COM,  # 串口
    baudrate=int(115200),  # 波特率
    timeout=0.2,  # 超时时间
)
print("串口打开成功，等待刷卡")

while True:
    try:
        readv = ruart_obj.readall()
        if len(readv) > 0:
            rdata = readv.decode("utf8")
            print("收到卡号:", rdata)
            if(len(readv) == 8):
                card_add(rdata)
    except Exception as e:
        print("通信异常", e)
