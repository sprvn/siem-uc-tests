from random import randrange
import sys
import socket
import struct
import pprint


def construct_ip_header(dest_addr, src_addr=('127.0.0.1', 35869)):
    ip_version = 4                    # IPv4
    ip_ihl = 5                        # Since no options are used
    ip_tos = 0                        # Routine service
    ip_tot_len = 0                    # Total length (ip header + data)
    ip_id = 65143                     # Random ID
    ip_flags = 0
    ip_ttl = 255
    ip_protocol = socket.IPPROTO_UDP  # 17
    ip_checksum = 0
    ip_src = socket.inet_aton(src_addr[0])
    ip_dest = socket.inet_aton(dest_addr[0])

    # Merge version and IHL into a byte
    ip_ver_ihl = (ip_version << 4) + ip_ihl
    ip_header = struct.pack('!BBHHHBBH4s4s',
                            ip_ver_ihl,
                            ip_tos,
                            ip_tot_len,
                            ip_id,
                            ip_flags,
                            ip_ttl,
                            ip_protocol,
                            ip_checksum,
                            ip_src,
                            ip_dest
                            )

    return ip_header


def construct_udp_header(data, dest_addr, src_addr=('127.0.0.1', 35869)):

    # Check the type of data
    if type(data) != bytes:
        data = bytes(data.encode('utf-8'))

    psh_protocol = socket.IPPROTO_UDP  # 17
    psh_src_ip = socket.inet_aton(src_addr[0])
    psh_dest_ip = socket.inet_aton(dest_addr[0])

    udp_src_port = src_addr[1]
    udp_dest_port = dest_addr[1]
    udp_length = 8 + len(data)
    udp_checksum = 0

    pseudo_header = struct.pack('!BBH', 0, psh_protocol, udp_length)
    pseudo_header = psh_src_ip + psh_dest_ip + pseudo_header

    # Construct temporary header for checksum computation
    udp_header = struct.pack('!4H', udp_src_port, udp_dest_port, udp_length, udp_checksum)
    udp_checksum = checksum_func(pseudo_header + udp_header + data)

    # Construct the real UDP header
    udp_header = struct.pack('!4H', udp_src_port, udp_dest_port, udp_length, udp_checksum)

    return udp_header


def checksum_func(data):
    checksum = 0
    data_len = len(data)
    if (data_len % 2) == 1:
        data_len += 1
        data += struct.pack('!B', 0)

    for i in range(0, len(data), 2):
        w = (data[i] << 8) + (data[i + 1])
        checksum += w

    checksum = (checksum >> 16) + (checksum & 0xFFFF)
    checksum = ~checksum & 0xFFFF
    return checksum


def send_udp(src, dst, data):

    if type(src) != tuple:
        src = (src, randrange(2000, 65000))
    if type(dst) != tuple:
        print("dst not a tuple")
        sys.exit()

    encoded_data = bytes(data.encode('utf-8'))
    udp_header = construct_udp_header(encoded_data, dst, src) 
    ip_header = construct_ip_header(dst, src)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        s.sendto(ip_header + udp_header + encoded_data, dst)
    except socket.error as msg:
        print("Failed: %s" % (msg))

if __name__ == '__main__':
    sys.exit(1)
