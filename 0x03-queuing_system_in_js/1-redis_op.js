#!/usr/bin/yarn dev
import { createClient } from "redis";

const client = createClient();

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
    client.SET(schoolName, value, (error, reply) => {
        error ? console.log(error) : console.log(reply);
    });
}

const displaySchoolValue = (schoolName) => {
    client.GET(schoolName, (error, reply) => {
        error ? console.log(error) : console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');