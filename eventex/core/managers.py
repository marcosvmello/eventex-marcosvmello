from django.db import models


class KindQuerySet(models.QuerySet):
    def emails(self):
        return self.filter(Kind=self.model.EMAIL)

    def phones(self):
        return self.filter(Kind=self.model.PHONE)


class PeriodManager(models.Manager):
    pass
