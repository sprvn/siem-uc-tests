from time import time
from datetime import datetime


def gen_timestamp(date):
    return datetime.fromtimestamp(date).strftime('%b %d %H:%M:%S')


def gen_ssh_failure(
                    date=None,
                    log_source="172.24.24.194",
                    ssh_user="root",
                    from_ip="127.0.0.1",
                    port=22
                    ):
    if not date:
        date = gen_timestamp(time())

    return "<86>%s %s sshd[9033]: Failed password for %s from %s port %s ssh2" % (
        date,
        log_source,
        ssh_user,
        from_ip,
        port
    )


def gen_ssh_success(
                    date=None,
                    log_source="172.24.24.194",
                    ssh_user="root",
                    from_ip="127.0.0.1",
                    port=22
                    ):
    if not date:
        date = gen_timestamp(time())

    return "<86>%s %s sshd[9033]: Accepted keyboard-interactive/pam for %s from %s port %s ssh2" % (
        date,
        log_source,
        ssh_user,
        from_ip,
        port
    )
