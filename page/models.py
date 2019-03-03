from django.db import models

class NavigationLink(models.Model):
    name = models.CharField(max_length=255)
    page = models.ForeignKey("SitePage", null=True, on_delete=models.SET_NULL)

    display_order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("display_order", "name")
        verbose_name = "Navigation Link"
        verbose_name_plural = "Navigation Links"

class SubNavigationLink(models.Model):
    name = models.CharField(max_length=255)
    page = models.ForeignKey("SitePage", null=True, on_delete=models.CASCADE)

    display_order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("display_order", "name")
        verbose_name = ""
        verbose_name_plural = ""

class SitePage(models.Model):
    name = models.CharField(max_length=255, help_text="Label for your page")
    slug = models.SlugField(help_text="Stub on the end of your URL e.g. /about")

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Site Page"
        verbose_name_plural = "Site Pages"


class PageSection(models.Model):
    page = models.ForeignKey(SitePage, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, help_text="Label for section")
    content = models.TextField(max_length=100000, default="")

    display_order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} for {self.page.name}"

    class Meta:
        ordering = ("display_order", "name")
        verbose_name = "Page Section"
        verbose_name_plural = "Page Sections"