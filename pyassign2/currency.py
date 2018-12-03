import random
from urllib.request import urlopen


"""
货币兑换模块 currency.py
输入用空格隔开的3个数据，分别为待兑换的货币A、希望兑换的货币B、A数量，返回B的数量
输入 "TEST" 测试整个模块
货币用三个大写字母的符号输入，支持输入相应符号查询是否支持该货币
输入 "TYPE" 打印所有支持货币的列表
输入 "RANDOM" 随机两个货币和金额兑换
输入 "BREAK" 停止运行

__author__ = 'yichen nie'
__pkuid__ = '1800011703'
__email__ = '1800011703@pku.edu.cn'
"""


# 货币列表和货币名称
currency_list = ['AED', 'AFN', 'ALL', 'AMD', 'ANG',
                 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
                 'BAM', 'BBD', 'BDT', 'BGN', 'BHD',
                 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
                 'BSD', 'BTC', 'BTN', 'BWP',  # BYR现在不再提供服务
                 'BZD', 'CAD', 'CDF', 'CHF', 'CLF',
                 'CLP', 'CNY', 'COP', 'CRC', 'CUC',
                 'CUP', 'CVE', 'CZK', 'DJF', 'DKK',
                 'DOP', 'DZD', 'EEK', 'EGP', 'ERN',
                 'ETB', 'EUR', 'FJD', 'FKP', 'GBP',
                 'GEL', 'GGP', 'GHS', 'GIP', 'GMD',
                 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL',
                 'HRK', 'HTG', 'HUF', 'IDR', 'ILS',
                 'IMP', 'INR', 'IQD', 'IRR', 'ISK',
                 'JEP', 'JMD', 'JOD', 'JPY', 'KES',
                 'KGS', 'KHR', 'KMF', 'KPW', 'KRW',
                 'KWD', 'KYD', 'KZT', 'LAK', 'LBP',
                 'LKR', 'LRD', 'LSL', 'LTL', 'LVL',
                 'LYD', 'MAD', 'MDL', 'MGA', 'MKD',
                 'MMK', 'MNT', 'MOP', 'MRO', 'MTL',
                 'MUR', 'MVR', 'MWK', 'MXN', 'MYR',
                 'MZN', 'NAD', 'NGN', 'NIO', 'NOK',
                 'NPR', 'NZD', 'OMR', 'PAB', 'PEN',
                 'PGK', 'PHP', 'PKR', 'PLN', 'PYG',
                 'QAR', 'RON', 'RSD', 'RUB', 'RWF',
                 'SAR', 'SBD', 'SCR', 'SDG', 'SEK',
                 'SGD', 'SHP', 'SLL', 'SOS', 'SRD',
                 'STD', 'SVC', 'SYP', 'SZL', 'THB',
                 'TJS', 'TMT', 'TND', 'TOP', 'TRY',
                 'TTD', 'TWD', 'TZS', 'UAH', 'UGX',
                 'USD', 'UYU', 'UZS', 'VEF', 'VND',
                 'VUV', 'WST', 'XAF', 'XAG', 'XAU',
                 'XCD', 'XDR', 'XOF', 'XPD', 'XPF',
                 'XPT', 'YER', 'ZAR', 'ZMK', 'ZMW',
                 'ZWL']


# 判断输入数据的合法性：长度为3
def test1(x):
    return len(x) == 3


# test1测试函数
def test_A():
    assert test1(['USD', 'CNY', '2.4'])
    assert not test1(['USD'])
    assert not test1([])


# 判断输入数据的合法性：转换前后的货币必须在货币列表中
def test2(x):
    return x[0] in currency_list


# test2测试函数
def test_B():
    assert test2(['USD', 'CNY', '2.4'])
    assert not test2(['usd', 'CNY', '2.4'])
    assert not test2(['', 'CNY', '2.4'])
    assert not test2(['1', 'CNY', '2.4'])


def test3(x):
    return x[1] in currency_list


# test3测试函数
def test_C():
    assert test3(['USD', 'CNY', '2.4'])
    assert not test3(['USD', 'cny', '2.4'])
    assert not test3(['USD', '', '2.4'])
    assert not test3(['USD', '1', '2.4'])


# 输入的数量必须可以转化为浮点数
def test4(x):
    try:
        float(x[2])
    except:
        return False
    else:
        return True


# test4测试函数
def test_D():
    assert test4(['USD', 'CNY', '2.4'])
    assert test4(['USD', 'CNY', '0'])
    assert not test4(['USD', 'CNY', 'a'])
    assert not test4(['USD', 'CNY', 'False'])
    assert not test4(['USD', 'CNY', ''])


# 输入合法性测试
def valid(x):
    if (test1(x) and test2(x) and test3(x) and test4(x)):
        return True
    else:
        return 'input invalid'


