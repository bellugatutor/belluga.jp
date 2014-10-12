from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

SPEAK_JAPAN_CHOICES = (
    ('yes', _('Yes')),
    ('a little', _('A little')),
    ('no', _('No')),
)

LANGUAGE_CHOICES = (
    ('English', _('English')),  # business conversation
    ('Chinese', _('Chinese')),
    ('Korean', _('Korean')),
)

HOURLY_RATE_CHOICES = [(i, str(i)+' JPY') for i in range(2000, 8500, 500)]


class User(AbstractUser):

    # basic info, for both students and turors
    # fields derived from AbstrackUser:
    # username, first_name, last_name, email, is_staff,is_active, date_joined
    # is_superuser, groups, user_permissions, password, last_login
    phone = models.CharField(_('phone number'), max_length=40, blank=True)

    # Credit card information
    card_type = models.CharField(_('credit card type'), max_length=100, blank=True)
    card_number = models.CharField(_('credit card number'), max_length=40, blank=True)
    card_name = models.CharField(_('name associated with card'), max_length=200, blank=True)
    expiration_date = models.DateField(_('expiration date'), null=True, blank=True)

    # for tutors
    is_tutor = models.BooleanField(_('is tutor'), default=False)
    nationality = models.CharField(_('nationality'), max_length=40, blank=True)
    speak_japanese = models.CharField(_('speak Japanese'), max_length=40, choices=SPEAK_JAPAN_CHOICES, default='yes')
    photo = models.ImageField(_('photo'), upload_to='accounts', blank=True)
    intro_text = models.TextField(_('introductory paragraph'), blank=True)
    intro_video = models.FileField(_('introductory video'), upload_to='accounts', blank=True)

    # Tutoring Preferences
    language = models.CharField(_('which language'), max_length=40, choices=LANGUAGE_CHOICES, default='English')
    hourly_rate = models.PositiveIntegerField(_('hourly rate'), choices=HOURLY_RATE_CHOICES, default=2000)

    def __unicode__(self):
        if self.last_name or self.first_name:
            return ' '.join([self.first_name, self.last_name])
        return self.username

    @classmethod
    def get_tutors(self):
        return User.objects.filter(is_tutor=True)

    @classmethod
    def get_students(self):
        return User.objects.filter(is_tutor=False)


class Time(models.Model):
    ''' totors' available time '''
    # time should be a start of a hour that can be booked one time
    tutor = models.ForeignKey(User)
    time = models.DateTimeField(_('time'))


class Location(models.Model):
    ''' tutors' available locations '''
    tutor = models.ForeignKey(User)
    location_name = models.CharField(_('location name'), max_length=500)


class Session(models.Model):
    ''' in a session student and tutor meet together '''
    student = models.ForeignKey(User, related_name='got_sessions')
    tutor = models.ForeignKey(User, related_name='gave_sessions')
    time = models.DateTimeField(_('time'))
    location_name = models.CharField(_('location name'), max_length=500)
    student_show = models.BooleanField('student show up', default=True)
    tutor_show = models.BooleanField('turor show up', default=True)
    hourly_rate = models.PositiveIntegerField(_('hourly rate'), blank=True)
