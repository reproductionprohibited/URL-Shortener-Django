import django.contrib.admin

import urls.models


@django.contrib.admin.register(urls.models.URL)
class URLAdmin(django.contrib.admin.ModelAdmin):
    list_display = [
        urls.models.URL.id.field.name,
        urls.models.URL.created_at.field.name,
    ]

    fields = [
        urls.models.URL.target_url.field.name,
        urls.models.URL.shortened_url.field.name,
    ]

    readonly_fields = [
        urls.models.URL.created_at.field.name,
    ]
