Title: Configurer un compte SIP (Free) avec un UC540/CME
Date: 2013-05-28 15:41
Author: Guillaume Roche
About_author: network engineer.
Category: dev&sysadmin
Tags: cisco, sip


Pour configurer un compte SIP (en l’occurence free) avec un UC500 de Cisco ou bien un Call Manager Express, voilà comment procéder :

	:::bash
	sip-ua 
	 credentials username numero-freebox password 0 motdepasse realm freephonie.net
	 keepalive target dns:freephonie.net
	 authentication username numero-freebox password 0 motdepasse
	 calling-info pstn-to-sip from number set numero-freebox
	 retry invite 3
	 retry response 3
	 retry bye 3
	 retry cancel 3
	 retry register 3
	 timers trying 1000
	 registrar 1 dns:freephonie.net expires 3600
	 sip-server dns:freephonie.net

Ensuite configurer simplement un dial-peer :

	:::bash
	dial-peer voice 60 voip
	 destination-pattern 0.T
	 session protocol sipv2
	 session target sip-server
	 voice-class sip dtmf-relay force rtp-nte
	 dtmf-relay sip-notify
	 codec g711alaw
	 
Et voila …