import os
import pytest
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "faq_project.settings")

pytest_plugins = ["django"]

django.setup()