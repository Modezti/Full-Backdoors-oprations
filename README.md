- 👋 Hi, I’m @Modezti
- 👀 I’m interested in python programming and ethical hacking
- 🌱 I’m currently learning python and kali linux

The server waits for client connections and displays a message when a connection is established.
Client (client.py)

The client.py script represents the client that connects to the server. Here's how to run the client:


python client.py

The client attempts to connect to the server using the specified IP address and port. It displays a message upon successful or failed connection.
Communication

Once the client is connected to the server, you can interact with the server via the client using a simple command-line interface. Here's how it works:

    When you run the client, it displays the shell>> prompt.
    You can enter commands to send to the server, e.g., cd <directory> to change the directory on the server.
    The server executes the received command and sends the response back to the client.
    The client displays the server's response.

    Example:


    Run the server (server.py) in one terminal window.
    Run the client (client.py) in another terminal window.
    In the client, enter a command, e.g., ls, and press Enter.
    The server executes the ls command, collects the output, and sends it back to the client.
    The client displays the server's output.

