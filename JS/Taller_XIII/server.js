var net = require('net');
var streamSet = require('stream-set');

var clients = streamSet();

var server = net.createServer( socket => {
    console.log("new client connected");
    // Proceso de replicacion del mensaje a los nodos que esten dentro del grupo
    // importante el servidor abre un proceso independiente por cada cliente
    clients.forEach(client => {
        socket.on('data', data =>{
            client.write(data);
        });
        client.on('data', data => {
            socket.write(data);
        })
    }); 
    clients.add(socket);
});

server.listen(10000);