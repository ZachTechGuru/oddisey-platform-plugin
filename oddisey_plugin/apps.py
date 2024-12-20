"""
oddisey_plugin Django application initialization.
"""

from django.apps import AppConfig


class OddiseyPluginConfig(AppConfig):
    """
    Configuration for the oddisey_plugin Django application.
    """

    name = 'oddisey_plugin'

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "oddisey",
                "regex": rf"oddisey/",
                "relative_path": "urls",
            },
        },
        "settings_config": {
            "lms.djangoapp": {
                "common": {"relative_path": "settings"},
                "test": {"relative_path": "settings"},
                "production": {"relative_path": "settings"},
            },
            "cms.djangoapp": {
                "common": {"relative_path": "settings"},
                "test": {"relative_path": "settings"},
                "production": {"relative_path": "settings"},
            },
        },
    }
