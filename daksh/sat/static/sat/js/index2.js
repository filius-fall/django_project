console.log("INDEX@@@@@@@")

const api_url = "ws://127.0.0.1:8080/sat/sat_api/v1/"

const ws_url = `ws://${window.location.host}/ws/socket-server`

const chatSocket = new WebSocket(ws_url)
chatSocket.onmessage = function(e){
    let data = JSON.parse(e.data)
    console.log(data)
}
