from multiprocessing.connection import Listener

listener = Listener(('localhost', 6000), authkey=b'secret password')
# listens to socket local 6000 url

running = True

while running:
    conn = listener.accept() 
    # Accept a connection.
    #   The socket must be bound to an address and listening for connections.
    #   The return value is a pair (conn, address)
    #   where conn is a new socket object usable to send and receive data on the connection,
    #   and address is the address bound to the socket on the other end of the connection.
    while True:
        msg = conn.recv() 
        # recieve message Receive data from the socket.
        #  The return value is a bytes object representing the data received.
        #  The maximum amount of data to be received at once is specified by bufsize.
        print(msg)
        #prints the message to shell window
        if msg == 'close':
            conn.close()
            #when recive close message from sotket close the connection
            running = False
            break
listener.close()
#close the listener