import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^\d+]', '', phone_number.strip())
    
    if cleaned_number.startswith('+380'):
        return cleaned_number
    
    if cleaned_number.startswith('380'):
        return '+' + cleaned_number
    
    if cleaned_number.startswith('0'):
        return '+38' + cleaned_number
    
    return cleaned_number

raw_numbers = [
    "067\t123 4567",
    "(0%95) 234-5678\n",
    "+380 44 123 4567",
    "38050@1234567",
    "  +38(050)123-32-34",
    "  0503451234",
    "(050)8889$900",
    "38050-111-22-22",
    "38050 11&1 22 11   ",
    ]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів:", sanitized_numbers)
