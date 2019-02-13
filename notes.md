#SOFTDEV NOTES

-----

## 02/12/19

**Aim**: Cold LAMPin' with Flav

* our web apps have been using Flask's built in web server
* recall: 
    * web server (in the software sense) is simply a process listening for HTTP requests and responding to them
    * Flask is a *microframework*

**flask's web server**
* great for dev/debugging b/c simple, fast, ez turn on/off
* **suboptimal** for full time site serving
* server is **single-threaded**:
    * each request(html/css/js/imgs/etc) handled sequentially. Visitors must wait for any prior requests before theirs get processed
    * not desgined to protect your app or host(serving mahine) from malicious attacks
    * not intended to be long-term, persistent, high-volume server (could fail for various reasons)

**production web servers**
* designed to handle high quantity of requests
* commonly use separate processes/threaded for each request (these often called workers)
* can serve multiple sites/apps from same host (eg: talos.stuy.edu, cyber.stuy.edu, someothersite.com)
* eg: apache, nginx, green unicorn
* more robust than Flask, less than apache/nginx
* requires minimal config

**why apache2?**
* longstanding
* familiar
  
**LAMP**:
* **L**inux
* **A**pache
* **M**ySql
* **P**hp
* alternatives: LEMP, MEEN, MEAN

* DO gide on LAMP: goo.gl/C7Ho5J
* goo.gl/vvnw7M

-----

## 02/04/19

**Aim**: Repaint, repaint, repaint, repaint ...

**DN**:
* animation is rendering images quickly and is used to imitate/create the illusion of movement when in reality its just successive playing of imagery

**commands**:
* **don't** use: ```setTimeout()``` or ```setInterval()``` because:
	* you dont get the delay you asked for
	* induce browser spasticity(force reflow before fully loaded)
* use ```window.requestAnimationFrame()```:
	* executes on *next available* screen repaint (ensures hardware/browsers are ready)
	* pauses for background tabs, hidden frames, etc.
	* is automatically passed a timestamp to mark call time
	* returns a **non-zero** integer(can be used as ID)
	* 60fps target
	* can be optimized bt browser (smoother animations)
	* more resource efficient(battery-friendly)
	* syntax: ```requestAnimationFrame(*callback*)```
* use ```window.cancelAnimationFrame()```:
	* stops animation
	* syntax: ```cancelAnimationFrame(id)```

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
