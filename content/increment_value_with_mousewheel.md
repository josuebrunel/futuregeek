Title: Increment input value using mousewheel in javascript
Slug: increment-input-value-mousewheel 
Date: 2015-01-28 18:14:08
Tags: web, javascript, js, jquery
Category: Programming
Author: Josue Kouka
Lang: en
Summary: How to increment value using javascript/jqeury

We will create a project __demo__ as follow in our __www__ directory :

```shell
$ mkdir -p demo/static/js
$ cd demo
```

Create a **index.html**

```html
<html>
    <head>
        <script src="static/js/jquery.min.js"></script>
        <script src="static/js/demo.js"></script>
    </head>
    <form>
        <label>Number</label>
        <input id="number" name="number" value="0" size="3" maxlength="3" type="text" max="100" min="1"/>
    </form>
</html>
```

*NB* : [jQuery](http://code.jquery.com/jquery-1.11.2.min.js) is required 

Create a file __static/js/demo.js__ with the code below

```javascript
$('document').ready(function(){
    $('#number').bind("mousewheel", function(event, delta){
        var delta = event.originalEvent.wheelDelta;
        var self = $(this);
        var val = parseInt(self.val());
        var max = self.attr('max');
        if (delta > 0 && val < max ){
            self.val(val + 1);
        }
        else{
           if ( val > 0 ){
               self.val(val - 1);
           } 
        }
        return false;
    });
})
```

You can test [localhost](http://localhost/demo/index.html) and play with your mousewheel

Voila !!!!
