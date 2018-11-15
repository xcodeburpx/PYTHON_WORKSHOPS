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


# Echo TCP Server
if args.server:

    # Tworzymy socket
    sock = socket.socket(
        socket.AF_INET,     # <- Sygnalizujemy, że chcemy połączyć się za pomocą IPv4
        socket.SOCK_STREAM  # <- Chcemy użyć procesu z protokołem TCP
    )

    # Pobierz informację o hoście i porcie
    host = args.host
    port = args.port

    server_address = (host, port)

    print('starting up on %s port %s' % server_address)

    # Informujemy system, że będziemy używać takiej kombinacji
    sock.bind(server_address)


    # Nasłuchujemy połączenia
    sock.listen(1)

    while True:
        # Oczekujemy na połączenie
        print('waiting for a connection')
        connection, client_address = sock.accept()

        # Jeśli będzie połączenie -> odbieramy dane
        try:
            print("connection from", client_address)

            while True:
                data = connection.recv(4096)  # <- odbieramy 16 bajtów danych
                data = data.decode("utf-8") # <- dekodujemy bajty do Unicode
                # Jeśli przesłane są dane -> odsyłamy spowrotem
                if data:
                    print("Received data: %s" % data)
                    data = input("Say something: ")
                    data = data.encode("utf-8")
                    connection.sendall(data)
                else:
                    print("no data from", client_address)
                    break

        # Jeśli Ctrl+C -> zamknij program
        except KeyboardInterrupt:
            connection.close()
            sock.close()
            sys.exit(1)

        # Zamknij program
        finally:
            connection.close()
            sock.close()
            sys.exit()

# Echo TCP Client
if args.client:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = args.host
    port = args.port

    server_address = (host, port)

    print("connecting to %s port %s" % server_address)

    sock.connect(server_address)

    while True:
        try:
            while True:
                # Wysyłamy dane
                message = input("Say something: ")
                print('sending "%s"' % message)
                message = message.encode("utf-8")
                sock.sendall(message)

                data = sock.recv(4096)
                data = data.decode("utf-8")
                print('received "%s"' % data)

        except KeyboardInterrupt:
            sock.close()
            sys.exit()
        finally:
            print('closing socket')
            sock.close()
            sys.exit()
