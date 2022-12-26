/*
 * Copyright (c) 2022.
 *
 * 25/12/22, 17:13, WebSocket.js created by Edoardo.
 */

const {Server} = require("socket.io");

const io = new Server({cors: {
    origin: "http://localhost:3000",
}});

io.on("connection", (socket) => {
    console.log("New client connected with id: " + socket.id);

    socket.on("send_board", (data) => {
        io.emit("send_board", data);
    })
});

io.listen(3001);