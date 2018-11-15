"""
    Pakiet socket.

    Socket programming is a way of connecting two nodes
    on a network to communicate with each other.
    One socket(node) listens on a particular port at an IP,
    while other socket reaches out to the other to form a connection.
    Server forms the listener socket while client reaches out to the server.

"""


import argparse
import socket
import sys

# Tworzymy parser argumentów
parser = argparse.ArgumentParser(description="Client/server program for simple socket connection")

# Potrzebny jest host
parser.add_argument("-H", "--host",
                    help="Host IP address",
                    required=True,
                    default="localhost")

# Potrzebny jest port
parser.add_argument("-p", "--port",
                    help="Port of the web server",
                    required=True,
                    type=int,
                    default=10000)

# Poinformuj, czy jesteś serverem
parser.add_argument("-S", "--server",
                    action="store_true",
                    help="Start program as a server")

# Poinformuj, czy jesteś klientem
parser.add_argument("-C", "--client",
                    action="store_true",
                    help="Start program as a client")


args = parser.parse_args()

# Nie możesz być jednocześnie klientem i serwerem
if args.server and args.client:
    print(type(args.port))
    print("ERROR: Program can't run as a server and a client"
          " simultaneously.")
    sys.exit(-1)


# Echo UDP Server
if args.server:

    # Tworzymy socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Pobierz informację o hoście i porcie
    host = args.host
    port = args.port

    server_address = (host, port)

    print('starting up on %s port %s' % server_address)

    # Informujemy system, że będziemy używać takiej kombinacji
    sock.bind(server_address)

    while True:
        try:
            # Oczekuj na wiadomość
            print("\nWaiting for receive message")
            data, address = sock.recvfrom(4096)
            print("received %s bytes from %s" % (len(data), address))

            data = data.decode("utf-8")

            # Wyślij dane
            if data:
                print("Message: %s" % data)
                data = data.encode("utf-8")
                sent = sock.sendto(data, address)
        except KeyboardInterrupt:
            sock.close()
            sys.exit()




# Echo TCP Client
if args.client:

    # Tworzymy socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Pobieramy info odnośnie hosta i portu
    host = args.host
    port = args.port

    server_address = (host, port)

    # Nasza wiadomość
    message = "This is a message. It will be repeated."


    try:
        # Wysyłamy dane
        print("sending %s" % message)
        message = message.encode("utf-8")
        sent = sock.sendto(message, server_address)


        # Odbieramy dane
        print("waiting to receive")
        data, server = sock.recvfrom(4096)
        data = data.decode("utf-8")
        print("received: %s" % data)

    except KeyboardInterrupt:
        sock.close()
        sys.exit()

    finally:
        print("closing socket")
        sock.close()
        sys.exit()


