from enum import unique

from django.db.models import TextChoices
from django.utils.functional import classproperty


@unique
class UsersType(TextChoices):
    NONE = '', '---------'

    # create by admin
    MODERATOR = 'moderator', 'Модератор'

    # can register
    COMPANY = 'company', 'Компания'
    PERSONAL_WORKER = 'personal_worker', 'Частный исполнитель'

    CLIENT = 'client', 'Клиент'

    @staticmethod
    def get_label(user_type: str) -> str:
        return UsersType(user_type).label

    @classproperty
    def user_types_registered(cls) -> list:
        return [cls.COMPANY, cls.PERSONAL_WORKER, cls.CLIENT]
