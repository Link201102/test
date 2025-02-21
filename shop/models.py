from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField("category_name", max_length=250, db_index=True)
    parent = models.ForeignKey(
        "Parent",
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        "URL", max_length=250, unique=True, null=False, editable=True
    )
    created_at = models.DateTimeField("", auto_now_add=True)

    class Meta:
        unique_together = ["slug", "parent"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Product", max_length=250, null=False, blank=False)
    price = models.FloatField("Price", null=False, blank=False)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    slug = models.SlugField("URL", unique=True, blank=False, null=False, max_length=250)

    image = models.ImageField("image", null=True, blank=True, upload_to="images/")

    created_at = models.DateTimeField("", auto_now_add=True)

    modified_at = models.DateTimeField("", auto_now=True)

    description = models.TextField("description", blank=True, null=True)

    Characteristics = models.ForeignKey(
        "Characteristics",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        pass


class Characteristics(models.Model):
    type = models.CharField("type", max_length=250, null=False, blank=False)

    country = models.CharField("country", max_length=250, null=False, blank=False)

    model = models.CharField("model", max_length=250, null=False, blank=False)

    code = models.CharField("code", max_length=250, null=False, blank=False)

    year = models.CharField("year", max_length=250, null=False, blank=False)

    material = models.CharField("material", max_length=250, null=False, blank=False)

    color = models.CharField("color", max_length=250, null=False, blank=False)

    size = models.CharField("size", max_length=250, null=False, blank=False)

    weight = models.CharField("weight", max_length=250, null=False, blank=False)

    class Meta:
        pass
