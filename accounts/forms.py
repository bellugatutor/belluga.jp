from django import forms
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
        fields = ('username', 'last_name', 'first_name', 'email', 'card_type', 'card_number', 'card_name', 'expiration_date')

    def __init__(self, *args, **kwargs):
        super(AdminUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True


class TutorCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
        fields += ('is_tutor', 'nationality', 'speak_japanese', 'photo', 'intro_text', 'intro_text2', 'intro_video', 'language', 'hourly_rate')
        widgets = {
            'is_tutor': forms.HiddenInput(),
            'intro_text': forms.Textarea(),
            'intro_text2': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(TutorCreationForm, self).__init__(*args, **kwargs)
        self.fields['is_tutor'].initial = True
        self.fields['photo'].required = True
        self.fields['nationality'].required = True
        self.fields['speak_japanese'].required = True
        self.fields['intro_text'].required = True
        self.fields['intro_text2'].required = True
        self.fields['language'].required = True
        self.fields['hourly_rate'].required = True


class TutorSearchForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('language', 'prefecture', 'area')
