Base python2.7,but it's easy convert to python3.6
Function:
convert chinese digits to arabic digits
Thought:
give the chinese digit order{'零': 0, '一': 1, '二': 1, '两': 1, '三': 1, '四': 1, '五': 1, '六': 1,
'七': 1, '八': 1, '九': 1, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000} ,
according the order,use recurrence method,divide the chinese digits into two parts,until every part has one
or two digits,then treat the sub part use the same recurrence