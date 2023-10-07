import django.urls

import urls.views

app_name = 'urls'

urlpatterns = [
    django.urls.path(
        '',
        urls.views.URLCreateView.as_view(),
        name='create_view',
    ),
    django.urls.path(
        '<str:shortened_url>',
        urls.views.URLRedirectView.as_view(),
        name='redirect_view',
    ),
]
