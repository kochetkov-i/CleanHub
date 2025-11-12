from django.db.models import BooleanField, DateTimeField, ForeignObjectRel, Manager, Model
from django.utils.functional import classproperty

from common.models.active_object_manager import ActiveObjectManager


class ModelBase(Model):
    is_deleted = BooleanField(default=False)
    time_create = DateTimeField(auto_now_add=True)
    time_update = DateTimeField(auto_now=True)

    objects = ActiveObjectManager()
    objects_all = Manager()

    class Meta:
        abstract = True

    @classproperty
    def field_names(cls) -> dict[str, str]:
        return {f.name: f.verbose_name for f in cls._meta.get_fields()
                if not isinstance(f, ForeignObjectRel)}
