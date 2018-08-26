import re
from core.shell_tools import run_command
from core.fomatting_tools import get_string_between, get_string_after


def netatalk_version():
    """
    Figures out which version of netatalk we're running
    :return: Version of netatalk (ex. 3.1.11)
    """
    cmd = "netatalk -v"
    output = get_string_between(run_command(cmd), "netatalk ", " - Netatalk")
    return output[0]


def avahi_version():
    """

    :return:
    """
    cmd = "avahi-daemon --version"
    output = get_string_after(run_command(cmd).decode("utf-8"), "avahi-daemon ")
    return output
