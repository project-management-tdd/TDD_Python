import requests

NUM_OF_USERS = 100

url = 'https://randomuser.me/api/?format=json&results=' + str(NUM_OF_USERS) + '&inc=gender,name,location,phone,dob'

json_data = requests.get(url).json()


class User:
    def __init__(self, firstName, lastName, gender, age, phone):
        self.name = firstName
        self.name += ' '
        self.name += lastName
        self.gender = gender
        self.age = age
        self.phone = phone

    def __str__(self):
        return 'Name: %s\nGender: %s\nAge: %s\nPhone: %s\n' % (self.name, self.gender, self.age, self.phone)


class UsersList:
    def __init__(self, users):
        self.users = users



list = []

for i in range(0, NUM_OF_USERS - 1):
    firstName = json_data['results'][i]['name']['first']
    lastName = json_data['results'][i]['name']['last']
    gender = json_data['results'][i]['gender']
    age = json_data['results'][i]['dob']['age']
    phone = json_data['results'][i]['phone']
    user = User(firstName, lastName, gender, age, phone)
    list.append(user)

userData = UsersList(list)






