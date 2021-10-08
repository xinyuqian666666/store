'''
    中国工商银行账户管理系统：
        ICBC:
'''
import random
import DBUtils

# 1.准备一个数据库 和 银行名称
# bank = {}  # 空的数据库
'''
    {
        "张三":{
            account:s001,
            country:"中国"
        }，
        "李四":{

        }


    }

'''
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


# 2.入口程序
def welcome():
    print("*************************************")
    print("*      中国工商银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")

# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    # 1.判断数据库是狗已满
    sql = "select count(*) from user"
    param = []
    date = DBUtils.select(sql, param)
    if date[0][0] >= 100:
        return 3
    # 2.判断用户是否存在
    sql2 = "select * from user where username = %s"
    param2 = [username]
    date2 = DBUtils.select(sql2, param2)
    if len(date2) != 0:
        return 2
    # 3.正常开户
    sql3 = "insert into user  values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
    param3 = [account, username, password, country, province, street, gate, money, bank_name]
    DBUtils.update(sql3, param3)
    return 1

# 用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))  # 将输入金额转换成int类型
    # 随机产生8为数字
    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password, country, province, street, gate, money)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            ------------------------
        '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name))

def cunqian(account, cundejine):
    sql = "select * from user where account = %s"
    param = [account]
    username = DBUtils.select(sql, param)
    if account == username[0][0]:
        sql1 = "update user set money = money + %s where account = %s   "
        param1 = [int(cundejine),account]
        money = DBUtils.update(sql1, param1)
        return "存款成功！"
    else:
        return False

def quqian(account, password, qudejine):
    sql = "select * from user where account = %s"
    param = [account]
    username = DBUtils.select(sql, param)
    if account == username[0][0]:
        if password==username[0][2]:
            if int(qudejine) <= username[0][7]:
                sql1 = "update user set money = money - %s where account = %s and password = %s and %s <= money"
                param1 = [int(qudejine), account, password, int(qudejine)]
                money = DBUtils.update(sql1, param1)
                return "取款成功！"
            else:
                return 3
        else:
            return 2
    else:
        return 1

def zhuanzhang(account,account_1,password,zhuanchujine):
    sql = "select * from user where account = %s"
    param = [account]
    username = DBUtils.select(sql, param)
    sql1 = "select * from user where account = %s"
    param1 = [account_1]
    username1 = DBUtils.select(sql1, param1)
    if int(account) == username[0][0]:
        if int(account_1) == username1[0][0]:
            if password==username[0][2]:
                if int(zhuanchujine) <= username[0][7]:
                    sql2 = "update user set money = money - %s where account = %s and password = %s and %s <= money"
                    param2 = [int(zhuanchujine), account, password, int(zhuanchujine)]
                    money2 = DBUtils.update(sql2, param2)
                    sql3 = "update user set money = money + %s where account = %s "
                    param3 = [int(zhuanchujine), account_1, int(zhuanchujine)]
                    money3 = DBUtils.update(sql3, param3)
                    return "转账成功！"
                else:
                    return 3
            else:
                return 2
    else:
        return 1

def chaxun(account,password):
    sql = "select * from user where account = %s"
    param = [account]
    username = DBUtils.select(sql, param)
    if account == username[0][0]:
        if password==username[0][2]:
            return username
        else:
            print("密码输入错误")
    else:
        print("用户不存在")
    return

while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        account = int(input("请输入相应的账号："))
        cundejine = int(input("请输入想要存入的金额："))
        cunqiande = cunqian(account, cundejine)
        print(cunqiande)
    elif chose == "3":
        account = int(input("请输入相应的账号："))
        password = input("请输入相应的账号密码：")
        qudejine = int(input("请输入想要取出的金额："))
        quqiande = quqian(account, password, qudejine)
        print(quqiande)
    elif chose == "4":
        account = int(input("请输入相应的转出账号："))
        account_1 = int(input("请输入相应的转入账号："))
        password = input("请输入相应的转出账号密码：")
        zhuanchujine = int(input("请输入想要转出的金额："))
        zhuanqian = zhuanzhang(account, account_1, password, zhuanchujine)
        print(zhuanqian)
    elif chose == "5":
        account = int(input("请输入相应的账号："))
        password = input("请输入相应的账号密码：")
        chazhao = chaxun(account, password)
        print(chazhao)
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")








