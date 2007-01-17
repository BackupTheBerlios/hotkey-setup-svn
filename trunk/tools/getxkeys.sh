#!/bin/bash
# Get the new xkey syms from the fedora wiki
wget -q -U ffesti 'http://fedoraproject.org/wiki/Extras/SIGs/Laptop/HotKeys/MissingMappingLinuxToX11?action=raw'

mv 'MissingMappingLinuxToX11?action=raw' xkeys.txt
