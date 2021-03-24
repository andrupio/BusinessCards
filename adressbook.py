class person:
   def __init__(self, name, surname, company, position, email):
       self.name = name
       self.surname = surname
       self.company = company
       self.position = position
       self.email = email

list = []
list.append(person("Kenneth", "Anderson", "Chase Pitkin", "Punch card operator", "KennethPAnderson@rhyta.com"))
list.append(person("Sheri", "Robinson", "Child World", "Clerical supervisor", "SheriERobinson@rhyta.com"))
list.append(person("Greg", "Miller", "Nobil", "Credit authorizer", "GregRMiller@rhyta.com"))
list.append(person("Joseph", "London", "System Star", "Physicist", "JosephOLondon@rhyta.com"))
list.append(person("Robert", "Main", "Mr. D's IGA", "General superintendent", "RobertSMain@dayrep.com"))

for i in list:
    print(i.name,",", i.surname,",", i.email)

