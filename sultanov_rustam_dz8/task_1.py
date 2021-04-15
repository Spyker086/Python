import re


def email_parse(email):
    keys = ['username', 'domain']
    # try:
    pattern = r'\w+[@]\w+[.]\w+'
    # pattern = r'[^@]'
    email_re = re.compile(pattern)
    if email_re.findall(email):
        pattern2 = r'@'
        dict_email = dict(zip(keys ,re.split(pattern2, email)))
        return print(dict_email)
    else:
        print("Error: invalid email")


email_parse('spycer@yan*dex.ru')