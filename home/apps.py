from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"


class ProfilePageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profile_page"
