from __future__ import unicode_literals

from django import __version__ as DJANGO_VERSION
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

from wagtaillinkchecker import urls
from wagtaillinkchecker import utils

if utils.is_wagtail_version_more_than_equal_to_2_0():
    from django import urls as urlresolvers
else:
    from django.core import urlresolvers

if utils.is_wagtail_version_more_than_equal_to_4_0():
    from wagtail.admin.menu import MenuItem
    from wagtail import hooks
elif utils.is_wagtail_version_more_than_equal_to_2_0():
    from wagtail.admin.menu import MenuItem
    from wagtail.core import hooks
else:
    from wagtail.wagtailadmin.menu import MenuItem
    from wagtail.wagtailcore import hooks


@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        path("link-checker/", include(urls)),
    ]


@hooks.register("register_settings_menu_item")
def register_menu_settings():
    return MenuItem(
        _("Link Checker"), urlresolvers.reverse("wagtaillinkchecker"), classnames="icon icon-link", order=300
    )
