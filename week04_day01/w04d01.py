import datetime
from enum import Enum
from typing import Sequence, List, Dict


class Sex(Enum):
    FEMALE = 'F'
    MALE = 'M'
    OTHER = 'O'
    UNSPECIFIED = 'U'


class RelationType(Enum):
    UNKNOWN = 'UNKNOWN'
    INVITED = 'INVITED'
    FRIEND = 'FRIEND'


class Relation:
    def __init__(self, user1, user2, relation_type):
        self.user1 = user1
        self.user2 = user2
        self.relation_type = relation_type

    def __repr__(self):
        return f'Relation between {self.user1} and {self.user2} is {self.relation_type.name}'

    @classmethod
    def send_invitation(cls, user1, user2):
        relation = cls(user1, user2, RelationType.INVITED)
        user2.invitations[user1] = relation

    def accept_invitation(self):
        self.user2.invitations.pop(self.user1)
        self.relation_type = RelationType.FRIEND
        self.user2.friends[self.user1] = self
        self.user1.friends[self.user2] = self


class User:
    names_count = dict()

    def __init__(self, first_name: str, last_name: str, sex=Sex.UNSPECIFIED, date_of_birth: datetime.date=None):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.profile_name: str = self.get_profile_name()
        self.sex: Sex = sex
        self.date_of_birth: datetime.date = date_of_birth

        self.invitations: Dict[User, Relation] = {}
        self.friends: Dict[User, Relation] = {}

    def __repr__(self):
        return self.profile_name

    def full_data(self):
        str_data = f'{self.first_name} {self.last_name}'
        if self.sex != Sex.UNSPECIFIED:
            str_data += f' (sex={self.sex.name})'
        if self.date_of_birth is not None:
            date_as_str = self.date_of_birth.strftime("%Y.%m.%d")
            str_data += f' (date_of_birth={date_as_str})'
        return str_data

    @staticmethod
    def get_clean_name(name: str) -> str:
        return name.lower().replace(' ', '-')

    def get_profile_name(self) -> str:
        name = f'{self.get_clean_name(self.first_name)}_{self.get_clean_name(self.last_name)}'
        name_id = self.names_count.get(name, 0) + 1
        self.names_count[name] = name_id
        return f'{name}_{name_id}'

    def send_invitation(self, other_user):
        Relation.send_invitation(self, other_user)

    def accept_invitation(self, other_user):
        self.invitations[other_user].accept_invitation()


if __name__ == '__main__':
    us1 = User('Jan', 'Kowalski')
    print(us1)
    us2 = User('Jan', 'kowalski', sex=Sex.MALE, date_of_birth=datetime.date(year=1996, month=5, day=25))
    print(us2)
    us3 = User('Adam', 'Nowak', date_of_birth=datetime.date(year=1995, month=2, day=16))
    print(us3)
    print(us2.full_data())
    print(us3.full_data())

    us1.send_invitation(us2)
    us3.send_invitation(us2)

    us2.accept_invitation(us1)

    print(us2.invitations)
    print(us2.friends)
    print(us1.friends)
