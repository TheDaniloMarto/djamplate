from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_the_status_code_of_the_index_view(client) -> None:
    response = client.get(reverse("core:index"))
    assert response.status_code == 200


def test_the_template_used_by_index_view(client) -> None:
    response = client.get(reverse("core:index"))
    assertTemplateUsed(response, "pages/index.html")
