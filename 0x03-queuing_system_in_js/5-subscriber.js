const { createClient } = require('redis');

const redisClient = createClient();
redisClient.on('connect', () => {
    console.log('Redis client connected to the server');
})
redisClient.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
})
redisClient.subscribe('holberton school channel');
redisClient.on('message', (channel, message) => {
    if (message !== 'KILL_SERVER') {
        console.log(message);
    }
    else {
        console.log(message);
        redisClient.unsubscribe('holberton school channel');
        redisClient.quit();
    }
})