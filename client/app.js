let BASE_API = "http://localhost:5000/image"
function getMousePosition(canvas, event) {
    let rect = canvas.getBoundingClientRect();
    let x = event.clientX - rect.left;
    let y = event.clientY - rect.top;
    return [x, y]
}

let canvasElem = document.querySelector("canvas");

canvasElem.addEventListener("mousedown", function (e) {
    let loc = getMousePosition(canvasElem, e);
    console.log(loc);
    setTimeout(() => {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open("POST", BASE_API + "/click", false); // false for synchronous request
        xmlHttp.setRequestHeader("Content-type", "application/json");
        xmlHttp.send(JSON.stringify(loc));
    }, 300)
}); 