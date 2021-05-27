import re


def is_valid_address(address):
    is_valid_ip = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", address)

    is_valid_dns = re.match("^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$", address)

    if is_valid_ip or is_valid_dns:
        return True
    else:
        return False


def get_private_ip_address():
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr


def option_handler(message_request, message_error, message_success, options, position_default ):
    selected = ""
    while str(selected).lower() not in [x.lower() for x in options]:
        print(message_request)
        selected = input()
        if (selected is None or selected == "") and position_default is not None and position_default < len(options):
            selected = options[position_default]
        if str(selected).lower() not in [x.lower() for x in options] and message_error is not None:
            print(message_error)
    if message_success is not None:
        print(message_success)
    return [x.lower() for x in options].index(str(selected).lower())

