from django import template
from core.config_manager import read_netatalk_afp_conf


register = template.Library()


@register.filter(name='read_netatalk_afp_config')
def read_netatalk_afp_config(str):
    """
    Returns contents of /etc/netatalk/afp.conf
    :param str: None (given only to use filter in this way)
    :return: Contents of /etc/netatalk/afp.conf
    """
    return read_netatalk_afp_conf(method='raw')
