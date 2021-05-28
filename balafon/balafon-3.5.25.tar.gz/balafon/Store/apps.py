# -*- coding: utf-8 -*-
"""app configuration"""

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BalafonAppConfig(AppConfig):
    name = 'balafon.Store'
    verbose_name = _("Balafon Store")
