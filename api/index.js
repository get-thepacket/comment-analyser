const express = require('express');
const app = express();
const grabber = require('./lib/grabber');
const PORT = 3000;

app.use('/static',express.static(path.join(__dirname,'static')));

app.get('/api', (req,res) => {
    res.send('You are on API page.');
})

app.get('/api/data',async (req,res)=> {
    
});
// app.get('/',(req,res) => {
    
// })

app.listen(PORT, () => console.log(`listening to port ${PORT}`));
