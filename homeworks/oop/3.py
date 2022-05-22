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


o_tymchuk = Profile('Oleksandr', 'Tymchuk', '123456789', 'Lutsk City',
                            'o.tymchuk@gmail.com', '06.10.2000', '21', 'male')


print(o_tymchuk.__dict__)
print(f'Hello my name is {o_tymchuk.name} {o_tymchuk.last_name},'
      f' my phone number: {o_tymchuk.phone_number},'
      f' my address: {o_tymchuk.address},'
      f' my email: {o_tymchuk.email},'
      f' my date of birthday: {o_tymchuk.birthday},'
      f' im {o_tymchuk.age} year old'
      f' and im {o_tymchuk.sex}')
