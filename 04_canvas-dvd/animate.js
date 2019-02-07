// happy cows
// Aaron Li, Joyce Liao
// SoftDev2 pd8
// K04 -- canvas-based, JS-driven animation -- now with external img
// 2019-02-06

// variables
var canvas = document.getElementById("playground"); // canvas element
var radius = 0; // current radius
var requestID = 0; // request id
var max = (canvas.width - 10) / 2; // max radius
var growing = true; // growing or shrinking

var stop = document.getElementById("stop"); // stop button
var animate = document.getElementById("circle"); // animation button
var dvd = document.getElementById("dvd");

var ctx = canvas.getContext("2d"); // set the context

// halts animation
var halt = function(e) {
	console.log(requestID);
	window.cancelAnimationFrame(requestID);
};

// animate
var draw = function(e) {
	// this is like clearing before drawing,
	// we want to stop any other animations before
	// starting another (prevent speeding up)
	halt();

	// request a new animation
	requestID = window.requestAnimationFrame(draw);
	// clear rect first
	ctx.clearRect(0, 0, canvas.width, canvas.height);

	// drawing the new circle
	ctx.beginPath();
	ctx.fillStyle = "#00FFFF";
	ctx.arc(canvas.width / 2, canvas.height / 2, radius, 0, Math.PI * 2);
	ctx.stroke();
	ctx.fill();

	// if growing, increment radius and vice versa
	if (growing) radius += 1;
	else {
		radius -= 1;
	}

	// facilitate growing/shrinking behavior upon
	// reaching max radius or 0
	if (radius >= max) {
		growing = false;
	}
	if (radius == 0) {
		growing = true;
	}
};

// dvd animation
var dvder = function(e) {
	// cancel previous frame to prevent speeding
	window.cancelAnimationFrame(requestID);
	// img dimensions
	var rectW = 100;
	var rectH = 50;
	// randomize starting location
	// stores the current x/y coordinate of image
	var rectX = Math.floor(Math.random() * (canvas.width - rectW));
	var rectY = Math.floor(Math.random() * (canvas.width - rectH));
	// vector components of movement
	var xVel = 1;
	var yVel = 1;

	// create the new image obj and set source
	var logo = new Image();
	logo.src = "logo_dvd.jpg";

	// use an internal function so you can callback without
	// resetting all variables above ^
	var dvdLogo = function() {
		// clear the canvas first
		ctx.clearRect(0, 0, canvas.width, canvas.height);
		// set request id
		requestID = window.requestAnimationFrame(dvdLogo);

		console.log(rectX);
		console.log(rectY);

		// draw the image
		ctx.drawImage(logo, rectX, rectY, rectW, rectH);
		if (rectX >= canvas.width - rectW) { // bounces off right
			xVel = -1;
		} else if (rectY <= 0) { // bounces top
			yVel = 1;
		} else if (rectY >= canvas.height - rectH) { // bounces buttom
			yVel = -1;
		} else if (rectX <= 0) { // bounces left
			xVel = 1;
		}

		// increment/decrement to the new position
		rectX += xVel;
		rectY += yVel;
	}; dvdLogo();
};

// button event listeners
stop.addEventListener("click", halt);
animate.addEventListener("click", draw);
dvd.addEventListener("click", dvder);
