#!/bin/bash

manufacturer=`dmidecode --string system-manufacturer`
name=`dmidecode --string system-product-name`
version=`dmidecode --string system-version`

SAVED_STATE=/var/run/hotkey-setup
THINKPAD_LOCKFILE=$SAVED_STATE.thinkpad-keys

# This is here because it needs to be executed both if we have a
# Lenovo that also IDs as a ThinkPad, or if we have a real IBM one.
do_thinkpad () {
    . /usr/share/hotkey-setup/ibm.hk
    if [ -x /usr/sbin/thinkpad-keys ]; then
	if [ ! -c /dev/input/uinput ]; then
	    modprobe uinput
	fi
	if [ ! -b /dev/nvram ]; then
	    modprobe nvram
	fi
	/usr/sbin/thinkpad-keys && touch $THINKPAD_LOCKFILE
    fi
}

case "$1" in
    start)

    /usr/sbin/dumpkeycodes >$SAVED_STATE
    
    if [ $? -gt 0 ]; then
	rm -f $SAVED_STATE
    fi

    . /usr/share/hotkey-setup/key-constants

    case "$manufacturer" in
	Acer*)
	. /usr/share/hotkey-setup/acer.hk
	case "$name" in
	    Aspire\ 16*)
	    . /usr/share/hotkey-setup/acer-aspire-1600.hk
	    ;;
	esac
	;;

	ASUS*)
	. /usr/share/hotkey-setup/asus.hk
	;;

	Compaq*)
	case "$name" in
	    Armada*E500*)
	    . /usr/share/hotkey-setup/compaq.hk
	    ;;
	esac
	;;

	Dell*)
	. /usr/share/hotkey-setup/dell.hk
	;;

	Hewlett-Packard*)
	# Load this _first_, so that it can be overridden
	. /usr/share/hotkey-setup/hp.hk
	case "$name" in
	    # Please open a bug if uncommenting these "Presario" entries works for you...
	    #*Presario\ V2000*)
	    #. /usr/share/hotkey-setup/hp-v2000.hk
	    #;;
	    *Tablet*)
	    . /usr/share/hotkey-setup/hp-tablet.hk
	    ;;
	esac
	;;

	IBM*)
	do_thinkpad
	;;

	LENOVO*)
	case "$version" in
	    *ThinkPad*)
	    do_thinkpad
	    ;;
	esac
	;;
	
	MEDION*)
	case "$name" in
	    *FID2060*)
	    . /usr/share/hotkey-setup/medion-md6200.hk
	    ;;
	esac
	;;

	Samsung*)
	. /usr/share/hotkey-setup/samsung.hk
	;;

	Sony*)
	modprobe sonypi; # Needed to get hotkey events
	;;

	*)
	. /usr/share/hotkey-setup/default.hk	
    esac
    . /usr/share/hotkey-setup/generic.hk
    ;;
    stop)
	if [ -f $THINKPAD_LOCKFILE ]; then
	    kill `pidof thinkpad-keys` && rm -f $THINKPAD_LOCKFILE
	fi
	if [ -f $SAVED_STATE ]; then
		setkeycodes $(cat $SAVED_STATE)
	fi
    ;;
    restart|force-reload)
    $0 stop || true
    $0 start
    ;;
esac
