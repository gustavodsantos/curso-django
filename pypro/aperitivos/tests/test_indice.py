import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def videos(db):
    return baker.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


def test_link_video(resp, videos):
    for video in videos:
        video_link = reverse('aperitivos:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')


# def test_conteudo_video(resp, video):
#     assert_contains(resp,
#                     f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video.youtube_id}"')
