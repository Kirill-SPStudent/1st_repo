from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Apple", "iPhone 7", "+79139990000")
phone2 = Smartphone("Nokia", "3310", "+79139990100")
phone3 = Smartphone("Sony", "ericsson w810i", "+79139990200")
phone4 = Smartphone("Samsung", "Galaxy  Note 5", "+79139990300")
phone5 = Smartphone("TECNO", "SPARK 9 pro", "+79139990400")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. - {phone.number}")
