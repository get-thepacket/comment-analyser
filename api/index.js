const express = require('express');
const app = express();
const PORT = 3000;

app.use('/static',express.static(path.join(__dirname,'static')));

app.get('/api', (req,res) => {
    res.send('You are on API page.');
})

// app.get('/',(req,res) => {
    
// })

app.listen(PORT, () => console.log(`listening to port ${PORT}`));
