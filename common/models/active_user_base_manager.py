from django.contrib.auth.models import UserManager
from django.db.models import QuerySet


class ActiveUserBaseManager(UserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_deleted=False)
