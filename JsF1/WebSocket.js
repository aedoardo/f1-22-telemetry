/*
 * Copyright (c) 2022.
 *
 * 25/12/22, 17:13, WebSocket.js created by Edoardo.
 */


const {Server} = require("socket.io");

io.on("connection", (socket) => {
    console.log("New client connected with id: " + socket.id);
})
