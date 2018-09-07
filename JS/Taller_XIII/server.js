const net = require('net');

const server = net.createServer((client)=>{
    console.log('client connected');
    client.on('end', () => {
        console.log('client disconnected');
    });
    client.on('data', (data) =>{
        client.write(data);
    });
    client.write('hello\r\n');
    client.pipe(client);
});
server.on('error', (err) => {
    throw err;
});
server.listen(6666, () => {
    console.log('server bound');
});