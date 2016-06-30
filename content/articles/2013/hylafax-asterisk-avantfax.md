Title: Serveur de Fax avec Hylaxfax, asterisk et avantfax
Date: 2013-09-15 15:41
Author: Guillaume Roche
About_author: network engineer.
Category: dev&sysadmin
Tags: hylafax, avantfax, asterisk

Depuis quelques temps, je recherche à monter un serveur de fax afin que celui-ci fonctionne sur la ToIP Cisco que j’installe régulièrement . Je me suis penché tout d’abord sur t38modem pour monter le trunk SIP ou H323 avec le Call Manager mais ca ne fonctionnait pas bien .
Ensuite, je me suis dirigé vers Asterisk avec un trunk SIP H323 et iaxmodem qui permet d’émuler des modems avec lesquels Hylafax va communiquer .
Voila la procédure mis en place sur une Debian Wheezy (attention j’ai essayé de faire marcher cela dans un container LXC mais sans succès surement à cause du iaxmodem qui pose problème lors de la création des modems)


### Asterisk

	:::bash
	apt-get install asterisk iaxmodem
Monter un trunk SIP avec votre équipement ou votre sortie :

	:::bash
	[ccm]
	type=friend
	host=x.x.x.x
	;allow=alaw
	allow=all
	nat=no
	canreinvite=yes
	qualify=yes
	dtmfmode=rfc2833
	context=default
	Configurons les modems :

/etc/iaxmodem/ttyIAX0

	:::bash 
	device          /dev/ttyIAX0
	owner           uucp:uucp
	mode            660
	port            4570
	refresh         60
	server          127.0.0.1
	peername        iaxmodem0
	secret          password0
	codec           alaw
	 
/etc/iaxmodem/ttyIAX1

	:::bash
	device          /dev/ttyIAX1
	owner           uucp:uucp
	mode            660
	port            4571
	refresh         60
	server          127.0.0.1
	peername        iaxmodem1
	secret          password1
	codec           alaw

Maintenant, le iaxmodem est entièrement configuré et doit être démarré. On le fait par l’intermédiaire du processus init . Donc, nous ajoutons la ligne suivante à la fin du fichier /etc/inittab ajoutée :

	:::bash
	IA00:23:respawn:/usr/bin/iaxmodem ttyIAX0
	IA00:23:respawn:/usr/bin/iaxmodem ttyIAX1
	MO00: 23: respawn :/ usr / local / sbin / faxgetty ttyIAX0
	MO00: 23: respawn :/ usr / local / sbin / faxgetty ttyIAX1

Configurons Asterisk pour utiliser ses modems :

	:::bash
	[general]
	bindport = 4569           
	bindaddr = 0.0.0.0    
	disallow = all
	allow = alaw
	allow = ulaw
	 
	[iaxmodem0]
	type = friend
	secret = password0
	port = 4570
	host = dynamic
	context = default
	disallow = all
	allow = alaw
	requirecalltoken = no
	 
	[iaxmodem1]
	type = friend
	secret = password1
	port = 4571
	host = dynamic
	context = default
	disallow = all
	allow = alaw
	requirecalltoken = no

En envoi, le fax va alors utiliser le contexte par défaut (context=default) mais libre à vous de l’adapter suivant votre configuration d’Asterisk.

Pour la réception, il faut modifier le fichier qui gère les contextes (extensions.conf) de la facon suivante :

	:::bash
	exten => 8010,1,Dial(IAX2/iaxmodem0)
	exten => 8011,1,Dial(IAX2/iaxmodem1)
Si vos fax arrivent via un trunk sip, bien vérifier que le trunk a un contexte dans lequel votre fax se trouve .

### Hylafax

	:::bash
	apt-get install hylafax-server
	faxsetup

### Avantfax

	:::bash
	apt-get install apache2 libapache2-mod-php5 php5 php-pear php5-mysql mysql-server imagemagick ghostscript libtiff4  libtiff-tools netpbm sudo postfix cups lpr psutils
	php-mdb2-driver-mysql php-mdb2

	chown -R www-data:www-data avantfax
	chmod -R 0770 avantfax/tmp/
	chown -R www-data:uucp avantfax/tmp/
	chown -R www-data:uucp avantfax/faxes/
	 
	ln -s /home/www/avantfax/includes/faxrcvd.php /var/spool/hylafax/bin/faxrcvd.php
	ln -s /home/www/avantfax/includes/dynconf.php /var/spool/hylafax/bin/dynconf.php
	ln -s /home/www/avantfax/includes/notify.php /var/spool/hylafax/bin/notify.php
	 
	mysql -uroot -p < create_user.sql
	mysql -uavantfax -pd58fe49 avantfax < create_tables.sql

Modifier le fichier includes/local_config-example.php