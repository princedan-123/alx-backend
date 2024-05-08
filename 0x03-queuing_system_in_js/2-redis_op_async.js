import redis from 'redis'
import util from 'util'
const client =  redis.createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
})

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: error.messagge`)
})

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

const get = util.promisify(client.get).bind(client)
async function displaySchoolValue(schoolName) {
	await get(schoolName)
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
