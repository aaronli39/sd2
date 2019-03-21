// Xiaojie(Aaron) Li
// SoftDev2 pd8
// K14 -- Learning to Swim
// 2019-03-20

// this is an array of arrays(subclass of arrays)
// of elements in head tag
var head = d3.select("head");
console.log(head);

// selects all h2 elements with selectAll
// h has only 1 group but has an array of nodes
// --------------------------------------------
// each select becomes the new group in the next
// selection, so you can chain selectAlls
var h = d3.selectAll("h2");
console.log(h);

// appending to a selection add one to each
// element in the group of the previous 
// selection. This will add a p element to each section
var sects = d3.selectAll("section").append("p");
console.log(sects);

// D3 ignores NULL elements, which are elements that
// are not found from the DOM.

// data isnt a property of the selection, but rather its elements
// you can bound data in 3 days:
// 1) using selection.data
// 2) assign to individual elements using selection.datum
// 3) inherited from a parent via append, insert, or select

// .exit() on a selection gives you non-corresponding data in the new dataset
// .update() gives you the found corresponding data in the dataset
// .enter() is a subclass of selection and represents data that
// doesn't yet exist or are not found in the dataset





