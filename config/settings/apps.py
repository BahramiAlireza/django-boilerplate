from base import env

INSTALLED_PACKAGES = env.list("INSTALLED_APPS")

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.forms",
]


THIRD_PARTY_APPS = []

if "crispy_forms" in INSTALLED_PACKAGES:
    THIRD_PARTY_APPS += ["crispy_forms", "crispy_bootstrap5"]

if "allauth" in INSTALLED_PACKAGES:
    THIRD_PARTY_APPS += [
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
    ]

if "rest_framework" in INSTALLED_PACKAGES:
    THIRD_PARTY_APPS += [
        "rest_framework",
        "rest_framework.authtoken",
    ]

if "corsheaders" in INSTALLED_PACKAGES:
    THIRD_PARTY_APPS += ["corsheaders"]

if "drf_spectacular" in INSTALLED_PACKAGES:
    THIRD_PARTY_APPS += ["drf_spectacular"]


LOCAL_APPS = [
    "core.users",
]


# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
