#SOFTDEV NOTES

-----

## 02/01/19

**Aim**: Connections

* paths used to draw arbitrary shapes, cindluig circles and curves
* a context can keep track of one path at a time
* path is not drawn until ```stroke()``` is called
* a path is considered done when ```beginPath()``` is called anew

**(some) functions**:
* ```beginPath()```: starts or resets current path
* ```stroke()```: renders all the lines in the path, **does not end the path**
* ```fill()```: fills the interior of the path, will not work if the path has fewer than 3 points in it
* ```arc()```: draws an arc

**useful commands**:
* ```moveTo(x, y)```: moves to (x, y) without pencil down
* ```lineTo(x, y)```: moves path to position (x, y) and will result in a line and filled in section
* ```closePath()```: results in a line from current position to start position. Path can be continued after

-----

## 01/31/19

**Aim**: Mess around on the canvas

**unix philosophy?**:
* have minimalistic small chunks of code
* when designing a tool, it does one job and does it well, and nothing else

-----

## 01/30/19

**Aim**: Mess around on the canvas

* aKoroza
* sashakor - github

-----

## 01/29/19

**Aim**: Sails | sheets |denim | tarps | politickin'...

**HTML5**:
* redesign of HTML with a focus on making the more modern features of web brwosers esy to work with
* includes **built-in** suport for audio and video playback via new elements:
	* ```<video>```
	* ```<audio>```
* designed around JS and a standardize DOM
* includes an element that can be used to draw a ```<canvas>``` using javascript

**ENter the CANVAS**:
* HTML5 element that provides drawing area
* you must give it an ID
* you must declare a rendering context(*2d drawing, 3d drawing, raw bitmap rendering...*)
* only 2 default attributes: height and weight
* assignable via DOM manipulation(JS calls)

**Test**:
```html
<canvas height="600" width="600" id="slate">
</canvas>
```
