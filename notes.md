#SOFTDEV NOTES

## 05/02/19

**Aim**: Memoization++ & Life Beyond

**Tech Resume**:
* action words
* less is more
* only list tech/lang if you know it
* do not leave out tech/lang you know
* appropriate email
* PROOFREAD
* goal of resume:
* need not fill page
* name and contact info clear at top

***args**:
* use this when you don't know how many arguments there will be
* when function is called, then you can access it as a list

```python
def mem(f):
    cache = {}
    def memoize(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    return memoize
```

-----

## 05/01/19

**Aim**: Achieve closure

* memoization: process of storing previously calculated results as to avoid recalculation

-----

## 04/30/19

* in python, a fxn is a first class citizen, meaning:
    * it can be passed as a variable etc
* a **closure** remembers the context in which it was created, even if you delete the creator function
```python
del outer
outer(42)
```

**creating a closure**:
* define nested function
* nested function must refer to var defined in enclosing fxn(optional)
* return nested function


-----

## 04/29/19

**Aim**: JS and the Holy Trinity of Data Processing

* reduce in JS

```js
x = [1, 2, 3, 4]
// this will sum elements of x
x.reduce(function(a, b), {return a + b});
```

* filter, map, and reduce (holy trinity of data processing)

```js
// mapping
var x = [1, 2, 3, 4]
var newX = x.map(function(n) {
    return n * 2;
});

console.log("doubled:", newX);

// filter
// filters out values you don't want
var x = [1, 2, 3, 4]
var newX = x.filter(function(n) {
    return (n % 2 == 0)
});

```

-----

## 04/17/19

**Aim** Reductio ad absurbdum

