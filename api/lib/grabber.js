'use strict'

const {google} = require('googleapis');
const config = require('../config.json');

const youtube = google.youtube({
    version : 'v3',
    auth : config.key
});

var grab = async (id) => {
    const param = {
        part : "snippet, replies",
        videoId : id
    }

    const res = await youtube.commentThreads.list(param);
    return res.data.items;

}

module.exports = {
    grab
}