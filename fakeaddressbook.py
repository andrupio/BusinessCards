from faker import Faker
fake = Faker()
class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

class BusinessContact(BaseContact):
   def __init__(self, job, company, phone_company, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.job = job
       self.company = company
       self.phone_company = phone_company
    #contact(3)
    @property
    def label_length(self):
        return len(self.first_name + self.last_name)

    def __str__(self):
        #return f'{self.first_name} {self.last_name} {self.email} {self.suma}'
         return f"{self.first_name} {self.last_name} {self.email} Suma długości imienia i nazwiska oddzielonych spacją = {self.suma}"


    def priv_contact(number):
        for i in range(number):
            first_name = fake.first_name()
            last_name = fake.last_name()
            job = fake.job()
            email = fake.email()
            print(f"Wybieram numer {first_name} {last_name}, {job}, {email}")

card = BaseContact(fake.first_name(), fake.last_name(), fake.job(), fake.email())
list = []
for i in range (5):
    list.append(BaseContact(fake.first_name(), fake.last_name(), fake.job(), fake.email()))

card1 = list[0]
card2 = list[1]
card3 = list[2]
card4 = list[3]
card5 = list[4]
cards = [card1, card2, card3, card4, card5]
print(card1, card2, card3, card4, card5)

#cards = [list]
by_first_name = sorted(cards, key=lambda BaseContact: BaseContact.first_name)
by_last_name = sorted(cards, key=lambda BaseContact: BaseContact.last_name)
by_email = sorted(cards, key=lambda BaseContact: BaseContact.email)



# print(by_first_name)
# print(by_last_name)
# print(by_email)

#print(by_first_name)
#print(cards)
# for i in list:
#     # print(by_first_name)
#     print(i.first_name,",", i.last_name, ",", i.email)
