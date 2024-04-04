#!/bin/sh

# The pure GTK build of emacs is not supported on X11, so try to avoid
# using if there is an alternative.

if [ "$XDG_SESSION_TYPE" = 'x11' ]; then
    exec emacs-x11 "$@"
else
    exec emacs-gtk "$@"
fi
