Title: How to install fonts on linux
Auhtor: Josue Kouka
Date: 2013-01-20
Tags: linux, font,
Category: Linux
Summary:


Hi guys !!!
I was using a mac lately, and i fell in love with the monaco font. That font is so cool on emacs ^_^.

So i started searching on the internet and found how to do so. Here it's:

You can get that font [here](http://jorrel.googlepages.com/Monaco_Linux.ttf).

Then on your terminal 

    :::console
    yosuke@loking:$sudo mkdir /usr/share/fonts/truetype/custom
    yosuke@loking:$sudo mv Monaco_Linux.ttf /usr/share/fonts/truetype/custom/
    yosuke@loking:$sudo fc-cache -f -v

That's all. Now you can use __monaco__ font .

![Alt example](./static_files/font/monaco_font.png)


Isn't it cool !!!