import pytest


@pytest.mark.django_db
def test_create_ad(client, access_token, user, category):
    data = {
        "author": user.pk,
        "category": category.pk,
        "name": "Что-то тут",
        "price": 5000,
        "description": ""
    }

    expected_data = {
        "id": 1,
        "is_published": False,
        "name": "Что-то тут",
        "price": 5000,
        "description": "",
        "image": None,
        "author": user.pk,
        "category": category.pk
    }

    response = client.post("/ad/", data, HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 201
    assert response.data == expected_data
