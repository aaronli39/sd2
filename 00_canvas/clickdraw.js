var c = document.getElementById("slate");
var clear = document.getElementById("clear");
var tog = document.getElementById("toggle");
var mode = "rectangle";
var cur = document.getElementById("cur");

// instantiate a CanvasRenderingContext2D
var ctx = c.getContext("2d");
// invoke interface methods
// ctx.fillStyle = "#ff0000";
// ctx.strokeStyle = "#ff0000";
// strokeStyle, clearRect(), fillText ellipse()
// ctx.fillRect(80, 100, 100, 200);
cur.innerHTML = "Current mode: " + mode;

c.addEventListener("click", function(e) {
	ctx.fillStyle = "#0000ff";
	ctx.fillRect(e.clientX, e.clientY, 100, 200);
	console.log(e.clientX);
	console.log(e.clientY);
});

clear.addEventListener("click", function(e) {
	ctx.clearRect(0, 0, c.height, c.width);
});

tog.addEventListener("click", function(e) {
	if (mode == "rectangle") {
		mode = "circle";
		cur.innerHTML = "Current mode: " + mode;
	} else {
		mode = "rectangle";
		cur.innerHTML = "Current mode: " + mode;
	}
});

console.log(c);
console.log(ctx);
