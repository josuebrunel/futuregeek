Title: How to import projects from another gitlab instance
Slug: how-to-import-projects-from-another-gitlab-instance
Date: 2015-05-27
Tags: shell, bash, git, gitlab
Category: Linux
Author: Josue Kouka
Lang: en
Summary: Import gitlab projects from another server

Hi, 
Given 2 gitlab servers:

* gitlab1
* gitlab2

And we want to import ___gitlab1 ___ projects into ___gitlab2___ . Both ***gitlab*** are installed with **omnibus** 

1. ### _Connect to gitlab1_ 

        :::shell
        john@gitlab1$ sudo tar czvf git-data.tar.gz /var/opt/gitlab/git-data
        john@gitlab1$ scp git-data.tar.gz john@gitlab2:~/

2. ### _Connect to gitlab2_

        :::shell
        john@gitlab2~$ sudo xzvf git-data -C /var/opt/gitlab/
        john@gitlab2~$ sudo chown -R git:git /var/opt/gitlab/git-data/
        john@gitlab2~$ sudo gitlab-rake gitlab:import:repos
        john@gitlab2~$ sudo gitlab-rake gitlab:assest:precompile

3. ### _Go on your gitlab interface and you will see your **projects** there._
