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

# fake.name()
# # 'Lucy Cechtelar'

# fake.address()
# # '426 Jordy Lodge
# #  Cartwrightshire, SC 88120-6700'

# fake.text()
# # 'Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi
# #  beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt
# #  amet quidem. Iusto deleniti cum autem ad quia aperiam.
# #  A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur qui
# #  quaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernatur
# #  voluptatem sit aliquam. Dolores voluptatum est.
# #  Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.
# #  Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.
# #  Et sint et. Ut ducimus quod nemo ab voluptatum.'
# for _ in range(10):
#    print(fake.name())
