from happypass.exceptions import (CreditAddError, CreditUpdateError,
                                  CreditDeleteError)


class CreditManager(object):
    credit_dict = {}

    def __init__(self):
        self._load_all_credit()

    def _load_all_credit(self):
        pass

    def get_all_credits(self):
        return self.credit_dict

    def add_credit(self, credit):
        credits = self.credit_dict.get(credit.get_credit_name())
        if credits is None:
            credits = []
        for acredit in credits:
            if credit.get_credit_username() == acredit.get_credit_username():
                raise CreditAddError("This credit is exist")
        credits.append(credit)
        self.credit_dict[credit.get_credit_name()] = credits

    def update_credit(self, name, username, password=None, website=None):
        status = 0
        if not name:
            raise CreditUpdateError(
                "When update, the credit name cannot be none")
        if not name:
            raise CreditUpdateError(
                "when update, the credit username cannot be none")
        credits = self.credit_dict.get(name)
        if credits is not None:
            for credit in credits:
                if username == credit.get_credit_username():
                    if password is not None:
                        credit.set_password(password)
                        status = 1
                    if website is not None:
                        credit.set_website(website)
                        status = 1

        else:
            raise CreditUpdateError('No such credit name')

    def find(self, name=None, username=None, password=None, website=None):
        result = []
        options = []
        if name:
            options.append('name')
        if username:
            options.append('username')
        if password:
            options.append('password')
        if website:
            options.append('website')

        if not options:
            return []
        else:
            for name, credits in self.credit_dict.iteritems():
                for credit in credits:
                    for option in options:
                        if locals().get(option) \
                                != getattr(credit, 'get_credit_'+option)():
                            break
                    else:
                        result.append(credit)
            return result

    def delete(self, name, username=None):
        if not name:
            raise CreditDeleteError(
                'When delete, the credit name cannnot be none')
        credits = self.credit_dict.get(name)
        if not credits:
            return
        else:
            if not username:
                credits = self.credits_dict.pop(name)
                return credits
            else:
                for credit in credits:
                    if credit.get_credit_username() == username:
                        credits.remove(credit)
                        if not credits:
                            self.credit_dict.pop(name)
                        return [credit]

credit_manager = CreditManager()
