import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';
import express from 'express';

const app = express();
const client = createClient();
const queue = createQueue();
const HOST = '127.0.0.1';
const PORT = 1245;
let reservationEnabled = true;

// Redis client ops
/**
 * Sets the number of available seats from Redis
 * @param {number} number -
 */
function reserveSeat(number) {
  client.set('available_seats', number);
}

/**
 * Queries redis for number of available seats
 * @returns {number} number of available seats
 */
async function getCurrentAvailableSeats() {
  const getAsync = promisify(client.get).bind(client);
  const availableSeats = await getAsync('available_seats');
  return Number(availableSeats);
}

// Express app routes
/* Gets number of available seats */
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.send({ numberOfAvailableSeats: availableSeats });
});

/* Enqueues seat reservation process */
app.get('/reserve_seat', (_req, res) => {
  if (!reservationEnabled) {
    res.send({ status: 'Reservation are blocked' });
    return;
  }
  res.send({ status: 'Reservation in process' });
  const reserveSeatJob = queue.create('reserve_seat').save();
  reserveSeatJob.on('complete', () => {
    console.log(`Seat reservation job ${reserveSeatJob.id} completed`);
  });
  reserveSeatJob.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${reserveSeatJob.id} failed ${errorMessage}`);
  });
});

/* Processes seats reservation jobs */
app.get('/process', (_req, res) => {
  queue.process('reserve_seat', async (_job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    if (!availableSeats) {
      done(new Error('Not enough seats available'));
      return;
    }
    availableSeats -= 1;
    reserveSeat(availableSeats);
    if (!availableSeats) reservationEnabled = false;
    done();
  });
  res.send({ status: 'Queue processing' });
});

app.listen(PORT, HOST, () => {
  console.log(`Server is live at ${HOST}:${PORT}`);
});
