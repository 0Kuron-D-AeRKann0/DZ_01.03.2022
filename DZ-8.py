import re


VALID_RE = re.compile(
    r"(?P<username>([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+)@(?P<domain>[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)")


def email_parse(email):
    """ validation of email """
    try:
        test = list(map(lambda x: x.groupdict(), VALID_RE.finditer(email)))
        print(test[0])
    except:
        raise ValueError from ValueError

import re

PARSE_RE = re.compile(
    r"""(?P<addres>^\S+)[\s-]*\[(?P<datatime>.*)\]\s*\"(?P<resp>\w*)\s*(?P<file>[/\w]+)[^\"]+\"\s+(?P<code>\d+)\s+(?P<size>\d+)""")

with open("./nginx_logs", "r", encoding="utf-8") as file:
    print(*(tuple(x.groupdict().values())
            for line in file for x in PARSE_RE.finditer(line)), sep="\n")

from functools import wraps


def type_logger(level=0):

    def logger(func):

        @wraps(func)
        def decor(*argv):


            if level > 0:

                return 'calc_cube(' + ", ".join([f"{func(x)}:{type(func(x))}" for x in argv]) + ")"

            else:

                return "calc_cube(" + ", ".join([str(func(x)) for x in argv]) + ")"

        return decor

    return logger


@ type_logger(2)
def calc_cube(x):
    """ cube of args """
    return x ** 3

from functools import wraps


def val_checker(func_filter):

    def checker(func):

        @wraps(func)
        def decor(x):

            if func_filter(x):
                return func(x)

            raise ValueError from ValueError

        return decor

    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3