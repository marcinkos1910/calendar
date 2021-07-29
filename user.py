import re


class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # self.name = f'{self.first_name} {self.last_name}'

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'          # regular expression
        if not re.match(regex, new_email):
            raise ValueError(f'Incorrect email address: {new_email}')
        self._email = new_email

    def __str__(self):
        return f'{self.name}'


# u = User("Marcin", "K", "a+@a.pl")
# print(u.name)
# u.first_name = "Janusz"
# print(u.name)
# print(u)
# u.name = "elo"
# "pawel@gmail.com"
# "pawel+python@gmail.com"
# "p.a.w.el+python2@gmail.com"
