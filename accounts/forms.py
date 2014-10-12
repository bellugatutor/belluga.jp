from django import forms
from collections import OrderedDict
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm
from django.contrib.auth.forms import AuthenticationForm as LoginForm
from .models import User


class UserChangeForm(AuthUserChangeForm):

    class Meta:
        model = User
        fields = '__all__'


class AdminUserCreationForm(AuthUserCreationForm):

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class UserCreationForm(AdminUserCreationForm):

    class Meta(AdminUserCreationForm.Meta):
        fields = ('username', 'last_name', 'first_name', 'email', 'phone', 'card_type', 'card_number', 'card_name', 'expiration_date')

    def __init__(self, *args, **kwargs):
        super(AdminUserCreationForm, self).__init__(*args, **kwargs)
        new_fields = OrderedDict()
        first_fields = ('username', 'password1', 'password2')
        for field_name in first_fields:
            new_fields[field_name] = self.fields.pop(field_name)
        for field_name, field_value in self.fields.items():
            new_fields[field_name] = field_value
        self.fields = new_fields


class TutorCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
        fields += ('is_tutor', 'nationality', 'speak_japanese', 'photo', 'intro_text', 'intro_video', 'language', 'hourly_rate')
        widgets = {
            'is_tutor': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(TutorCreationForm, self).__init__(*args, **kwargs)
        self.fields['is_tutor'].initial = True
