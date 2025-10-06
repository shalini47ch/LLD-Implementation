
class User:
    def __init__(self, user_id, name, email, phone):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._phone = phone
    
    def get_user_id(self):
        return self._user_id
    
    def get_name(self):
        return self._name 
    #similarly we can do for email and phone 
    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone
