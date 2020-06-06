const app = require('express')();
const port = 3000;

app.get('/', (req,res)=> {
    res.send('<h1>Hello World</h1>');
});

app.listen(port, ()=> console.log(`Listening to port ${port}`));