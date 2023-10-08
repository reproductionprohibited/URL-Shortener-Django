import http

import django.test
import django.urls

import urls.forms
import urls.models


class StaticURLTests(django.test.TestCase):
    def test_url_endpoint_status(self) -> None:
        url = django.urls.reverse('urls:create_view')

        response = django.test.Client().get(url)
        self.assertEqual(
            response.status_code,
            http.HTTPStatus.OK,
            f'Expected: {http.HTTPStatus.OK}, '
            f'got: {response.status_code}, testcase: {url}',
        )


class URLCreateFormTests(django.test.TestCase):
    def setUp(self) -> None:
        self.url_form = urls.forms.URLForm()
        super(URLCreateFormTests, self).setUp()

    def test_target_url_label(self) -> None:
        target_url_label = self.url_form['target_url'].label
        self.assertEquals(target_url_label, 'Target url')


class URLCreateViewTests(django.test.TestCase):
    form_data = {
        'target_url': 'https://google.com',
    }

    def test_create_url(self) -> None:
        url = django.urls.reverse('urls:create_view')

        url_object_count = urls.models.URL.objects.count()

        django.test.Client().post(
            url,
            data=self.form_data,
        )

        self.assertEqual(urls.models.URL.objects.count(), url_object_count + 1)
