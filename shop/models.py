from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField("category name", max_length=250, db_index=True)
    parent = models.ForeignKey(
        "Parent",
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


slug = models.SlugField("URL", max_length=250, unique=True, null=False, editable=True)
created_at = models.DateTimeField("", auto_now_add=True)


class Meta:
    unique_together = ["slug", "parent"]
    verbose_name = "category"
    verbose_name_plural = "categories"
