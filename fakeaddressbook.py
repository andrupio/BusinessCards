from faker import Faker
fake = Faker('pl_PL')
class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.contact_phone}'

    @property
    def contact_phone(self):
        return self.phone

    @property
    def label_length(self):
        return len(self.first_name + self.last_name)

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}, Label length = {self.label_length}")

class BusinessContact(BaseContact):
    def __init__(self, job, company, company_phone, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.job = job
        self.company = company
        self.company_phone = company_phone

    @property
    def contact_phone(self):
        return self.company_phone

def create_contacts(type, number):
    contacts = []
    if type == "base":
        for i in range(number):
            priv = BaseContact(first_name = fake.first_name(), last_name = fake.last_name(), phone = fake.phone_number(), email = fake.email())
            contacts.append(priv)
            print(priv.contact(), priv)
    elif type == "business":
        for i in range(number):
            bus = BusinessContact(first_name = fake.first_name(), last_name = fake.last_name(), phone = fake.phone_number(), email = fake.email(), job = fake.job(), company = fake.company(), company_phone = fake.phone_number())
            contacts.append(bus)
            print(bus.contact(), bus)
    return contacts

create_contacts("business", 2)

