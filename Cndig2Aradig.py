# -*- coding: UTF-8 -*-
"""
Function:
convert chinese digits to arabic digits
Thought:
give the chinese digit order{'零': 0, '一': 1, '二': 1, '两': 1, '三': 1, '四': 1, '五': 1, '六': 1,
'七': 1, '八': 1, '九': 1, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000} ,
according the order,use recurrence method,divide the chinese digits into two parts,until every part has one
or two digits,then treat the sub part use the same recurrence

"""


# compute a chinese digit string to a arabic digit
def comput(cn_digits, common_used_numerals, order):
    # get the length of chinese digits
    i = len(cn_digits) - 1
    # if the length is zero, we return 1
    if len(cn_digits) == 0:
        return 1
    # if the length is 1 ,or length is 2 and the first digit is zero,we return the second digit directly
    elif len(cn_digits) == 1 or (len(cn_digits) == 2 and common_used_numerals[cn_digits[i-1]] == 0 and common_used_numerals[cn_digits[i]] > 0):
        return common_used_numerals.get(cn_digits[i])
    # if the length >=2 and the first is not zero,then divide it into two parts
    else:
        # search the i, that i-indexed digit 's order is high than the last digit
        while (i-1) >= 0 and order.get(cn_digits[i-1]) <= order.get(cn_digits[-1]):
            i -= 1
        # if all the digits'order before the last is lower than the last's(eg. 三百四十五万)，divide it into one part
        if i == 0:
            return int(comput(cn_digits[0:len(cn_digits) - 1], common_used_numerals, order)) * int(order.get(cn_digits[i - 1]))
        # if it's ordinary(eg. 三百四十万六千二百零一) ,we divide it into two parts
        else:
            return int(comput(cn_digits[0:i], common_used_numerals, order)) + int(comput(cn_digits[i:len(cn_digits)], common_used_numerals, order)) * 1


if __name__  == "__main__":
    order_tmp = {'零': 0, '一': 1, '二': 1, '两': 1, '三': 1, '四': 1, '五': 1, '六': 1, '七': 1,
                 '八': 1, '九': 1, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}

    common_used_numerals_tmp = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7,
                                '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
    common_used_numerals = {}
    order = {}
    for key in common_used_numerals_tmp:
        common_used_numerals[key.decode('utf-8')] = common_used_numerals_tmp[key]
        order[key.decode('utf-8')] = order_tmp[key]
    for x in ['零', '零一', '五', '十', '十五', '二十', '二十五', '九十九', '一百', '一百零二','二百五十',
              '二百五十六万', '二百五十六亿二百五十六万四千零三百零三', '一千零一十万']:
        print comput(x.decode('utf-8'), common_used_numerals, order),
