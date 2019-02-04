// Canvasseurs
// Aaron Li, Aleksandra Koroza
// SoftDev2 pd8
// K02 -- Connecting the dots
// 2019-02-02

// variables
var canvas = document.getElementById("playground");
var radius = 0;
var requestID = 0;
var max = (canvas.width - 10) / 2;
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
	if (grow == null) {
		grow = true;
		growing = true;
	}

	if (! grow) {
		grow = true;
	}

	console.log(grow);
	if (grow) {
		requestID = window.requestAnimationFrame(draw);
		ctx.beginPath();
		ctx.fillStyle = "#00FFFF";
		console.log(radius);
		ctx.clearRect(0, 0, canvas.width, canvas.height);
		ctx.arc(canvas.width / 2, canvas.height / 2, radius, Math.PI, Math.PI * 3);
		ctx.fill();
		if (growing) radius += 1;
		else {
			radius -= 1;
		}

		console.log(growing);
		if (radius >= max) {
			growing = false;
		}

		if (radius == 0) {
			growing = true;
		}
	}
};



stop.addEventListener("click", halt);
animate.addEventListener("click", draw);
