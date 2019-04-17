http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_Dinov_020108_HeightsWeights

var data = [
    [66, 113], [72, 136], [69, 153],
    [68, 142], [67, 144], [68, 123],
    [70, 136], [68, 113], [67, 121],
    [69, 143], [71, 138], [68, 130]
];

// map data
var weights = data.map(function(d) { return d[0] });
var heights = data.map(function(d) { return d[1] });


// add svg/margins
var height = 600;
var width = 500;

// set scales
var xScale = d3.scaleLinear()
    .domain([0, d3.max(data)])
    .range([0, width]);

var svg = d3.select("body").append("svg");