* Math.sqrt in python is costly since it's not super accurate and also it jumps back in forth to try to make an approximation
* reduce: a function tat returns something to a single value, performs rolling calculation on successive value pairs
* reduce is from `functools`
* lambda in python:
    * must return a value
    * should remind you of scheme
    * conditionals must be in form of a python ternary operator
    * `exprA if conditions else exprB

-----

## 04/15/19

**Aim**: WHat else can you do via list comprehensions?

* quicksort is 

-----

## 04/12/19

**Aim**: comprende

-----

## 04/11/19

* list comprehension    
    * can have zero or more ifs/fors to be more complex
* tuples: immutable list

-----

## 03/19/19

**enter selection**
* collection of placeholder nodes for each data element for which no corresponding existing DOM element was found
* the styling works only b/c you have binded dom elements to data

-----

## 03/18/19
**Aim**: _ocument_riven_ata

**the basics**
* include http://d3js.org/d3.v5.min.js in a script tag to sse d3 or download the source and link that instead
* d3 is a data visualization tool

**selectors**
* a la jquery
* concisify selection of DOM elements
* eg, some D3 selector functions:
    * `d3.select( IDENTIFIER );`: returns first element matching identifier
    * `d3.selectALL( IDENTIFIER );`: returns an array of all elements matching given identifier
* why d3? after selectin an element, you can set various attributes: style, text, etc:
    * `d3.select("body').style("color", "red")`
* or pass **functions** to set values dynamically:
    * `d3.selectAll("p").style("font-size", function() { return Math.floor( Math.random() * 15) + "px"});`
* binding data: you can bind data to elements in d3


-----

## 03/15/19

**Event propagation**:
* an element intercepts an event
* browser collects DOM node path of the event from the starting element to the root
* **capture**: event propagtaes down the path from step 2
* **bubbling**: event propatates up the path from step 2

* *default* event listener trigger in bubbling phase
* to trigger during capture phase, add `true` argument as 3rd option to `addEventListener`

**`this`**:
* has different meanings depending on JS context
* in a JS obj, `this` refers to the calling obj
* in an event listener, `this` refers to the currently triggered element

**`.target`**:
* returns the element that began the event propagation chain

-----

## 03/13/19

-----

## 03/12/19

**XML**:
* extensible markup language
* meta-language: use it to create other languages
* defines a set of rules for encoding data in a format which is both *human-readable* and *machine-readable*
* **not** a formatting language(HTML, GHFMD)
* allows you to define a file *type* or data *type*
* stores data, but not really render it
* framework for creating markup-based grammars
* uses some syntactic standards of HTML(tags, attributes)
* emphasizes **organizing** and **representing** data(instead of rendering/displaying it)
* an XML **workspace** is defined by the tags and attributes associated with a specific XML language
* forms of XML namespaces(docx, RSS, MathML)
* **raster** image encoding: PNG, JPEG, GIF, etc
    * comes from Latin *rastrum* -> "Rake"
    * **bit by bit** specification of an image
* **SVG**: scalable vector graphics
    * vector image format
    * XML-based
    * an SVG img and its actions are defined by its XML file
    * vector graphics are images not represented as a 2d grid of pixels, but rather a **list of drawing commands**
    * **biggest advantage:** to vector graphics is that they are scalable to any size without *resulting in pixelation*
    * `<svg>` element is designed to store SVG code
    * `<xmlns>`: attribute that identifies that namespace for the specific XML language being used
    * eg:
```xml
<svg xmlns="http://www.w3.org/2000/svg">
    <!-- YOUR SVG CODE HERE -->
</svg>

```

-----

## 03/07/19

* you can run mongo on 127.0.0.1 by doing:
```py
if __name__== "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
```



-----

## 03/06/19

**Aim**: Throw a facade on it


-----

## 02/28/19

* you needed to create a /data/db/ directory before you can use `mongod -v --bind_ip_all --noauth --dbpath <path>`

**using pymongo**
* pip install pymongo
* then:
```py

import pymongo

SERVER_ADDR = "149.89.150.100"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.test
collection = db.restaurants

```

* checkout [here](api.mongodb.com/python/current/tutorial.html)
* 

-----

## 02/27/19

**matthew ming - ocaml**
* objective caml, made to be highly readable, excels at recursion
* considered to be one of the fastest high-level languages

**mongo**
* the `<($lt), >($gt), <=($lte), >=(gte), !=(ne)` operators
    * eq: `{"id": {$lt: 400}`
```py
{$or [{"name":"boa"},
    {"id":{$lt:400}}
    ]
}

$ mongoimport --db <dbname> --collection <collection_name> --file <path to json import file>

$ mongod -v --bind_ip_all --noauth --dbpath <path>
```

-----

## 02/25/19

**Aim**: Hu**mongo**us learnination

**relational dbs**:
* libraries
* you are not in default in the yellow pages
* hospital 
* school
* prison
* dmv
* airlines
* user profile - bad for relational db

**drawbacks of relational db**
* fixed schedma
    * must be known ahead of time
    * problematic to change after up and running
* lists are problematic
* redundant data(in a bad way)(storing excess data that has no true purpose)
* must live on a single host

**noSQL (doument-oriented DB)**
* non table based relational db
* growing b/c of web apps, big data
* **key-value dictionaries:** db is essentially a huge dictionary
* **graph:** db stored as graph w relationships btwn nodes
* **document:** db collection of documents each containing unfixed data(amount, type)
* sites like FB and Twitter would not possible without graph data
* SQL <-> DocDB:
    * record <-> doc
    * table <-> collection

**documented-oriented db**
* each record stored as a doc(instead of row in table)
* each doc contains:
    * all data associated with given record, as key-value pairs("fields" with "values")
* fields need no type specification
* a field mayb contain different types of data
* docs may be grouped together in a collection
* docus in a collection need NOT have same complement of fields
* each dot gets primary key, usually assigned by DB manager
* docs need not be stored on same storage device
* you can dynamically update/add data without having to take it down

**making MongoDB work for you**
* employs separate server/daemon(as opposed to storing entire DB as a single file)
* facilitate distribution of DB over many hosts if required

**commands**
* `db.<collection>.insert(<doc>)`
    * adds doc to collection
    * if collection doesnt exist, create

-----

## 02/14/19

**reading flask and apache2 errors**
* `sudo cat /var/log/apache2/error.log`
* all requests, updated real time: `sudo tail /var/log/apache2/access.log -f`

-----

## 02/13/19

**apache2**
* each unique site is a virtual host
* all processes run as:
    * user **www-data**
    * group **www-data**
* config files live in **/etc/apache2**
* websites live in **/var/www**

**apache2 + flask**
* goal: apache2 as web server, but flask as backend

* enter WSGI(web server gateway interface)
* convention/set of common fxn names
* allows conventional web server to fwd requests to a microframework like flask
* http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/

1) rename flask app to `__init__.py`
2) entire flask app in a single dir, named after your app
3) put this dir in another of same name
4) in outer dir, create file `<appname>.wsgi` (`<appname>.conf` is required too)

**server setup on 18.04**
1) install apache2
2) sudo apt install apache2
3) install and enable WSGI

```python
sudo apt install libapache2-mod-wsgi
sudo a2enmod wsgi # enable module
sudo service apache2 restart # restarts server

# write WSGI file

#!/usr/bin/python
import sys
sys.path.insert(0, "/var/www/<appname>/)
from <appname> import app as application
# change app to match name of Flask object in __init__.py
```
goo.gl/hJVt5J

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
