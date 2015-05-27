Title: ssh sans mot de passe
Auhtor: Josue Kouka
Date: 2012-12-20
Tags: linux, ssh, server
Category: Linux
Summary: Se connecter via ssh a des serveurs sans taper sans mot de passe

Hi guys !!!!

Vous êtes fatigué d'entrer votre mot de passe sur les differents serveurs sur lesquels vous travaillez tous les jours ?

Vous êtes fatigué de rechercher vos credentials ssh dans les différentes fiches techniques afin de vous connecter ? 

Vous êtes fatigué de ....

    loking> Yo Joe!!! Stop it !!!
    loking> You ain't a commercial speaker, are you ? 
    josue> Nope, ain't.
    loking> Then stop !!!
    loking> Besides, you suck !!!!
    josue> that was mean bro :( 

Petit guide sur comment faire pour eviter d'en avoir marre.

    :::console
    huey@freeman:~$ssh -t keygen rsa
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/huey/.ssh/id_rsa): 
    Created directory '/home/huey/.ssh'.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /home/huey/.ssh/id_rsa.
    Your public key has been saved in /home/huey/.ssh/id_rsa.pub.
    The key fingerprint is:
    3e:4f:05:79:3a:9f:96:7c:3b:ad:e9:58:37:bc:37:e4 huey@freeman

    huey@freeman:~$ ls .ssh/
    id_rsa  id_rsa.pub  known_hosts

***NB***: N'entrez pas de ***passphrase*** 

On se connecte sur le serveur _ruckus_
On cree un repertoire ___.ssh___ s'il n'existe pas.

    :::console
    uncle@ruckus:~$mkdir .ssh/
    uncle@ruckus:~$exit

De retour sur huey, entrez la commande suivante et votre mot de passe _pour la derniere fois_

    :::console
    huey@freeman:~$cat .ssh/id_rsa.pub | ssh uncle@ruckus 'cat >> .ssh/authorized_keys'
    uncle@ruckus's password:

Maintenant, huey peut se connecter avec le compte _uncle_ sur _ruckus_ sans mot de passe.

Et moi je peux aller [poser ma question à Ronalda](http://www.youtube.com/watch?v=b3F0B4hAsmI)


