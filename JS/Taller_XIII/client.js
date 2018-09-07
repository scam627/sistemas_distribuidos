const net = require('net');
const client = net.createConnection({ port: 6666}, () => {
    console.log('conneted to server!');
    client.write('world\r\n');
});

process.stdin.on('data', function (data) {
    console.log(data.toString());
})

//client.on('data',(data) => {
//    console.log(data.toString());
//});

client.on('end',() => {
    console.log('disconnected from server');
});