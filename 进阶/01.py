from enum import IntEnum


class StudentEnum(IntEnum):
	NAME, AGE, SEX, EMAIL = range(4)


s = ('jim', 16, 'male', 'jim8721@gmail.com')
t = (34, 'liushuo')
StudentEnum.NAME

s[StudentEnum.NAME]

from random import randint

d = {k: randint(60, 100) for k in 'abcdefgh'}
l = [(v, k) for k, v in d.items()]
list(zip(d.values(), d.keys()))

p = sorted(d.items(), key=lambda item: item[1], reverse=True)

p = sorted(d.items(), key=lambda item: item[0], reverse=True)

for i, (k, v) in enumerate(p, 1):
	print(i, k, v)

for i, (k, v) in enumerate(p, 1):
	d[k] = (i, v)
