// Canvasseurs
// Aaron Li, Aleksandra Koroza
// SoftDev2 pd8
// K02 -- Connecting the dots
// 2019-02-02

// get canvas element
var c = document.getElementById("playground");
// get clear button
var clear = document.getElementById("clear");
var first = true;
// last dot location
var xcor = -1;
var ycor = -1;
var tempF;
var tempS;
// instantiate a CanvasRenderingContext2D
var ctx = c.getContext("2d");


// clearing canvas starting from the origin
// and all the way to the height/width of the canvas
clear.addEventListener("click", function(e) {
	ctx.clearRect(0, 0, c.width, c.height);
	first = True;
});

// drawing a dot and connect lines
var draw = function(e) {
	if (first) { // if ur the first dot
		ctx.beginPath();
		ctx.strokeStyle = "rgb(" + Math.floor(Math.random() * 256) + ", " +
		Math.floor(Math.random() * 256) + ", " +
		Math.floor(Math.random() * 256) + ")";
		ctx.fillStyle = "rgb(" + Math.floor(Math.random() * 256) + ", " +
		Math.floor(Math.random() * 256) + ", " +
		Math.floor(Math.random() * 256) + ")";
		ctx.ellipse(e.offsetX, e.offsetY, 8, 10, 0, Math.PI, Math.PI * 3);
		xcor = e.offsetX;
		ycor = e.offsetY;
		ctx.fill();
		ctx.stroke();
		first = false;
		tempS = ctx.strokeStyle;
		tempF = ctx.fillStyle;
	} else { // if ur the second dot
		ctx.strokeStyle = "rgb(" + Math.floor(Math.random() * 256) + ", " +
		Math.floor(Math.random() * 256) + ", " +
		Math.floor(Math.random() * 256) + ")";
		ctx.fillStyle = "rgb(" + Math.floor(Math.random() * 256) + ", " +
		Math.floor(Math.random() * 256) + ", " +
		Math.floor(Math.random() * 256) + ")";

		// draw the line
		ctx.beginPath();
		ctx.moveTo(xcor, ycor);
		let x = xcor;
		let y = ycor;
		let stroke = ctx.strokeStyle;
		let fill = ctx.fillStyle;
		// set new coordinates
		xcor = e.offsetX;
		ycor = e.offsetY;

		ctx.lineTo(e.offsetX, e.offsetY);
		ctx.fill();
		ctx.stroke();

		// draw the new dot
		ctx.beginPath();
		ctx.ellipse(e.offsetX, e.offsetY, 8, 10, 0, Math.PI, Math.PI * 3);
		ctx.fill();
		ctx.stroke();

		// draw old dot to cover lines
		ctx.beginPath();
		ctx.strokeStyle = tempS;
		ctx.fillStyle = tempF;
		ctx.ellipse(x, y, 8, 10, 0, Math.PI, Math.PI * 3);
		ctx.fill();
		ctx.stroke();

		// set the new stroke/fill styles
		tempS = stroke;
		tempF = fill;

	}
};

// only draw if mouse within the canvas
c.addEventListener("click", draw);

// diagnostic print statements
console.log(c);
console.log(ctx);
