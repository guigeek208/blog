Title: Script Munin pour créer un graph des lignes isdn occupées
Date: 2014-11-30 09:41
Author: Guillaume Roche
About_author: network engineer.
Category: dev&sysadmin
Tags: munin, isdn

Afin de pouvoir superviser plus facilement les lignes occupées et s’il y a saturation voici un petit script qui trace un graphique avec les lignes isdn occupées par rapport aux lignes isdn disponibles :
	:::bash
	#!/bin/bash
	 
	. $MUNIN_LIBDIR/plugins/plugin.sh
	 
	if [ "$1" = "autoconf" ]; then
	        echo yes
	        exit 0
	fi
	 
	# If run with the "config"-parameter, give out information on how the
	# graphs should look.
	 
	if [ "$1" = "config" ]; then
	 
	        # The host name this plugin is for. (Can be overridden to have
	        # one machine answer for several)
	 
	        # The title of the graph
	        echo 'graph_title ISDN Channels'
	        # Arguments to "rrdtool graph". In this case, tell it that the
	        # lower limit of the graph is '0', and that 1k=1000 (not 1024)
	        echo 'graph_args --base 1000 -l 0'
	        # The Y-axis label
	        echo 'graph_vlabel channels'
	        # We want Cur/Min/Avg/Max unscaled (i.e. 0.42 load instead of
	        # 420 milliload)
	        echo 'graph_scale no'
	        # Graph category. Defaults to 'VOIP'
	        echo 'graph_category VOIP'
	        # The fields. "label" is used in the legend. "label" is the only
	        # required subfield.
	        echo 'chbusy.label chbusy'
	    echo 'chtotal.label chtotal'
	 
	        # Last, if run with the "config"-parameter, quit here (don't
	        # display any data)
	        exit 0
	fi
	 
	OID="iso.3.6.1.2.1.10.20.1.2.1.1.2"
	community="public"
	host="10.254.1.254"
	 
	nbcalls=0
	nbchan=0
	newoid=$OID
	regex="iso\.3\.6\.1\.2\.1\.10\.20\.1\.2\.1\.1\.2"
	while [[ $newoid =~ $regex ]];
	do
	    res=$(snmpgetnext -c $community -v 2c $host $newoid)
	    newoid=$(echo $res | cut -d"=" -f1)
	    if [[ $newoid =~ $regex ]]; then
	        #echo $res
	    nbchan=$((nbchan+1))
	        state=$(echo $res | cut -d" " -f4)
	        if [[ $state != "1" ]]; then
	           nbcalls=$((nbcalls+1)) 
	        fi
	        #echo $state
	    fi
	done
	echo "chbusy.value "$nbcalls
	echo "chtotal.value "$nbchan

Voila le résultat obtenu :

![noplacelike](//blog.guigeek.org/images/munin.jpg)