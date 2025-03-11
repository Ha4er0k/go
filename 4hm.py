from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_difference = (birthday_this_year - today).days
        
        if 0 <= days_difference <= 7:
            if birthday_this_year.weekday() >= 5:  
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays


users = [
    {"name": "Alexander Ivanov", "birthday": "1990.07.10"},
    {"name": "Marina Petrov", "birthday": "1985.01.11"},
    {"name": "Igor Sidorov", "birthday": "1992.03.12"},
    {"name": "Natalie Kovalenko", "birthday": "1993.09.08"},
    {"name": "Vasyl Melnyk", "birthday": "1988.03.01"},
    {"name": "Elena Tkachenko", "birthday": "1995.03.17"},
    {"name": "Dmitry Shevchenko", "birthday": "1991.01.21"},
    {"name": "Anna Hrytsenko", "birthday": "1994.12.12"},
    {"name": "Serhiy Bondar", "birthday": "1987.07.07"},
    {"name": "Julia Moroz", "birthday": "1996.03.12"},
    {"name": "Pavlo Dmytrenko", "birthday": "1993.01.20"},
    {"name": "Katherine Zhuk", "birthday": "1992.05.30"},
    {"name": "Maxim Lysenko", "birthday": "1989.09.22"},
    {"name": "Svitlana Romanenko", "birthday": "1997.03.10"},
    {"name": "Andrew Kravchenko", "birthday": "1990.02.24"},
    {"name": "Oksana Polishchuk", "birthday": "1985.11.15"},
    {"name": "Eugene Havryliuk", "birthday": "1986.08.24"},
    {"name": "Tatiana Oliynyk", "birthday": "1994.03.15"},
    {"name": "Roman Stepanenko", "birthday": "1991.02.11"},
    {"name": "Inna Martynenko", "birthday": "1995.07.01"},
]


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
#