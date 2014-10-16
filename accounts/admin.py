from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User, Time, Location, Session
from .forms import UserCreationForm, UserChangeForm
from django import forms

class UserAdmin(AuthUserAdmin):
    save_on_top = True
    add_form = UserCreationForm
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'email')}),
        (_('Tutor info'), {'fields': ('is_tutor', 'nationality', 'speak_japanese', 'photo', 'intro_text', 'intro_text2', 'language', 'hourly_rate', 'intro_video')}),
        (_('Credit card'), {'fields': ('card_type', 'card_number', 'card_name', 'expiration_date')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(UserAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ('intro_text', 'intro_text2'):
            formfield.widget = forms.Textarea({'style':'width:500px;height:50px'})
        return formfield

admin.site.register(User, UserAdmin)

admin.site.register(Time)
admin.site.register(Location)
admin.site.register(Session)
