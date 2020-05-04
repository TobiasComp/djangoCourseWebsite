import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
import django
django.setup()

import random
from faker import Faker
from first_app.models import User

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_first = fakegen.first_name()
        fake_second = fakegen.last_name()
        # fake_email = fakegen.email()
        password = fakegen.password()
        User.objects.get_or_create(first_name=fake_first, last_name=fake_second, password=password)


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('population complete!')
