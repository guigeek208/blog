Title: Oops! It appears your browser does not allow cookies. You need to enable cookies in order to use the Zimbra Web Client.
Date: 2015-11-30 10:31
Author: Guillaume Roche
About_author: network engineer.
Category: dev&sysadmin
Tags: zimbra, linux

Si vous avez ce message d’erreur sur Zimbra voilà la marche à suivre :

	:::bash
	/opt/zimbra/libexec/zmproxyconfig -e -w -o -a 8080:80:8443:443 -x both -H `zmhostname`

Si vous avez une erreur à cette commande là, lancer ensuite celle là :

	:::bash
	zmprov ms `zmhostname` zimbraReverseProxySSLToUpstreamEnabled FALSE`

Puis relancer la commande précédente et enfin les commandes suivantes :

	:::bash
	zmtlsctl both
	zmprov ms `zmhostname` zimbraReverseProxyMailMode both
	zmprov ms `zmhostname` zimbraMailMode both
	zmcontrol restart
