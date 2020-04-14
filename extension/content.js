'use strict'

chrome.runtime.onMessage.addListener((message,sender,sendResponse) => {
    const para = document.getElementsByTagName('p');
    for(var i=0 ;i<para.length ; i++)
        para[i].innerText = message.txt;
    console.log(message.txt);
});

