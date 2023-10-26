#!/usr/bin/yarn dev
import { createClient } from "redis";
import { promisify } from 'util';

const client = createClient();

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', async () => {
    console.log('Redis client connected to the server');
    await main();
});

const setNewSchool = (schoolName, value) => {
    client.SET(schoolName, value, (error, reply) => {
        error ? console.log(error) : console.log(reply);
    });
}

const displaySchoolValue = async (schoolName) => {
   console.log(await promisify(client.GET).bind(client)(schoolName));
}

async function main () {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');