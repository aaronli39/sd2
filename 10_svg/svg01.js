// Xiaojie(Aaron) Li
// SoftDev2 pd8
// K10 -- Ask Circles [Change || Die]
// 2019-03-13

var pic = document.getElementById("vimage");
var but = document.getElementById("but_clear");
// cant use offset due to firefox issues
var rect = pic.getBoundingClientRect();

// clear just removes all child nodes of the svg tag
var clear = (e) => {
    while (pic.firstChild) {
        pic.removeChild(pic.firstChild);
    }
}

var draw = (e) => {
    // default click creates new red circle
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", e.clientX - rect.left);
    c.setAttribute("cy", e.clientY - rect.top);
    c.setAttribute("r", 10);
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
}

// add the event listeners
pic.addEventListener("click", draw);
but.addEventListener("click", clear);