# -*- coding: utf-8 -*-
import re
def structure(st):
    l = []
    for link in re.finditer(r"https://t.co/\w+(\s|$)",st):
        l.append(link.span())
    i = 0

    if len(l)==1:
        lt = [st[:l[0][0]]]
        lt.append(st[l[0][1]:])
    elif len(l)==0:
        return st
    else:
        lt = [st[:l[0][0]]]
        while i < (len(l) - 1):
            lt.append(st[(l[i][1]):l[i + 1][0]])
            i += 1
        lt.append(st[(l[i][1]):])
    st = "".join(lt)
    return st
