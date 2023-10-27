#!/usr/bin/yarn dev
import { createClient } from "redis";

const client = createClient();
const EXIT_MSG = 'KILL_SERVER';

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
    console.log(message);
    if (message === EXIT_MSG) {
        client.unsubscribe('holberton school channel');
        client.quit();
    }
});