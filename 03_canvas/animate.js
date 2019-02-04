// Canvasseurs
// Aaron Li, Aleksandra Koroza
// SoftDev2 pd8
// K02 -- Connecting the dots
// 2019-02-02

// variables
var canvas = document.getElementById("playground");
var radius = 0;
var requestID = 0;
var max = canvas.width - 10;
var grow; // growing or stopped
var growing;

var stop = document.getElementById("stop");
var animate = document.getElementById("circle");

var ctx = canvas.getContext("2d");

var halt = function(e) {
	if (grow) {
		console.log(requestID);
		window.cancelAnimationFrame(requestID);
		grow = false;
	}
};

var draw = function(e) {
	if (grow == null) grow = true;
	console.log(grow);
	if (grow) {
		requestID = window.requestAnimationFrame(draw);
		ctx.beginPath();
		ctx.fillStyle = "#00FFFF";
		ctx.arc(canvas.width / 2, canvas.height / 2, radius, Math.PI, Math.PI * 3);
		ctx.fill();
		radius += 1;

		if (radius == max)
	}
};



stop.addEventListener("click", halt);
animate.addEventListener("click", draw);
