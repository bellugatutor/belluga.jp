import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

CARD_TYPE_CHOICES = (
    ('JCB', _('JCB')),
    ('MasterCard', _('MasterCard')),
    ('VISA', _('VISA')),
)

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
    # username, first_name, last_name, email, is_staff, is_active, date_joined
    # is_superuser, groups, user_permissions, password, last_login
    phone = models.CharField(_('phone number'), max_length=40, blank=True)

    # Credit card information
    card_type = models.CharField(_('credit card type'), max_length=100, blank=True, choices=CARD_TYPE_CHOICES)
    card_number = models.CharField(_('credit card number'), max_length=40, blank=True)
    card_name = models.CharField(_('name with card'), max_length=200, blank=True)
    expiration_date = models.DateField(_('expiration date'), null=True, blank=True)

    # for tutors
    is_tutor = models.BooleanField(_('is tutor'), default=False)
    nationality = models.CharField(_('nationality'), max_length=40, blank=True)
    speak_japanese = models.CharField(_('speak Japanese'), max_length=40, choices=SPEAK_JAPAN_CHOICES, default='yes')
    photo = models.ImageField(_('profile picture'), upload_to='accounts', blank=True)
    intro_text = models.CharField(_('profile(200 words or less)'), max_length=400, blank=True, help_text=_('It will show up on the search page.'))
    intro_text2 = models.CharField(_('profile(1000 words or less)'), max_length=2000, blank=True, help_text=_('It will show up on your profile page.'))
    intro_video = models.FileField(_('introductory video'), upload_to='accounts', blank=True)

    # Tutoring Preferences
    language = models.CharField(_('which language'), max_length=40, choices=LANGUAGE_CHOICES, default='English')
    hourly_rate = models.PositiveIntegerField(_('hourly rate'), choices=HOURLY_RATE_CHOICES, default=2000)

    def __unicode__(self):
        if self.first_name:
            return self.first_name
        return self.username

    @classmethod
    def get_tutors(cls):
        return User.objects.filter(is_tutor=True)

    @classmethod
    def get_students(cls):
        return User.objects.filter(is_tutor=False)

    def get_sessions(self):
        if self.is_tutor:
            return self.gave_sessions.all()
        else:
            return self.got_sessions.all()

    def get_reviews(self):
        return []

    def get_stars(self):
        if not hasattr(self, 'stars'):
            self.stars = random.randint(1, 5)
        return range(self.stars)


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
