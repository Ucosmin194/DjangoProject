from teacher.models import Teacher


def get_all_teachers(request):
    all_teachers = Teacher.objects.all()
    return {'teachers': all_teachers}
