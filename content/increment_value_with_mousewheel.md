Title: Increment input value using mousewheel in javascript
Slug: 
Date: 2015-01-28 18:14:08
Tags: web, javascript, js, jquery
Category: Programming
Author: Josue Kouka
Lang: en
Summary: How to increment value using javascript/jqeury



```html
<html>
    <head>
        <script src="static/js/jquery.min.js"></script>
        <script src="static/js/demo.js"></script>
    </head>
    <form>
        <label>
            Number
        </label>
        <input id="number" name="number" value="0" size="3" maxlength="3" type="text" max="100" min="1"/>
    </form>
</html>
```

```javascript
$('document').ready(function(){
    console.log('Doc Ready');
    $('#number').bind("mousewheel", function(event, delta){
        var delta = event.originalEvent.wheelDelta;
        var self = $(this);
        var val = parseInt(self.val());
        var max = self.attr('max');
        console.log(delta)
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
