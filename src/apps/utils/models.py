from django.db import models

class LogicDeletionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class LogicDeletionModel(models.Model):

    is_deleted = models.BooleanField(default=False)
    objects = LogicDeletionManager()

    def delete(self):
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True