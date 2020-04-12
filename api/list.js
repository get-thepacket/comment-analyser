'use strict'

const rp = require('request-promise');
const config = require('./config.json');
const {google} = require('googleapis');

const youtube = google.youtube({
    version : 'v3',
    auth : config.key
});

const testparams = {
    part : "snippet",
    q : "lucky one"
}

var testrun = async () => {
    const data = await youtube.search.list(testparams);
    console.log(data.data);
};

const param = {
    part : "snippet, replies",
    videoId : "T-p_-ueDBmU"
}

var comments = async () => {
    const res = await youtube.commentThreads.list(param);
    console.log(res.data.items[0].snippet.topLevelComment);
}

comments().catch(console.error);

// run().catch(console.error);
