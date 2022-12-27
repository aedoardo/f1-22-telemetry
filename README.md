# **F1-22 Telemetry**

This is an open source project which aims to provide a cool live-telemetry of the F1-22 Game.

The documentation of the packets and other stuff regarding the game are in the "Data Output from F1 22 v14.pdf" file.

The project is divided into three programs:

    - the UDP server, written in Python;
    - the WebSocket, written in Javascript with the socket.io library;
    - the website, written in typescript.
    
    
## UDP Server

It is the UDP socket which receives and handles the packets from the F1-22 game. The structure for each packet is documented
in the "Data Output from F1 22 v14.pdf" file. 

You can configure it simply by changing the port number and the host inside the `main.py` file:

```python
HOST, PORT = "192.168.56.1", 27222
```

Then, you can run the UDP server with the following command:

`python main.py`.

At the moment, the UDP server supports the following packets:

    - PacketLobbyInfo;
    - PacketParticipants;
    - PacketSessionHistory.
    
This server has multiple `Managers`:

    - the MainManager: it handles the data packet and it manages all the other Managers;
    - the BoardManager: it manages the drivers' board in real time (the best lap and sectors);
    - the ParticipantsManager: it manages the participants in the current game;
    - the SessionHistoryManager: it manages the session's history.
    
    
## WebSocket server
The WebSocket server uses the `socket.io` library. In order to run the WebSocket, you can use these commands:
    
    - npm install
    - npm run WebSocket.js
    
The UDP server emits events (see `self._webDispatch` in the `MainManager`) every `X` seconds, where `X` is the second value of the tuple
in each key of the `self._webDispatch` dictionary.


## Website

It uses `Next.js` as framework. You can run `yarn install` to install all the dependences. Then, you can use the command `yarn dev` to start the website.


# Development

The plan is to create a website which is able to handle all the telemetry of the game in real time.

At the moment, there is only the drivers board (_still to complete_).

### Drivers board

![MainBoard](https://i.gyazo.com/5dc1bbcde0208f44e788d23d3a236969.png)

This is the **Drivers Board** which receives an update every second.

**TODO LIST**:

- [X] Add drivers list to the board
- [X] Add sectors and best lap times to the board;
- [X] Add purple color for the best lap;
- [X] Add purple color for best sectors (among the best laps only!)
- [ ] Add purple color for best sectors **AMONG ALL THE LAPS**
- [ ] Add green color for sectors that are not the best in general
- [ ] Add team image
- [ ] Add current tyres in use
