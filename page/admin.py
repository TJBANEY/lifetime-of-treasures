from django.contrib import admin

from page.models import SitePage, PageSection

@admin.register(SitePage)
class SitePageAdmin(admin.ModelAdmin):
    model = SitePage

@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    model = PageSection