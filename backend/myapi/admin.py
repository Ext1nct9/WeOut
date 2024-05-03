from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Event, Organizer
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('get_user_permissions',)

    def get_user_permissions(self, obj):
        return ", ".join([p.codename for p in obj.user_permissions.all()])
    get_user_permissions.short_description = 'User Permissions'


class OrganizerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('get_managed_events',)
    readonly_fields = ('get_managed_events',)
    def get_managed_events(self, obj):
        return ", ".join([e.title for e in obj.managed_events.all()])
    get_managed_events.short_description = 'Managed Events'
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'company', 'email', 'bio')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Events'), {'fields': ('get_managed_events',)}),
    )



class AdminSite(admin.AdminSite):
    site_header = "WeOut"
    site_title = "Admin Dashboard"
    index_title = "Admin Dashboard"

    def has_permission(self, request):
        return request.user.is_active and request.user.is_superuser
    
adminSite = AdminSite(name="adminSite")
adminSite.register(User, UserAdmin)
adminSite.register(Group)
adminSite.register(Organizer, OrganizerAdmin)
adminSite.register(Event)