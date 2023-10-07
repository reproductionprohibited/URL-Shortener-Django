import debug_toolbar.urls

import django.conf
import django.contrib.admin
import django.urls


import urls.urls

urlpatterns = [
    django.urls.path('', django.urls.include(urls.urls)),
    django.urls.path('admin/', django.contrib.admin.site.urls),
]

if django.conf.settings.DEBUG:
    urlpatterns += [
        django.urls.path(
            '__debug__/',
            django.urls.include(debug_toolbar.urls),
        ),
    ]
