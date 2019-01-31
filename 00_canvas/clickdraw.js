// Aaron Li
// SoftDev2 pd8
// K00 -- I See a Red Door
// 2019-01-30

var c = document.getElementById("slate");
var clear = document.getElementById("clear");
var tog = document.getElementById("toggle");
var mode = "(boring) box";
var cur = document.getElementById("cur");

// instantiate a CanvasRenderingContext2D
var ctx = c.getContext("2d");

// setting the current mode
cur.innerHTML = "Current mode: " + mode;
tog.addEventListener("click", function(e) {
	if (mode == "(boring) box") {
		mode = "(big) dot";
		cur.innerHTML = "Current mode: " + mode;
	} else {
		mode = "(boring) box";
		cur.innerHTML = "Current mode: " + mode;
	}
});

// clearing canvas
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
		ctx.fillRect(e.offsetX - 50, e.offsetY - 75, 100, 150);
	} else if (mode == "(big) dot") { // mode circle
		ctx.beginPath();
		ctx.strokeStyle = "rgb(" + Math.floor(Math.random() * 256) + ", " +
						Math.floor(Math.random() * 256) + ", " +
						Math.floor(Math.random() * 256) + ")";
		ctx.fillStyle = "rgb(" + Math.floor(Math.random() * 256) + ", " +
						Math.floor(Math.random() * 256) + ", " +
						Math.floor(Math.random() * 256) + ")";
		ctx.ellipse(e.offsetX, e.offsetY, 10, 15, 0, Math.PI, Math.PI * 3);
		ctx.fill();
		ctx.stroke();
	}
};

// only draw if mouse within the canvas
c.addEventListener("click", draw);

console.log(c);
console.log(ctx);
