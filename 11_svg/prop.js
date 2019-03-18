// Xiaojie(Aaron) Li
// SoftDev2 pd8
// K11 -- Ask Circles [Change || Die] ... While On The Go
// 2019-03-17

var pic = document.getElementById("vimage");
var but = document.getElementById("but_clear");
var move = document.getElementById("move");
var tele = document.getElementById("teleport");
// cant use offset due to firefox issues
var rect = pic.getBoundingClientRect();
var requestID, timeout;

// clear just removes all child nodes of the svg tag
var clear = (e) => { 
    pic.innerHTML = "";
    window.cancelAnimationFrame(requestID);
}

// animate
var ani = (e) => {
    window.cancelAnimationFrame(requestID);
    let i;
    let children = pic.children;
    for (i = 0; i < children.length; i++) {
        let circ = children[i];
        let r = circ.getAttribute("r");
        let cx = parseInt(circ.getAttribute("cx")) + parseInt(circ.getAttribute("vx"));
        let cy = parseInt(circ.getAttribute("cy")) + parseInt(circ.getAttribute("vy"));
        let vx = parseInt(circ.getAttribute("vx"));
        let vy = parseInt(circ.getAttribute("vy"));

        if (cx > pic.getAttribute("width") - r || cx < r) circ.setAttribute("vx", vx * -1);
        if (cy > pic.getAttribute("height") - r || cy < r) circ.setAttribute("vy", vy * -1);
        
        circ.setAttribute("cx", cx);
        circ.setAttribute("cy", cy);
    }
    requestID = window.requestAnimationFrame(ani);
};

var draw = (e) => {
    // default click creates new red circle
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", e.clientX - rect.left);
    c.setAttribute("cy", e.clientY - rect.top);
    c.setAttribute("r", 10);
    c.setAttribute("vx", 2);
    c.setAttribute("vy", 2);
    c.setAttribute("fill", "red");
    c.setAttribute("stroke", "black");

    // first click turns circle black, stops propogation
    c.addEventListener("click", (e) => {
        e.stopPropagation();
        c.setAttribute("fill", "black");

        // second listener removes circle and respawns
        // stops propagation so it wont trigger other events
        c.addEventListener("click", (e) => {
            e.stopPropagation();
            c.remove();
            var xcor = (Math.floor(Math.random() * (rect.width - 5)) + rect.left + 5);
            var ycor = (Math.floor(Math.random() * (rect.height - 5)) + rect.top + 5);
            c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            c.setAttribute("cx", xcor - rect.left);
            c.setAttribute("cy", ycor - rect.top);
            c.setAttribute("r", 10);
            c.setAttribute("fill", "red");
            c.setAttribute("stroke", "black");
            pic.appendChild(c);
        });
    });
    // add circle if normal click
    pic.appendChild(c);
};

// does the teleporting and random speed mod
var woosh = (e) => {
    window.cancelAnimationFrame(requestID);
    if (pic.children.length == 0) return;
    let i = [1, 2, 1, 3, 5, 7, 10];
    let spd = i[Math.floor(Math.random() * (i.length - 1))];
    let circ = pic.children[Math.floor(Math.random() * (pic.children.length))];
    console.log(circ.getAttribute("cx"));
    let r = circ.getAttribute("r");
    let cx = (Math.floor(Math.random() * (rect.width - 5)) + rect.left + 5);
    let cy = (Math.floor(Math.random() * (rect.height - 5)) + rect.top + 5);
    let vx = spd;
    let vy = spd;
    console.log(circ.getAttribute("vx"));
    circ.setAttribute("vx", spd);
    circ.setAttribute("vy", spd);
    if (cx + vx > pic.getAttribute("width") - r || cx + vx < r) circ.setAttribute("vx", vx * -1);
    if (cy + vy > pic.getAttribute("height") - r || cy + vy < r) circ.setAttribute("vy", vy * -1);
    
    circ.setAttribute("cx", cx - rect.left);
    circ.setAttribute("cy", cy - rect.top);
    
    requestID = window.requestAnimationFrame(ani);
    clearTimeout(timeout);
    timeout = setTimeout(function() {woosh();}, 1000);
    
};

// add the event listeners
pic.addEventListener("click", draw);
but.addEventListener("click", clear);
move.addEventListener("click", ani);
tele.addEventListener("click", woosh);