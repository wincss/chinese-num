#coding=utf-8

from itertools import count

def get_chinese(num):
    digit = u'零一两三四五六七八九'
    subunit = [u'', u'十', u'百', u'千']
    unit = ((u'万' * n).replace(u'万万', u'亿')[::-1] for n in count(0))

    result = []

    addzero = False
    while num > 0:
        if addzero:
            result.append(digit[0])
        result.append(unit.next())
        subnum = num % 10000
        num = num / 10000

        digits = [int(b) for b in reversed(str(subnum))]
        digitandbase = zip(digits, subunit)
        hasnum = False
        lastzero = False
        for d, u in digitandbase:
            if d == 0:
                if hasnum and not lastzero:
                    result.append(digit[0])
                lastzero = True
            else:
                hasnum = True
                lastzero = False
                result.append(u)
                if d == 2 and (u == u'十' or u == u''):
                    result.append(u'二')
                else:
                    result.append(digit[d])
        addzero = len(digitandbase) < 4

        if result[-2:] == [u'十', u'一']:
            result.pop()

    return u''.join(reversed(result))

if __name__ == '__main__':
    while True:
        try:
            num = int(raw_input())
        except (ValueError, EOFError, KeyboardInterrupt):
            break
        print get_chinese(num)
