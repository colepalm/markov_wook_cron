const cron = require('node-cron')
const { spawn } = require('child_process');

cron.schedule('* * * * *', () => {
    console.log('running a task every minute');
    const command = spawn('npm run test', {
        shell: true
    })

    command.stdout.on('data', data =>   console.log(data.toString()))
    command.stderr.on('data', data => console.error(data.toString()))
});
