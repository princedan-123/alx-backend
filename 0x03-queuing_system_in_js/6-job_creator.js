const kue = require('kue');

const push_notification_code = kue.createQueue();
const jobData = {
  phoneNumber: '090-234-456-470',
  message: 'Hello, welcome to obimaco enterprise!!!'
}
const job = push_notification_code.create('email', jobData)
job.save((error) => {
  if(!error) {
    console.log(`Notification job created: ${job.id}`);
  }
})
job.on('complete', () => {
  console.log('Notification job completed');
})
job.on('failed', () => {
  console.log('Notification job failed')
})
