from faker import Faker
fake = Faker()
class person:
   def __init__(self, name, address, email):
       self.name = name
       self.address = address
       self.email = email

list = []
for i in range (5):
    list.append(person(fake.name(), fake.address(), fake.email()))

for i in list:
    print(i.name,",", i.address,",", i.email)
