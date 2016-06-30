Title: Comment rendre bootable une ISO CUCM Cisco seulement réservée pour les mises à jour ?
Date: 2015-01-26 11:01
Author: Guillaume Roche
About_author: network engineer.
Category: dev&sysadmin
Tags: cisco, cucm, iso

	:::bash
	mkdir iso
	mount -t iso9660 -o loop UCSInstall_UCOS_xxxxxx.iso iso
	cp -rv iso iso2
	cd iso2
	genisoimage -o ../Bootable_UCSInstall_UCOS_xxxxxx.iso   -R -no-emul-boot -boot-load-size 32 -boot-info-table -b isolinux/isolinux.bin .

