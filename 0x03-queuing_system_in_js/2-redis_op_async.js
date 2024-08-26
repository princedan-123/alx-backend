const redis = require('redis');
const { promisify } = require('util');
const createClient = redis.createClient;

const client = createClient();
const get = promisify(client.get).bind(client);
client.on('connect', () => {
  console.log('Redis client connected to the server');
})
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}
async function displaySchoolValue(schoolName) {
  try {
    const data = await get(schoolName);
    console.log(data);
  }
  catch(error) {
    console.log(error);
  }
}
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`)
})
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
