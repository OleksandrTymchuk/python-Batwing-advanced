class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        lst = []
        for value in self.__dict__.values():
            lst.append(value)
        return lst.__repr__()


o_tymchuk = Profile('Oleksandr', 'Tymchuk', '123456789', 'Lutsk City',
                    'o.tymchuk@gmail.com', '06.10.2000', '21', 'male')
print(o_tymchuk)
