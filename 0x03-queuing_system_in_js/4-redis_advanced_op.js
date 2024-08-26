const redis = require('redis');

const client = redis.createClient();
client.on('connect', () => {
    console.log('Redis client connected to the server');
})
const school = {
    Portland: 50,
    Seattle: 80,
    'New York':20,
    Bogota:20,
    Cali:40,
    Paris:2
}
for (let field in school) {
    if(school.hasOwnProperty(field)) {
        client.hset('HolbertonSchools', field, school[field], redis.print)
    }
}
client.hgetall('HolbertonSchools', (err, data) => {
    if (err) {
        console.log(err);
    }
    console.log(data);
})
client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`)
  })