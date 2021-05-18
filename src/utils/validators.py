import re


def is_correct_email(email: str) -> bool:
    if re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email):
        return True
    return False
