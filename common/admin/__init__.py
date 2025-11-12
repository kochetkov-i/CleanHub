from django.contrib import admin

from common.admin.user_base_admin import UserBaseAdmin
from common.models.user_base import BaseUser

admin.site.register(BaseUser, UserBaseAdmin)
