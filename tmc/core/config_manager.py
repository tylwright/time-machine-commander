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
