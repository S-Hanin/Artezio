# -*- coding: utf8 -*-
"""
Напишите шаблон регулярного выражения, который соответствовал бы паролю,
состоящему из 8-12 символов, среди которых могут быть строчные и заглавные
буквы латинского алфавита, цифры, нижнее подчеркивание, звездочка,
процент и амперсанд. Пароль обязательно должен включать в себя одну строчную
букву, одну заглавную букву и одну цифру.
"""
import re


def is_password_in_rules(password: str):
    """
    Checks password conformity to restrictions
    """
    pattern = r"""(?=.*[0-9])   # at least one number
                  (?=.*[a-z])   # at least one lowercase letter
                  (?=.*[A-Z])   # at least one uppercase letter
                  [0-9a-zA-Z_*%&]{8,12}"""
    return bool(re.search(pattern, password, re.VERBOSE))


if __name__ == '__main__':
    print(f"'asdfghjk' is strong: {is_password_in_rules('asdfgh1A')}")
    print(f"'1Aasdfgh' is strong: {is_password_in_rules('1Aasdfgh')}")
    print(f"'1asdfghA' is strong: {is_password_in_rules('1asdfghA')}")
    print(f"'asdfghjk' is strong: {is_password_in_rules('asdfghjk')}")
