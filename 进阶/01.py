from enum import IntEnum

class StudentEnum(IntEnum):
	NAME, AGE, SEX, EMAIL = range(4)
s = ('jim', 16, 'male', 'jim8721@gmail.com')
t = (34, 'liushuo')
StudentEnum.NAME

s[StudentEnum.NAME]

from random import randint