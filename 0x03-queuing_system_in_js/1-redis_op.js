const redis = require('redis');
const createClient = redis.createClient;

const client = createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
})
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}
function displaySchoolValue(schoolName) {
  client.get(schoolName, redis.print);
}
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`)
})
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
