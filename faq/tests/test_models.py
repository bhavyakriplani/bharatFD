import pytest
from rest_framework.test import APIClient
from faq.models import FAQ
from django.core.cache import cache

@pytest.mark.django_db
def test_create_faq():
    client = APIClient()
    data = {
        "question": "What is Python?",
        "answer": "Python is a programming language",
        "language": "en"
    }
    response = client.post("/api/faqs/", data, format="json")

    assert response.status_code == 201, f"Response: {response.content}"
    assert FAQ.objects.count() == 1
    assert FAQ.objects.first().question == "What is Python?"

@pytest.mark.django_db
def test_get_faqs():
    client = APIClient()
    FAQ.objects.all().delete()
    cache.clear()  
    
    FAQ.objects.create(question="What is Django?", answer="Django is a web framework", language="en")

    response = client.get("/api/faqs/", format="json")

    assert response.status_code == 200, f"Response: {response.content}"
    assert len(response.data) == 1

@pytest.mark.django_db
def test_update_faq():
    client = APIClient()
    faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework", language="en")


    data = {
        "question": "Updated Django?",
        "answer": "Updated Answer",
        "language": "en"
    }

    response = client.put(f"/api/faqs/{faq.id}/", data, format="json")

    assert response.status_code == 200, f"Response: {response.content}"
    faq.refresh_from_db()
    assert faq.question == "Updated Django?"

@pytest.mark.django_db
def test_delete_faq():
    client = APIClient()
    faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework", language="en")

    response = client.delete(f"/api/faqs/{faq.id}/")

    assert response.status_code == 204, f"Response: {response.content}"
    assert FAQ.objects.count() == 0