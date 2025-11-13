from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import CharField, EmailField
from django.utils.functional import classproperty

from common.models.active_user_base_manager import ActiveUserBaseManager
from common.models.model_base import ModelBase
from common.models.users_type import UsersType


class BaseUser(AbstractUser, ModelBase):

    first_name = CharField(max_length=150, verbose_name='Имя', blank=False)
    email = EmailField(max_length=150, verbose_name='Емейл', blank=False)

    user_type = CharField(
        max_length=30,
        choices=UsersType.choices,
        default=UsersType.NONE,
        verbose_name='Тип пользователя'
    )

    objects = ActiveUserBaseManager()
    objects_all = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        ordering = ['id']

    def __str__(self) -> str:
        return f'{self.username} {self.email}'

    @classproperty
    def is_company(self) -> bool:
        return self.user_type == UsersType.COMPANY

    @classproperty
    def is_personal_worker(self) -> bool:
        return self.user_type == UsersType.PERSONAL_WORKER

    @classproperty
    def is_client(self) -> bool:
        return self.user_type == UsersType.CLIENT

    @classproperty
    def is_moderator(self) -> bool:
        return self.user_type == UsersType.MODERATOR
