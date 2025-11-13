from django.db.models import Manager, QuerySet


class ActiveObjectManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_deleted=False)
