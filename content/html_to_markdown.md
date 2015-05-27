Title: html to markdown	
Slug: html-to-markdown
Date: 2013-07-07 08:07:14
Tags: linux, html, markdwon, shell
Category: Linux
Author: Josue Kouka
Lang: 
Summary: Get a markdown file from your html.

Hi guys ^_^ !! .

Yeah i know, ya'll happy to read me again, just like friends happy to see a friends they haven't seen in a very very long time ^_^.
Don't worry i missed you too even though i don't KNOW you. Maybe you a creeper or something (No just kidding ). 

A couple weeks ago a lost all my markdown files, by the way i write my articles using markdown. Since last week i wanted to be back on rails with the 
blog, i decided to to find a way (seriously, above all the time) to retrieve my markdown files. 
I've found 2 very convevial tools to do so. But i'm just going to talk about one of them : ***html2markdown*** . The other one being ***pandoc***.

###Installation
----------------------
On your terminal guys 

    :::console
    yosuke@loking:~$ sudo aptitude install html2markdown

###How to 
----------------
    :::console 
    yosuke@loking:~$ html2markdown myfile.html >> myfile.md


You might be in a situation where you have a directory full of html files that you want to convert into markdown. To do so, you can use the script below :

    :::bash
    for file in ./*.html
    do
        echo $file ;
    html2markdown --ignore-links --ignore-image "$file" >> "`basename $file .html`.md"
    done

Tada !!! Your *html* files are now in *markdwon*. Check the **help** to know what **--ignore-inks** and **--ignore-image** do .

Thanks for reading guys and have a nice day ^_^.

