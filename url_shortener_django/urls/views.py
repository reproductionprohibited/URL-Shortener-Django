import datetime
import random
import string
from typing import Any

import django.conf
import django.contrib.messages
import django.http
import django.shortcuts
import django.views.generic

import urls.forms
import urls.models


SPECIAL_CHARS = '$-_.+!*(),'
URL_CHARS = (
    string.ascii_lowercase
    + string.ascii_uppercase
    + string.digits
    + SPECIAL_CHARS
)
SHUFFLED_CHARS = list(URL_CHARS)
random.shuffle(SHUFFLED_CHARS)
URL_CHARS = ''.join(SHUFFLED_CHARS)


def generate_short_url(length: int = 8) -> str:
    return ''.join([random.choice(SHUFFLED_CHARS) for _ in range(length)])


class URLCreateView(django.views.generic.CreateView):
    model = urls.models.URL
    form_class = urls.forms.URLForm
    template_name = 'urls/create.html'
    success_url = '/'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def form_valid(self, form: urls.forms.URLForm) -> django.http.HttpResponse:
        domain_name = django.conf.settings.DOMAIN_NAME
        url = form.save(commit=False)
        shortened_url = generate_short_url()
        duplicates = urls.models.URL.objects.url_objects_by_shortened(
            shortened_url
        )
        while len(duplicates) > 0:
            shortened_url = generate_short_url()
            duplicates = urls.models.URL.objects.url_objects_by_shortened(
                shortened_url
            )
            duplicate = duplicates[0]
            now = datetime.datetime().now()
            one_day_delta = datetime.timedelta(hours=24)
            if one_day_delta + duplicate.created_at <= now:
                duplicate.target_url = url.target_url
                duplicate.save()
                shortened_url = duplicate.shortened_url
        django.contrib.messages.add_message(
            self.request,
            django.contrib.messages.SUCCESS,
            f'Shortened url: {domain_name}/{shortened_url}',
        )
        url.shortened_url = shortened_url
        url.save()
        return super().form_valid(form)


class URLRedirectView(django.views.generic.RedirectView):
    def get_redirect_url(self, shortened_url: str) -> str | None:
        url = django.shortcuts.get_object_or_404(
            urls.models.URL,
            shortened_url=shortened_url,
        )
        return url.target_url
