import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from onlinecourse.models import Course, Lesson, Question, Choice
from django.utils.timezone import now

# Create or get sample course
course, created = Course.objects.get_or_create(
    id=1,
    defaults={
        'name': 'Introduction to Python & Django',
        'description': 'Learn core concepts of Python and Django Web Framework',
        'pub_date': now().date()
    }
)

if created or course.lesson_set.count() == 0:
    # Add Lessons
    Lesson.objects.get_or_create(
        course=course,
        title='Django Overview',
        order=0,
        content='Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.'
    )
    Lesson.objects.get_or_create(
        course=course,
        title='Django Models & Views',
        order=1,
        content='Models define your data structure. Views handle business logic and templates render HTML.'
    )

    # Question 1
    q1, _ = Question.objects.get_or_create(
        course=course,
        content='What is Django?',
        grade=50
    )
    Choice.objects.get_or_create(question=q1, content='A Web framework', is_correct=True)
    Choice.objects.get_or_create(question=q1, content='A Movie', is_correct=False)

    # Question 2
    q2, _ = Question.objects.get_or_create(
        course=course,
        content='What is Django Model?',
        grade=50
    )
    Choice.objects.get_or_create(question=q2, content='The single, definitive source of information about your data', is_correct=True)
    Choice.objects.get_or_create(question=q2, content='A web framework', is_correct=False)
    Choice.objects.get_or_create(question=q2, content='Perform ORM for developers', is_correct=True)

    # Question 3
    q3, _ = Question.objects.get_or_create(
        course=course,
        content='What is Django View?',
        grade=50
    )
    Choice.objects.get_or_create(question=q3, content='Class-based view', is_correct=True)
    Choice.objects.get_or_create(question=q3, content='Function-based view', is_correct=True)
    Choice.objects.get_or_create(question=q3, content='It is a Controller', is_correct=False)

print(f"Sample data created successfully for Course ID: {course.id}")
