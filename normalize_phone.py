# import re

# def normalize_phone_numbers(text):
#     sanitized_numbers=[]
#     for phone in text:
#         # cleaned_number = re.sub(r'\D', '', phone)
#         cleaned_number = re.sub(r'[^0-9]', '', phone)
#         if not cleaned_number.startswith('+'):
#             if cleaned_number.startswith('380'):
#                 cleaned_number = '+' + cleaned_number
#                 sanitized_numbers.append(cleaned_number)
#         else:
#             cleaned_number = '+38' + cleaned_number
#             sanitized_numbers.append(cleaned_number)

#     return sanitized_numbers


# # phone_numbers = [
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11 asf  "


# phone_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# print(normalize_phone_numbers(phone_numbers))
from pathlib import Path
import sys

def main():
    if len(sys.argv) < 2:
        user_input=''
    else:
        user_input=sys.argv[1]
    path=Path(user_input)
    if path.exists():
        if path.is_dir():
            items=path.glob('**/*')
            for item in items:
                print(item)
        else:
            print(f"{path} is the file")
    else:
        print(f"{path} not exists")

if __name__ == '__main__':
    main()
