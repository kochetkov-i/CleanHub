from django.contrib import admin


class UserBaseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'email', 'user_type',
                    'is_deleted', 'time_create', 'time_update')
    list_display_links = ('pk', 'first_name')
    search_fields = ('pk', 'first_name', 'email')
    list_editable = ('is_deleted',)
    list_filter = ('user_type', 'is_deleted', 'time_create', 'time_update')
    fields = ('first_name', 'email', 'user_type', 'is_deleted',
              'time_create', 'time_update', 'last_login', 'date_joined')
    readonly_fields = ('time_create', 'time_update',  'last_login', 'date_joined')
    save_on_top = True
