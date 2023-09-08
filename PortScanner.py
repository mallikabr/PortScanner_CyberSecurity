import socket
import errno

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

target = input("[+] Enter Target IP:")   # Input Ip Address


def tcp_scanner(port):  # TCP port scan
    try:
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.connect((target, port))
        tcp_sock.close()
        return True
    except:
        return False


def udp_scanner(port):   # UDP port scan
    try:
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            udp_sock.sendto("Message".encode('utf_8'), (target, port))    # send data
            udp_sock.connect((target, port))
            udp_sock.settimeout(0.5)                   # Socket timeout
            data, address = udp_sock.recvfrom(1024)     # receive data
        except socket.timeout:
            udp_sock.close()
            return True
        except socket.error as socket_error:
            if socket_error == errno.ECONNREFUSED:      # connection refused error
                udp_sock.close()
                return False
        except Exception as e:
            udp_sock.close()
            return False
    except:
        return False


for portNumber in range(1, 1024):
    if tcp_scanner(portNumber):
        print('[*]Port', portNumber, '/tcp', 'isopen')       # display TCP open ports
    elif udp_scanner(portNumber):
        print('[*]Port', portNumber, '/udp', 'isopen')       # display UDP open ports