import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User
from onlinecourse.models import Instructor, Course, Lesson, Question, Choice
from django.utils.timezone import now

# 1. Add admin as Instructor
admin_user = User.objects.filter(username='admin').first()
if not admin_user:
    admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'p@ssword123')

instructor, _ = Instructor.objects.get_or_create(
    user=admin_user,
    defaults={
        'full_time': True,
        'total_learners': 0
    }
)

# 2. Add Course "Learning Django"
course, _ = Course.objects.get_or_create(
    name='Learning Django',
    defaults={
        'description': 'Django is an extremely popular and fully featured server-side web framework, written in Python',
        'pub_date': now().date(),
        'total_enrollment': 0
    }
)
course.instructors.add(instructor)

# 3. Add Lesson #1
lesson, _ = Lesson.objects.get_or_create(
    course=course,
    title='What is Django',
    defaults={
        'order': 0,
        'content': "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source."
    }
)

# 4. Add Test Question & Choices
question, _ = Question.objects.get_or_create(
    course=course,
    content='Is Django a Python framework',
    defaults={
        'grade': 100
    }
)

Choice.objects.get_or_create(question=question, content='Yes', defaults={'is_correct': True})
Choice.objects.get_or_create(question=question, content='No', defaults={'is_correct': False})

print("Task 4 Test Data created successfully!")
