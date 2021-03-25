from faker import Faker
fake = Faker()
class person:
   def __init__(self, name, address, email):
       self.name = name
       self.address = address
       self.email = email
   def __str__(self):
       return f'{self.name} {self.address} {self.email}'

card = person(fake.name(), fake.address(), fake.email())
print(card)

# list = []
# for i in range (5):
#     list.append(person(fake.name(), fake.address(), fake.email()))

# for i in list:
#     print(i.name,",", i.address,",", i.email)
