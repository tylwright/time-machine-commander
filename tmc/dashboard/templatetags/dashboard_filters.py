from django import template
from core.dependency_manager import netatalk_version, avahi_version


register = template.Library()


@register.filter(name='get_netatalk_version')
def get_netatalk_version(str):
    return netatalk_version()


@register.filter(name='get_avahi_version')
def get_avahi_version(str):
    return avahi_version()