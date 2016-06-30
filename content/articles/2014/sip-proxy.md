Title: Monter un proxy SIP
Date: 2014-07-03 15:41
Author: Guillaume Roche
About_author: network engineer.
Category: dev&sysadmin
Tags: asterisk, sip

Lorsque vous paramétrez un Call Manager Cisco (CUCM), il n’est pas possible de configurer un SIP Trunk avec authentification via un SIP Provider, il faut rajouter en général un routeur . Si vous n’en avez pas la moyen, pas de problème un proxy SIP avec Asterisk fera l’affaire .

Asterisk

1
apt-get install asterisk
Monter le trunk SIP :

	:::bash
	[ccm]
	type=friend
	host=x.x.x.x
	allow=all
	fromdomain=x.x.x.x
	nat=yes
	canreinvite=yes
	qualify=no
	dtmfmode=rfc2833

	[SIPExt]
	type=friend
	allow=all
	host=x.x.x.x
	dtmfmode=inband
	qualify=no
	nat=yes
	insecure=port,invite
	context=fromSIPExt
	dtmfmode=rfc2833
	directmedia=nonat

le directmedia=nonat va permettre que tous les flux audio passent pas l’asterisk si vous êtes NATé ..

Puis dans le fichier extensions.conf :

	:::bash
	[default]
	exten => _6XX,1,Dial(SIP/ccm/${EXTEN})
	exten => 201, 1, Dial(SIP/201,25,r)
	exten => _0,1,Set(CALLERID(number)=35220600${CALLERIDNUM})
	exten => _0.,1,Dial(SIP/SIPExt/${EXTEN})
	 
	[fromSIPExt]
	exten => _35220600XXX,1,Dial(SIP/ccm/${EXTEN:8})
	
Faites un redémarrage de Asterisk .
Pour débugger passer en mode debug avec :

	:::bash
	asterisk -rvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
 	sip set debug peer x.x.x.x

Vous verrez mieux ce qu’il se passe .

Si par hasard vous rencontez des problème du type : la communication se coupe après quelques minutes et un message d’erreur de ce genre :

	:::bash
	WARNING[1641]: chan_sip.c:4169 retrans_pkt: Retransmission timeout reached on transmission 76db5012673eae5401286b7e6718e8b4@65.51.243.124:5060 for seqno 102 (Critical Request) -- See  
	modifier le fichier sip.conf de la sorte :

	[general]
	externip = <your real="" ip=""> 
	localnet = <locanet mask="">
	</locanet></your>