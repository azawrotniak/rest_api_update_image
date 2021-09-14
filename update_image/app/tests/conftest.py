from django.contrib.auth.models import User

import pytest
from rest_framework.test import APIClient

from app.models import Person, Account


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def user():
    username = "user1"
    password = "bar"
    user = User.objects.create_user(username=username, password=password)
    return user


@pytest.fixture
def person_basic(user):
    account = Account.objects.create(name='Basic', size_small=200, size_large=400)
    person_basic = Person.objects.create(user=user, account=account)
    return person_basic


@pytest.fixture
def person_premium(user):
    account = Account.objects.create(name='Premium', size_small=200, size_large=400)
    person_premium = Person.objects.create(user=user, account=account)
    return person_premium


@pytest.fixture
def person_enterprise(user):
    account = Account.objects.create(name='Enterprise', size_small=200, size_large=400)
    person_enterprise = Person.objects.create(user=user, account=account)
    return person_enterprise



