from configparser import ConfigParser


def read_netatalk_afp_conf(method):
    """
    Return the contents of /etc/netatalk/afp.conf
    :param method:
        raw: Returns file as is
        parsed: Returns sections that are found in the file
    :return: /etc/netatalk/afp.conf configuration file
    """
    if method is "raw":
        with open('/etc/netatalk/afp.conf') as f:
            return "<br/>".join(f.read().split("\n"))
    else:
        c = ConfigParser()
        c.read('/etc/netatalk/afp.conf')
        return c.sections()


def read_netatalk_afpd_conf():
    """
    Return the contents of /etc/netatalk/afpd.conf
    :return: /etc/netatalk/afpd.conf configuration file
    """
    with open('/etc/netatalk/afpd.conf') as f:
        return "<br/>".join(f.read().split("\n"))


def read_netatalk_volumes_conf():
    """
    Return the contents of /etc/netatalk/AppleVolumes.default
    :return: /etc/netatalk/AppleVolumes.default configuration file
    """
    with open('/etc/netatalk/AppleVolumes.default') as f:
        return "<br/>".join(f.read().split("\n"))


def read_avahi_daemon_conf():
    """
    Return the contents of /etc/avahi/avahi-daemon.conf
    :return: /etc/avahi/avahi-daemon.conf configuration file
    """
    with open('/etc/avahi/avahi-daemon.conf') as f:
        return "<br/>".join(f.read().split("\n"))