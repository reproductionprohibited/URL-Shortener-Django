import django.db.models

import urls.managers


class URL(django.db.models.Model):
    objects = urls.managers.URLManager()

    target_url = django.db.models.CharField(
        verbose_name='target url',
        max_length=1354,
    )

    shortened_url = django.db.models.CharField(
        verbose_name='shortened_url',
        max_length=8,
        unique=True,
    )

    created_at = django.db.models.DateTimeField(
        verbose_name='created at',
        auto_now_add=True,
    )
