"""

"""


class Credit:
    def __init__(self, name, username, password):
        self.__name = name
        self.__username = username
        self.__password = password
        self.__website = None

    def set_name(self, name):
        assert name
        self.__name = name

    def set_username(self, username):
        assert username
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_website(self, website):
        self.__website = website

    def get_credit_info(self):
        return (self.__name, self.__username, self.__password, self.__website)

    def get_credit_name(self):
        return self.__name

    def get_credit_username(self):
        return self.__username

    def get_credit_password(self):
        return self.__password

    def get_credit_website(self):
        return self.__website

    def __str__(self):
        credit_info = "name:\t" + self.__name + '\n' \
                    + "username:\t" + self.__username + '\n' \
                    + "password:\t" + self.__password + '\n'
        if not self.__website:
            credit_info += "website:\t" + self.__website + '\n'
        return credit_info
