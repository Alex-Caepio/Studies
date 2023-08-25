import re


def validate_email(email):
    pattern = r"^[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}~]+(\.[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}~]+)*@([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]{2,63}\.[a-zA-Z]{2,63}$"

    if re.match(pattern, email):
        return True
    return False


email1 = "username@example.com"
email2 = "user.name@example.com"
email3 = "user.nam.e@example.com"

print(validate_email(email1))
print(validate_email(email2))
print(validate_email(email3))
