class User:
    names_count = dict()

    def __init__(self, first_name: str, last_name: str):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.profile_name: str = self.get_profile_name()

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.profile_name})'

    @staticmethod
    def get_clean_name(name: str) -> str:
        return name.lower().replace(' ', '-')

    def get_profile_name(self) -> str:
        name = f'{self.get_clean_name(self.first_name)}_{self.get_clean_name(self.last_name)}'
        name_id = self.names_count.get(name, 0) + 1
        self.names_count[name] = name_id
        return f'{name}_{name_id}'


if __name__ == '__main__':
    us1 = User('Jan', 'Kowalski')
    print(us1)
    us2 = User('Jan', 'kowalski')
    print(us2)
    us3 = User('Adam', 'Nowak')
    print(us3)
