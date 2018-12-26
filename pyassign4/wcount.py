#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Yichen Nie"
__pkuid__  = "1800011703"
__email__  = "1800011703@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def download():  # 或取数据

    url = sys.argv[1]
    try:
        doc = urlopen(url)
    except Exception as error:  # 捕获错误
        print(error)  # 打印错误代码
        return 'Error'  # 返回值'Error'
    else:
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode('utf-8')
    return jstr


def replace_dict(lines):

    li_lo = lines.lower()  # 转换大小写

    for i in illegal_symbol:  # 替换不合法字符
        li_lo = li_lo.replace(i, " ")

    li_lo = li_lo.split(' ')

    for i in li_lo:
        if i in dictionary and i != '':  # 除掉空串
            dictionary[i] += 1  # 字典计数+1
        else:
            dictionary[i] = 1  # 字典新建一个item


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, print out the topn (word count), each in one line. 
    """

    global illegal_symbol, dictionary
    illegal_symbol = ('\r', '\n', '--',
                      "'s", "'t", "'ll", "'re", "'d", "'ve", "'m",
                      '_', '#', '[', ']', '(', ')', '-',
                      '*', '!', ',', '.', ';', '"', ':',
                      "'", '/', '$', '%', '”', '»',
                      '|', '+', '1', '2', '3', '4',
                      '5', '6', '7', '8', '9', '0')  # 不合法字符
    dictionary = {}
    replace_dict(lines)
    d = sorted(dictionary.items(),  # 按出现次数从高到低排序
               key=lambda i:i[1], reverse=True)

    for counter in range(topn):
        print(d[counter][0], d[counter][1])

def main():
    lines = download()
    if lines != 'Error':  # 如果不返回错误
        if len(sys.argv) == 3:
            wcount(lines, int(sys.argv[2]))
        else:
            wcount(lines)


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If \
not given, will output top 10 words')
        sys.exit(1)

    main()
