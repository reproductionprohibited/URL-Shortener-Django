import django.db.models


class URLManager(django.db.models.Manager):
    def url_objects_by_shortened(
        self, shortened_url: str
    ) -> django.db.models.QuerySet:
        return self.get_queryset().filter(shortened_url=shortened_url)
