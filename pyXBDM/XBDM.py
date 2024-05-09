import socket

class XBDM:
    def __init__(self, ip_addr):
        """
        Initializes XBDM with the given IP address and default port.

        USAGE: 
        """
        self.ip = ip_addr
        self.port = 730
        self.sock = None
        self.connected = False

    def connect(self):
        """
        Opens a connection to the XDK/RGH/JTAG.

        USAGE: 
        """
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.ip, self.port))
            self.connected = True
            print('Connected!')
        except Exception as e:
            print('Error connecting: ', e)

    def disconnect(self):
        """
        Closes the connection to the XDK/RGH/JTAG.

        USAGE: 
        """
        if self.connected:
            try:
                if self.sock:
                    self.sock.close()
                self.connected = False
                print('Disconnected!')
            except Exception as e:
                print('Error disconnecting: ', e)
        else:
            print('You are not connected to a console!')