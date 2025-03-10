import re

def normalize_phone(phone_number):
    
    cleaned_number = re.sub(r'\D', '', phone_number).strip()
    
    if cleaned_number.startswith('+380'):
        return cleaned_number
    
    return '+380' + cleaned_number[-9:]

raw_numbers = [
"abc067\\t12x3 45y67!",
"(0z95) 2@34-5#678\\n",
"+38A0 44 1B23 4C567",
"375D05$012%34567",
" +4 4(E050)12F3-3G2-34",
" 0H50I345J1234",
"(0K50)L888M99N00",
"3915O0-P111Q-22R-22",
" 3S7  02T0 U111 V22 W11   "
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів:", sanitized_numbers)