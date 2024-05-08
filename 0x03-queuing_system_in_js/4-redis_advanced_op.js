import redis from 'redis'

const client =  redis.createClient();

client.on('connect', () => {
        console.log('Redis client connected to the server');
})

client.on('error', (error) => {
        console.log(`Redis client not connected to the server: error.messagge`)
})

let counter = 1;
const myMap = new Map([
	['Portland', '50'], ['Seattle', '80'], ['New York', '20'], ['Bogota', '20'],
	['Cali', '40'], ['Paris', '2']
])
for (let [key, value] of myMap) {
	client.hset('HolbertonSchools', key, value, redis.print)
}


client.hgetall('HolbertonSchools', (error, reply) => {
	if (error) {
		console.log(error)
	}
	console.log(reply);
});
