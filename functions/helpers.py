from random import randrange


def get_random_internal_ip():
    return "192.168.%s.%s" % (randrange(2, 254), randrange(2, 254))
