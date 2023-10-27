#!/usr/bin/yarn dev
import { createClient } from "redis";  
import { print } from "redis";

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
})

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

const publishMessage = (message, time) => {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        client.publish('holberton school channel', message);
    }, time);
}

    publishMessage('Holberton school', 1000);
    publishMessage('Holberton', 2000);
    publishMessage('Holberton school', 3000);
    publishMessage('Holberton', 4000);
    publishMessage('Holberton school', 5000);
    publishMessage('Holberton', 6000);
