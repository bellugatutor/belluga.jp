from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User, Time, Location, Session
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(AuthUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'email', 'phone')}),
        (_('Credit card'), {'fields': ('card_type', 'card_number', 'card_name', 'expiration_date')}),
        (_('Tutor info'), {'fields': ('nationality', 'speak_japanese', 'photo', 'intro_text', 'intro_video', 'language', 'hourly_rate')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, UserAdmin)

admin.site.register(Time)
admin.site.register(Location)
admin.site.register(Session)
