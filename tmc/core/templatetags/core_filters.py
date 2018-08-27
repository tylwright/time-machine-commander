from django import template
from core.config_manager import read_netatalk_afp_conf, read_netatalk_afpd_conf, read_netatalk_volumes_conf, \
    read_avahi_daemon_conf


register = template.Library()


@register.filter(name='read_netatalk_afp_config')
def read_netatalk_afp_config(str):
    """
    Returns contents of /etc/netatalk/afp.conf
    :param str: None (given only to use filter in this way)
    :return: Contents of /etc/netatalk/afp.conf
    """
    return read_netatalk_afp_conf(method='raw')


@register.filter(name='read_netatalk_afpd_config')
def read_netatalk_afpd_config(str):
    """
    Returns contents of /etc/netatalk/afpd.conf
    :param str: None (given only to use filter in this way)
    :return: Contents of /etc/netatalk/afpd.conf
    """
    return read_netatalk_afpd_conf()


@register.filter(name='read_netatalk_volumes_config')
def read_netatalk_volumes_config(str):
    """
    Returns contents of /etc/netatalk/AppleVolumes.default
    :param str: None (given only to use filter in this way)
    :return: Contents of /etc/netatalk/AppleVolumes.default
    """
    return read_netatalk_volumes_conf()


@register.filter(name='read_avahi_daemon_config')
def read_avahi_daemon_config(str):
    """
    Returns contents of /etc/avahi/avahi-daemon.conf
    :param str: None (given only to use filter in this way)
    :return: Contents of /etc/avahi/avahi-daemon.conf
    """
    return read_avahi_daemon_conf()