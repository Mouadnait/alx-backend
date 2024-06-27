#!/usr/bin/env node
// Create a queue with Kue
// Create a function named sendNotification:
//  - It will take two arguments phoneNumber and message
//  - It will log to the console "Sending notification to PHONE_NUMBER,
// with message: MESSAGE"
// Write the queue process that will listen to new jobs on 
// push_notification_code:
//  - Every new job should call the sendNotification function with the
// phone number and the message contained within the job data
import { createQueue } from 'kue';

// create the queue
const queue = createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};

// queue process that will listen to new jobs on push_notification_code
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

export default queue;
