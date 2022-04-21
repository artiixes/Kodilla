class card:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email
    def __str__(self):
        return f'{self.name} {self.surname} {self.company} {self.position} {self.email}'


class base_contact(card):
    def __init__(self, name, surname, company, position, email, phone_number):
        super().__init__(name, surname, company, position, email)
        self.phone_number = phone_number
        self._name_length = 0

    def contact(self):
        print("Kontakuję sie z " + str(self.phone_number))
    @property
    def name_length(self):
        return self._name_length
    @name_length.setter
    def name_length(self, length):
        length = len(self.name) + len(self.surname)
        self._name_length = length


class business_contact(card):
    def __init__(self, name, surname, company, position, email, business_phone_number):
        super().__init__(name, surname, company, position, email)
        self.business_phone_number = business_phone_number
        self._name_length = 0
    def contact(self):
        print("Kontakuję sie z " + str(self.business_phone_number))    
    @property
    def name_length(self):
        print(self._name_length)
        return self._name_length
    @name_length.setter
    def name_length(self, length):
        length = len(self.name) + len(self.surname)
        self._name_length = length
        print(self._name_length)

 
p = business_contact(name="Dawid", surname="Płosiński", email="dplosinski97@gmail.com", company="af", position="senior", business_phone_number=123456798)
p.name_length