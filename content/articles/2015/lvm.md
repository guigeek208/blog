Title: Redimensionner un LVM avec un minimum de coupure …
Date: 2015-04-11 11:34
Author: Guillaume Roche
About_author: network engineer.
Category: dev&sysadmin
Tags: lvm, linux


Pour détecter le nouveau disque ou la modification de la taille du disque
	
	:::bash
	echo 1 > /sys/class/scsi_device/0\:0\:0\:0/device/rescan
Modifier les partitions en supprimant et recréant la partition (vérifiez pour plus de sécurité les index start)

	:::bash
	fdisk /dev/sdaX
Une fois les partitions modifiées, redémarrez en serrant les fesses 😉

Une fois redémarré, on rescan le physical volume :

	:::bash
	pvscan
Et on le redimensionne :

	:::bash
	pvresize /dev/sda5
On l’affiche :

	:::bash
	pvdisplay
Ensuite il faut démonter la partition à redimensionner :

	:::bash
	umount /home
On étend le lvm :

	:::bash
	lvextend -l +100%FREE /dev/snack1/home
On affiche le lvm :

	:::bash
	lvdisplay
On vérifie et nettoie le lvm :

	:::bash
	e2fsck -f /dev/snack1/home
Et enfin on redimensionne le filesystem

	:::bash
	resize2fs /dev/snack1/home
Et on remonte la partition :

	:::bash
	mount -a
