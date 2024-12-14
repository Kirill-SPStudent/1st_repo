from Address import Address
from Mailing import Mailing

to_address = Address("221133", "Москва", "Ленина", "25", "20")

from_address = Address("221144", "Новосибирск", "Красный проспект", "230", "5")

mail_1 = Mailing(to_address, from_address, "2000", "2222222")

print(mail_1)
