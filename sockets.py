import socket
#ipv4 tcp, DGRAM is upd
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
port = 9999
def do_server():
  tcp.bind((host, port))
  tcp.listen(5)
  print("Listening...")
  while True:
    csocket, addr = tcp.accept()
    print(f"Client connected: {addr}")
    msg = "Thanks for connecting".encode("ascii")
    csocket.send(msg)
    csocket.close()
def do_client():
  tcp.connect((host, port))
  msg = tcp.recv(1024)
  tcp.close()
  print(f"Received message: {msg.decode('ascii')}")
choice = input("Client or Server?")
if choice in "client":
  do_client()
else:
  do_server()