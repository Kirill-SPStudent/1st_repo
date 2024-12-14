def month_to_season(month):
    if month in [1, 2, 12]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Такого месяца не существует"


if __name__ == "__main__":
    month = int(input("Введите номер месяца: "))
    season = month_to_season(month)
    print(f"{month}-й месяц относится к времени года {season}")
