from django.contrib import admin

from page.models import SitePage, PageSection, NavigationLink, SubNavigationLink


@admin.register(SitePage)
class SitePageAdmin(admin.ModelAdmin):
    model = SitePage

@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    model = PageSection

@admin.register(NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    model = NavigationLink

@admin.register(SubNavigationLink)
class SubNavigationLinkAdmin(admin.ModelAdmin):
    model = SubNavigationLink