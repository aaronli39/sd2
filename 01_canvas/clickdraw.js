// Canvasseurs
// Aaron Li, Aleksandra Koroza
// SoftDev2 pd8
// K00 -- I See a Red Door
// 2019-01-30

// get canvas element
var c = document.getElementById("slate");
// get clear button
var clear = document.getElementById("clear");
// get toggle button
var tog = document.getElementById("toggle");
// state of the mode(circle or rect)
var mode = "";
// get heading to display current mode
var cur = document.getElementById("cur");
// instantiate a CanvasRenderingContext2D
var ctx = c.getContext("2d");


// setting the current mode
cur.innerHTML = "Current mode: " + mode;

// each click of toggle button switches to the other mode
tog.addEventListener("click", function(e) {
	if (mode == "(boring) box") {
		mode = "(big) dot";
		cur.innerHTML = "Current mode: " + mode;
	} else {
		mode = "(boring) box";
		cur.innerHTML = "Current mode: " + mode;
	}
});

// clearing canvas starting from the origin
// and all the way to the height/width of the canvas
clear.addEventListener("click", function(e) {
	ctx.clearRect(0, 0, c.width, c.height);
});

// drawing whatever mode is on
var draw = function(e) {
	console.log("xcor: " + e.offsetX);
	console.log("ycor: " + e.offsetY);
	if (mode == "(boring) box") { // mode rect
		// randomize color of box
		ctx.fillStyle = "rgb(" + Math.floor(Math.random() * 256) + ", " +
						Math.floor(Math.random() * 256) + ", " +
						Math.floor(Math.random() * 256) + ")";

		// --------------------------------------------------------------
		// we use offsetX and offsetY here in order to
		// draw the rectangle at the top-left corner of the mouse.
		// This is because offsetX is a property of the mouse-event itself
		// and is the distance between the mouse click and the padding of the
		// canvas, in this case, this distance is the coordinate from which the
		// rectangle should be drawn. The same can be said offsetY but for y-coordinates.
		// --------------------------------------------------------------
		ctx.fillRect(e.offsetX, e.offsetY, 100, 150);
	} else if (mode == "(big) dot") { // mode circle
		// beginPath() is used at the beginning of each line in order to
		// be able to make unique strokes in the ellipses(the outline)
		ctx.beginPath();
		ctx.strokeStyle = "rgb(" + Math.floor(Math.random() * 256) + ", " +
						Math.floor(Math.random() * 256) + ", " +
						Math.floor(Math.random() * 256) + ")";
		ctx.fillStyle = "rgb(" + Math.floor(Math.random() * 256) + ", " +
						Math.floor(Math.random() * 256) + ", " +
						Math.floor(Math.random() * 256) + ")";

		// --------------------------------------------------------------
		// offsetX and offsetY is used here to center the ellipse since
		// the ellipse is draw with the center supplied as opposed to the
		// rectangle where the coordinates supplied is the top-left of the
		// rectangle.Because of this we don't have to do extra work to
		// determine where the center of the ellipse/dot is.
		// --------------------------------------------------------------

		ctx.ellipse(e.offsetX, e.offsetY, 10, 15, 0, Math.PI, Math.PI * 3);
		ctx.fill();
		ctx.stroke();
	}
};

// only draw if mouse within the canvas
c.addEventListener("click", draw);

// --------------------------------------------------------------
// we decided to not use e.preventDefault() in this
// assignment because its usability is beyond the scope of this
// assignment. No meaningful action can be created with it.
// What it does is preventing the default action of whatever
// event it is attached to from activating. For eg, preventing
// a checkbox from being checked when preventDefault() is
// attached to an event listener for that checkbox
// --------------------------------------------------------------

// diagnostic print statements
console.log(c);
console.log(ctx);
