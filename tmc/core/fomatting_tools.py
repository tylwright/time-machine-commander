import re


def get_string_between(full_string, before_wanted, after_wanted):
    """

    :param full_string:
    :param before_wanted:
    :param after_wanted:
    :return:
    """
    return re.findall(r'{}(.*?){}'.format(before_wanted, after_wanted), str(full_string))


def get_string_after(full_string, before_wanted):
    """

    :param full_string:
    :param before_wanted:
    :return:
    """
    return str(full_string).split(before_wanted, 1)[1]
