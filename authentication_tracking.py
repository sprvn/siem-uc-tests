import functions.loggen as functions
import functions.helpers as helpers
import socket
import time
import sys


def excessive_authentication_attempts():
    number_of_logs = 10
    interval = 0.5

    daddr = '192.168.1.1'
    dport = 514

    from_ip = helpers.get_random_internal_ip()

    # Create a socket towards USM
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i in range(number_of_logs):

        # Construct a new message
        message = functions.gen_ssh_failure(
            from_ip=from_ip,
            ssh_user='kevgus_testing')

        time.sleep(interval)

        print("Sent: %s" % (message))
        sock.sendto(message.encode(), (daddr, dport))


def successful_after_bruteforce():
    number_of_unsuccessful = 20
    interval = 0.5

    daddr = '192.168.1.1'
    dport = 514

    from_ip = helpers.get_random_internal_ip()

    # Create a socket towards USM
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i in range(number_of_unsuccessful):

        # Construct a new message
        message = functions.gen_ssh_failure(
            from_ip=from_ip,
            ssh_user='kevgus_testing')

        time.sleep(interval)

        print("Sent: %s" % (message))
        sock.sendto(message.encode(), (daddr, dport))

    message = functions.gen_ssh_success(
        from_ip=from_ip,
        ssh_user='kevgus_testing')

    time.sleep(interval)

    print("Sent: %s" % (message))
    sock.sendto(message.encode(), (daddr, dport))

if __name__ == "__main__":
    functions_list = [
                      'Excessive authentication attempts',
                      'successful_after_bruteforce'
                     ]
    if(len(sys.argv) == 1):
        for index, value in enumerate(functions_list):
            print("%s: %s" % (index+1, value))
        sys.exit(0)

    try:
        id = int(sys.argv[1])
    except ValueError:
        print("Please enter an integer")
        sys.exit(1)

    if int(sys.argv[1]) == 1:
        excessive_authentication_attempts()
    elif int(sys.argv[1]) == 2:
        successful_after_bruteforce()
    else:
        print("Invalid id")
