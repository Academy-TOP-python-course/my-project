class User:
    def __init__(self, id, name, email):
        self._id = id       # Приватный атрибут
        self._name = name   # Приватный атрибут
        self._email = email # Приватный атрибут

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def save(self):
        # Логика сохранения в базу данных
        print(f"Сохранение пользователя: {self.name}, email: {self.email}")

class Admin(User):
    def __init__(self, id, name, email, role):
        super().__init__(id, name, email)  # Вызов конструктора родительского класса
        self._role = role  # Приватный атрибут

    @property
    def role(self):
        return self._role

    def delete_user(self, user_id):
        # Логика удаления пользователя
        print(f"Администратор {self.name} удалил пользователя с id {user_id}")