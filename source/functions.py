import platform


def is_win10():
    return platform.platform().find('Windows-10') != -1
