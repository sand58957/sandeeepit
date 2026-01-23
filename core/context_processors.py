from django.conf import settings
from django.core.cache import cache
from apps.settings.models import *
from apps.accounts.models import UserProfile
from apps.menus.models import *
from apps.home.models import serviceSection, projectSection
from apps.contact.models import SubscriberFormTitle

# Website Setting Context
def website_settings_context(request):
    settings_obj = cache.get_or_set('website_settings', lambda: websiteSetting.objects.first(), 3600)
    return {'settings': settings_obj}

def seo_settings_context(request):
    seo_settings = cache.get_or_set('seo_settings', lambda: SeoSetting.objects.first(), 3600)
    return {'seo_settings': seo_settings}

def header_footer_context(request):
    header_footer = cache.get_or_set('header_footer_settings', lambda: headerFooterSetting.objects.first(), 3600)
    return {'header_footer': header_footer}

# Menu Context
def menu_data(request):
    primary_menus = cache.get_or_set('primary_menus', lambda: list(primaryMenu.objects.all()), 3600)
    sub_menus = cache.get_or_set('sub_menus', lambda: list(subMenu.objects.all()), 3600)

    return {
        'primary_menus': primary_menus,
        'sub_menus': sub_menus,
    }

## User Profile Context Processor
def user_profile_context(request):
    user_profile = None
    if request.user.is_authenticated:
        cache_key = f'user_profile_{request.user.id}'
        user_profile = cache.get_or_set(cache_key, lambda: UserProfile.objects.filter(user=request.user).first(), 3600)
    return {
        'user_profile': user_profile
    }

# Service Context Processor
def service_context(request):
    services = cache.get_or_set('fservices_all', lambda: list(serviceSection.objects.all()), 3600)
    return {
       'fservices': services,
    }

# Project Context Processor
def project_context(request):
    # Caching the random projects for 5 minutes instead of querying every time
    projects = cache.get_or_set('fprojects_random', lambda: list(projectSection.objects.all().order_by('?')[:6]), 300)
    return {
       'fprojects': projects,
    }

# Subscriber Form Title Context Processor
def subscriber_form_title_context(request):
    subscriber_form_title = cache.get_or_set('subscriber_form_title', lambda: SubscriberFormTitle.objects.first(), 3600)
    return {
       'subscriber_form_title': subscriber_form_title,
    }

## Demo Mode Template Context Proccessor
def demo_mode_enabled(request):
    return {'demo_mode_enabled': 'core.middleware.middleware.DemoModeMiddleware' in settings.MIDDLEWARE}