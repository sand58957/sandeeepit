from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from apps.settings.models import websiteSetting, SeoSetting, headerFooterSetting

@receiver([post_save, post_delete], sender=websiteSetting)
def clear_website_settings_cache(sender, instance, **kwargs):
    cache.delete('website_settings')
    # Also clear other related caches just in case
    cache.delete('seo_settings')
    cache.delete('header_footer_settings')

@receiver([post_save, post_delete], sender=SeoSetting)
def clear_seo_settings_cache(sender, instance, **kwargs):
    cache.delete('seo_settings')

@receiver([post_save, post_delete], sender=headerFooterSetting)
def clear_header_footer_cache(sender, instance, **kwargs):
    cache.delete('header_footer_settings')
