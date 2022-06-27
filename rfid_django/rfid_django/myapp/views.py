from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import HttpResponse
from django.shortcuts import render  # 导入
from django.views.decorators.csrf import csrf_exempt
import pymysql
import json
# 数据库连接信息
SQL_user = "root"
SQL_passwd = "wsmnnmm"
SQL_db = "django_sql"

# 读取卡号


def card_read():
    # 建立数据库连接
    SQL_conn = pymysql.connect(
        host="localhost", port=3306, user=SQL_user, passwd=SQL_passwd, db=SQL_db)
    # 得到数据库操作游标
    SQL_cur = SQL_conn.cursor(cursor=pymysql.cursors.DictCursor)
    resdata = SQL_cur.execute("select * from t_nowcard  where id=1")
    SQL_conn.close()
    return SQL_cur.fetchone()["card"]

# 读取卡号


def card_check(SQL_cur, card):
    resdata = SQL_cur.execute("select * from t_dorm  where card='%s'" % card)
    if resdata == 0:
        return 1
    else:
        return 0

# 读取宿舍号


def card_read_dorm(SQL_cur, card):
    resdata = SQL_cur.execute("select * from t_dorm  where card='%s'" % card)
    if resdata == 0:
        return 0
    else:
        return SQL_cur.fetchone()["dorm"]

# 注册


def card_register(card, dorm):
    # 建立数据库连接
    SQL_conn = pymysql.connect(
        host="localhost", port=3306, user=SQL_user, passwd=SQL_passwd, db=SQL_db)
    # 得到数据库操作游标
    SQL_cur = SQL_conn.cursor(cursor=pymysql.cursors.DictCursor)

    res = card_check(SQL_cur, card)
    if res == 0:
        return "卡已经注册"

    strsql = "insert into t_dorm(card,dorm) " \
        "values('%s','%s')" % (card, dorm)
    SQL_cur.execute(strsql)
    SQL_conn.commit()

    SQL_conn.close()

    return "注册成功"

# 上报记录


def card_report(card, texts):
    # 建立数据库连接
    SQL_conn = pymysql.connect(
        host="localhost", port=3306, user=SQL_user, passwd=SQL_passwd, db=SQL_db)
    # 得到数据库操作游标
    SQL_cur = SQL_conn.cursor(cursor=pymysql.cursors.DictCursor)

    res = card_check(SQL_cur, card)
    if res == 1:
        return "卡还没有注册"

    dorm = card_read_dorm(SQL_cur, card)

    strsql = "insert into t_record(card,dorm,text,time) " \
        "values('%s','%s','%s',now())" % (card, dorm, texts)
    SQL_cur.execute(strsql)
    SQL_conn.commit()

    SQL_conn.close()

    return "上传成功"

# 查询记录


def card_record():
    # 建立数据库连接
    SQL_conn = pymysql.connect(
        host="localhost", port=3306, user=SQL_user, passwd=SQL_passwd, db=SQL_db)
    # 得到数据库操作游标
    SQL_cur = SQL_conn.cursor(cursor=pymysql.cursors.DictCursor)
    relist = []
    resdata = SQL_cur.execute(
        "select * from t_record order by time desc limit 0,50")
    for i in range(0, resdata):
        sobj = SQL_cur.fetchone()
        relist.append({"card": "%s" % sobj["card"], "dorm": "%s" % sobj["dorm"],
                      "text": "%s" % sobj["text"], "time": "%s" % str(sobj["time"])})

    SQL_conn.close()
    return relist


def test(requestx):
    return HttpResponse("xxxxxx my ok")


def getcarid(requestx):
    return HttpResponse(card_read())


@csrf_exempt
def my_register_post(requestx):
    jsstr = requestx.POST.get("rd", "{}")
    data_json = json.loads(jsstr)
    card = data_json["card"]
    dorm = data_json["dorm"]
    rstr = ""
    if card == "" or dorm == "":
        rstr = "输入不可为空"
    else:
        rstr = card_register(card, dorm)
    return HttpResponse(rstr)


@csrf_exempt
def my_report_post(requestx):
    jsstr = requestx.POST.get("rd", "{}")
    data_json = json.loads(jsstr)
    card = data_json["card"]
    texts = data_json["texts"]
    rstr = "---"
    if card == "" or texts == "":
        rstr = "输入不可为空"
    else:
        rstr = card_report(card, texts)
    return HttpResponse(rstr)


class Homeclass(View):
    def get(self, requestx):  # 当请求为get时进入
        # return HttpResponse(requestx.GET.get("gdax","无数据"))
        # return render(requestx, "home.html", {"dongx": 12})  # 返回文件
        return render(requestx, "home.html")  # 返回文件

    def post(self, requestx):  # 当请求为POST时进入
        return HttpResponse(requestx.POST.get("user", "无数据"))


class Registerclass(View):
    def get(self, requestx):  # 当请求为get时进入
        # return HttpResponse(requestx.GET.get("gdax","无数据"))
        # return render(requestx, "home.html", {"dongx": 12})  # 返回文件
        return render(requestx, "my_register.html")  # 返回文件

    def post(self, requestx):  # 当请求为POST时进入
        # return HttpResponse(requestx.POST.get("rd","无数据"))
        return "ok"


class Reportclass(View):
    def get(self, requestx):  # 当请求为get时进入
        # return HttpResponse(requestx.GET.get("gdax","无数据"))
        # return render(requestx, "home.html", {"dongx": 12})  # 返回文件
        return render(requestx, "my_report.html")  # 返回文件

    def post(self, requestx):  # 当请求为POST时进入
        return HttpResponse(requestx.POST.get("user", "无数据"))


class Recordclass(View):
    def get(self, requestx):  # 当请求为get时进入
        rlist = card_record()
        return render(requestx, "my_record.html", {"listxto": rlist})  # 返回文件

    def post(self, requestx):  # 当请求为POST时进入
        return HttpResponse(requestx.POST.get("user", "无数据"))
