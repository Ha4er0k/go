from datetime import datetime as dtt

def get_days_from_today(date: str) -> int:
    try:
        war_date = dtt.strptime(date, "%Y-%m-%d")
        today_date = dtt.today()
        delta = today_date - war_date
        return delta.days
    except ValueError:
        raise ValueError("Неправильний формат дати.")
print(get_days_from_today("2022-2-24"))
#