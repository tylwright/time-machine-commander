import re


def get_string_between(full_string, before_wanted, after_wanted):
    """
    Returns a substring of the given string
    :param full_string: Full string that you wish to parse
    :param before_wanted: Text that occurs before the substring you wish to get
    :param after_wanted: Text that occurs after the substring you wish to get
    :return: Substring of given string
    :example:
        full_string = "this is a test"
        before_wanted = "this "
        after_wanted = " test"
        return = "is a"
    """
    return re.findall(r'{}(.*?){}'.format(before_wanted, after_wanted), str(full_string))


def get_string_after(full_string, before_wanted):
    """
    Returns a substring of the given string
    :param full_string: Full string that you wish to parse
    :param before_wanted: Text that occurs before the substring you wish to get
    :return: Substring of given string
    :example:
        full_string = "this is a test"
        before_wanted = "this is "
        return = "a test"
    """
    return str(full_string).split(before_wanted, 1)[1]
