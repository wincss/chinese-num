#coding=utf-8

from itertools import count, dropwhile

def get_chinese(num, alt_2=True):
    digit = u'零一二三四五六七八九'
    subunit = [u'', u'十', u'百', u'千']
    unit = ((u'万' * n).replace(u'万万', u'亿')[::-1] for n in count(0))
    alt_2_char = u'两'

    result = []

    while num > 0:
        subnum = int(num % 10000)
        num = num // 10000
        current_unit = next(unit)

        # 10000 -> 一万
        if subnum == 0:
            continue

        result.append(current_unit)
        digits = [int(b) for b in reversed(str(subnum))]
        dupzero = False
        for d, u in dropwhile(lambda x: x[0] == 0, zip(digits, subunit)):
            if d > 0:
                result.append(u)
            elif dupzero:
                # 3005 -> 三千零五
                continue
            else:
                dupzero = True

            if alt_2 and d == 2 and (u == subunit[3] or u == subunit[0] and current_unit):
                # 20220 -> 两万零二百二十
                result.append(alt_2_char)
            else:
                result.append(digit[d])

        if len(digits) < 4 and num > 0:
            # 20005 -> 两万零五
            result.append(digit[0])

        if digits[1:] == [1] and num == 0:
            # 10 -> 十
            result.pop()

    return u''.join(reversed(result))

if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass

    while True:
        try:
            num = int(input())
        except (ValueError, EOFError, KeyboardInterrupt):
            break
        print(get_chinese(num))