# valid测试函数
def test_E():
    assert valid(['USD', 'CNY', '2.4'])
    assert valid(['USD', 'CNY', '0'])
    assert valid(['USD', 'CNY']) == 'input invalid'
    assert valid(['CNY', '0']) == 'input invalid'
    assert valid(['usd', 'CNY', '0']) == 'input invalid'
    assert valid(['USD', 'cny', '0']) == 'input invalid'


# 请求汇率数据
def getdata(x):

    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' \
           + x[0] + '&to=' + x[1] \
           + '&amt=' + x[2]

    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')

    return jstr


# getdata测试函数
def test_F():
    data1 = '{ "from" : "2.5 United States Dollars", "to" : \
"2.1589225 Euros", "success" : true, "error" : "" }'
    data2 = '{ "from" : "2 United States Dollars", "to" : \
"2 United States Dollars", "success" : true, "error" : "" }'
    data3 = '{ "from" : "-2.5 United States Dollars", "to" : \
"-2.1589225 Euros", "success" : true, "error" : "" }'

    assert getdata(['USD', 'EUR', '2.5']) == data1
    assert getdata(['USD', 'USD', '2']) == data2
    assert getdata(['USD', 'EUR', '-2.5']) == data3


# 分割反馈数据，转成字典，取出"to"和"success"
def data_sep(s):

    data = getdata(s)
    # 如果直接用eval函数会报错true未定义变量，因此替换为'True'或'False'，eval函数得到布尔值
    data = data.replace('true', 'True')
    data = data.replace('false', 'False')
    data_dict = eval(data)
    data_list = [data_dict["to"], data_dict["success"]]

    return data_list


# data_sep测试函数
def test_G():
    assert data_sep(['USD', 'EUR', '2.5']) == \
        ["2.1589225 Euros", True]
    assert data_sep(['USD', 'USD', '2.5']) == \
        ["2.5 United States Dollars", True]
    assert data_sep(['USD', 'XXX', '2.5']) == \
        ["", False]


# 分割带空格的字符串，before_space返回字符串第一个空格前的字符串
def before_space(s):
    sep = s.split(' ')[0]
    return sep


# before_space测试函数
def test_H():
    assert before_space('1 2') == '1'
    assert before_space('1 2 3 4 5') == '1'


# after_space返回字符串第一个空格后第二个空格前的字符串
def after_space(s):
    sep = s.split(' ')[1]
    return sep


# after_space测试函数
def test_I():
    assert after_space('1 2') == '2'
    assert after_space('1 2 3 4 5') == '2'


# exchange函数 接收data_sep函数输出的数据，返回兑换货币数量
def exchange(currency_from, currency_to, amount_from):
    ds = data_sep([currency_from, currency_to, amount_from])
    To = ds[0]
    To = before_space(To)
    return To


# exchange测试函数
def test_J():
    assert exchange('USD', 'EUR', '2.5') == '2.1589225'
    assert exchange('USD', 'USD', '2') == '2'
    assert exchange('USD', 'EUR', '-2.5') == '-2.1589225'


# 总测试函数
def test_all():
    test_A()
    test_B()
    test_C()
    test_D()
    test_E()
    test_F()
    test_G()
    test_H()
    test_I()
    test_J()
    print("All tests passed")


# main
def main():

    print('input the currency on hand, the currency to \
convert to and the amount of currency to convert')
    print('use a space to separate each parameter')
    print('input "TYPE" to print supported currenct list')
    print('input "TEST" to test the module')
    print('input a code to check if it is supported')
    print('input "RANDOM" to choose two random currencies')
    print('input "BREAK" to stop \n\n')

    while True:

        data = list(map(str, input().split()))

        # 确定货币是否在支持列表
        if (len(data) == 1 and len(data[0]) == 3 and
                str.upper(data[0]) == data[0]):

            if data[0] in currency_list:
                print('supported')
            else:
                print('NOT supported')

        # 输入TYPE，打印支持货币列表
        elif data == ['TYPE']:
            print('currency supported: \n')

            for i in range(len(currency_list)):
                print("{:6}".format(currency_list[i]), end='\t')
                if i % 5 == 4:
                    print('\n')

        # 输入BREAK，停止程序
        elif data == ['BREAK']:
            break

        # 输入TEST，测试程序
        elif data == ['TEST']:
            test_all()

        # 输入RANDOM，随机货币
        elif data == ['RANDOM']:
            a = currency_list[random.randint(0, len(currency_list) - 1)]
            b = currency_list[random.randint(0, len(currency_list) - 1)]
            c = str(random.random())
            print('input = ' + a + ' ' + b + ' ' + c)
            print(exchange(a, b, c))

        # 非以上特殊输入，判断输入没有错误后，获取数据
        elif valid(data) == True:
            print(exchange(data[0], data[1], data[2]))

        # 否则不合法输入
        else:
            print(valid(data))

        # 结尾input another data
        print('input another data')
        print('\n')


if __name__ == "__main__":
    main()
