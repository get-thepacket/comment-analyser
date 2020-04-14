function setup(){
    noCanvas();
    let text = select('#text');
    text.input(() => {
        let params = {
            active : true,
            currentWindow : true
        };
        chrome.tabs.query(params, (tabs)=> {
        console.log(tabs);
        let msg = {
            txt : text.value()
        };
        chrome.tabs.sendMessage(tabs[0].id,msg);
        });
    });
}