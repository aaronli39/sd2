// Xiaojie(Aaron) Li
// SoftDev2 pd8
// K09 -- Connect the Dots
// 2019-03-12

var pic = document.getElementById("vimage");
var but = document.getElementById("but_clear");
var pX = -1; // previous x
var pY = 0; // previous y

// clear just removes all child nodes of the svg tag
var clear = (e) => {
    while (pic.firstChild) {
        pic.removeChild(pic.firstChild);
    } pX = -1;
}

var draw = (e) => {
    if (pX == -1) { // if first circle
        pX = e.offsetX;
        pY = e.offsetY;
        var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        c.setAttribute("cx", e.offsetX);
        c.setAttribute("cy", e.offsetY);
        c.setAttribute("r", 5);
        c.setAttribute("fill", "red");
        c.setAttribute("stroke", "black");
        pic.appendChild(c);
    } else {
        console.log(pX, pY, e.offsetX, e.offsetY);
        
        // draw the line
        var l = document.createElementNS("http://www.w3.org/2000/svg", "line")
        l.setAttribute("x1", pX);
        l.setAttribute("y1", pY);
        l.setAttribute("x2", e.offsetX);
        l.setAttribute("y2", e.offsetY);
        l.setAttribute("stroke", "black");
        l.setAttribute("stroke-width", "1");
        pic.appendChild(l)

        // draw the new circle
        var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        c.setAttribute("cx", e.offsetX);
        c.setAttribute("cy", e.offsetY);
        c.setAttribute("r", 5);
        c.setAttribute("fill", "red");  
        c.setAttribute("stroke", "black");
        pic.appendChild(c);

        // draw prev circle to cover up the line
        c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        c.setAttribute("cx", pX);
        c.setAttribute("cy", pY);
        c.setAttribute("r", 5);
        c.setAttribute("fill", "red");
        c.setAttribute("stroke", "black");
        pic.appendChild(c);

        // set the new coordinates
        pX = e.offsetX;
        pY = e.offsetY;
    }
}

// add the event listeners
pic.addEventListener("click", draw);
but.addEventListener("click", clear);