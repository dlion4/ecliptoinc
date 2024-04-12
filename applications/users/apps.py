import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "applications.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import applications.users.signals  # type: ignore # noqa: F401
