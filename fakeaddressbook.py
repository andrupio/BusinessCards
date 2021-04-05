from faker import Faker
fake = Faker('pl_PL')
class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    @property
    def label_length(self):
        return len(self.first_name + self.last_name)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone} {self.email}'

    def contact(self):
        print(f'Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}, Label length = {self.label_length}')

class BusinessContact(BaseContact):
    def __init__(self, job, company, phone_company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.phone_company = phone_company

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone} {self.email} {self.job} {self.company} {self.phone_company} '

def create_contacts(type, number):
    if type == "base":
        for i in range(number):
            card = BaseContact(first_name = fake.first_name(), last_name = fake.last_name(), phone = fake.phone_number(), email = fake.email())
            print(card, card.contact())
    elif type == "business":
        for i in range(number):
            card = BusinessContact(first_name = fake.first_name(), last_name = fake.last_name(), phone = fake.phone_number(), email = fake.email(), job = fake.job(), company = fake.company(), phone_company = fake.phone_number())
            print(card, card.contact())

create_contacts("business", 5)

