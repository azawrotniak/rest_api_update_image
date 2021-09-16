import pytest

from app.models import Image


def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_display_image_for_person_basic(client, user, person_basic):
    client.force_login(user)
    response = client.get('/images/')
    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_display_one_image_for_person_basic(client, user, person_basic):
    client.force_login(user)

    image_name = 'photo.jpg'
    Image.objects.create(image=image_name, user=person_basic)

    response = client.get('/images/')
    assert response.status_code == 200
    assert response.data == [{'image_small': 'example.com/media/cache/a0/0e/a00e726a82fedd80e68ad8b4cc442e01.jpg'}]


@pytest.mark.django_db
def test_display_image_for_person_premium(client, user, person_premium):
    client.force_login(user)
    response = client.get('/images/')
    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_display_one_image_for_person_premium(client, user, person_premium):
    client.force_login(user)

    image_name = 'photo.jpg'
    Image.objects.create(image=image_name, user=person_premium)

    response = client.get('/images/')
    assert response.status_code == 200
    assert response.data == [{'image_small': 'example.com/media/cache/a0/0e/a00e726a82fedd80e68ad8b4cc442e01.jpg', 
                                'image_large': 'example.com/media/cache/49/91/4991cec1eafcd70f126b5c851a23c941.jpg', 
                                'image_original': 'example.com/media/photo.jpg'
                            }]


@pytest.mark.django_db
def test_display_image_for_person_enterprise(client, user, person_enterprise):
    client.force_login(user)
    response = client.get('/images/')
    assert response.status_code == 200
    assert response.data == []