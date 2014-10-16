from .models import User, Session


def total_numbers(request):
    return {
        'total_students': User.get_students().count(),
        'total_tutors': User.get_tutors().count(),
        'total_lessons': Session.objects.all().count(),
    }
