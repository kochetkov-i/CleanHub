from django import template
from django.db.models.query import QuerySet

from common.models.model_base import ModelBase

register = template.Library()


@register.filter(name='field_verbose_name')
def get_field_verbose_name(obj: object, name: str) -> str:
    """
        Allow to take model field and use more readable verbose name.

        Example:
        <th class="col-md-1">{{ films|field_verbose_name:"name" }}</th>
        <th class="col-md-1">{{ films|field_verbose_name:"year" }}</th>
        <th class="col-md-1">{{ films|field_verbose_name:"rating" }}</th>
        """
    model_obj = get_model_object(obj)
    return model_obj.field_names.get(name, name)


def get_model_object(obj: object) -> ModelBase:
    if isinstance(obj, QuerySet):
        return obj.first()

    if isinstance(obj, list):
        first_obj = next(iter(obj), None)
        if isinstance(first_obj, ModelBase):
            return first_obj

    if isinstance(obj, ModelBase):
        return obj

    raise ValueError(f'Unsupported type of object: {type(obj)}')
