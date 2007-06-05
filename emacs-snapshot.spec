%define checkout_HEAD 0
%{?_with_checkout: %{expand: %%global checkout_HEAD 1}}


Summary:	The Emacs text editor for the X Window System

Name:		emacs-snapshot
Version:	22.0.99
Release:	%mkrel 1.20070514.1
License:	GPL
Group:		Editors
URL:		http://www.gnu.org/software/emacs/

Source0:	ftp://alpha.gnu.org/gnu/emacs/pretest/emacs-%{version}.tar.bz2
Source2:	gnu-mini.png
Source3:	gnu-normal.png
Source4:	gnu-large.png
Source5:	emacs-config

Patch1: 	emacs-20.5-loadup.patch
Patch3: 	emacs-20.6-ia64-2.patch
Patch5:		emacs-21.1-bzip2.patch
Patch6:		emacs-snapshot-same-etc-DOC-for-all.patch
Patch7:		emacs-22.0.90-rpath.patch
Patch9:		emacs-22.0.90-force-sendmail-program.patch

Patch20:	emacs-20.4-ppc-config.patch
Patch21:	emacs-20.4-ppc.patch
Patch22:	emacs-21.1-omit-nocombreloc-ppc.patch

Patch100:	emacs-22.0.98-infofix.patch
Patch101:	emacs-21.2-version.patch
Patch103:	emacs-21.2-x86_64.patch
Patch104:	emacs-21.2-hide-toolbar.patch
Patch111:	emacs-22.0.93-ispell-dictionnaries-list-iso-8859-15.patch
Patch114:	emacs-21.3-ppc64.patch

BuildRoot:	%_tmppath/%name-root
BuildRequires:	libxaw-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	XFree86
BuildRequires:	libx11-devel
BuildRequires:	gcc
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	ncurses-devel
BuildRequires:	libungif-devel
BuildRequires:  texinfo
BuildRequires:	xpm-devel
BuildRequires:	gtk+2-devel

Requires(preun): /usr/sbin/update-alternatives
Requires(post):  /usr/sbin/update-alternatives

Requires:	emacs-snapshot-common = %version
Provides:	emacs-bin

#Obsoletes:	emacs-X11 < 22.0.50
#Provides:	emacs-X11 < 22.0.50

%description
Emacs-X11 includes the Emacs text editor program for use with the X
Window System (it provides support for the mouse and other GUI
elements). Emacs-X11 will also run Emacs outside of X, but it has a
larger memory footprint than the 'non-X' Emacs package (emacs-snapshot-nox).

Install emacs-snapshot if you are going to use Emacs with the X Window System.
You should also install emacs-snapshot if you're going to run Emacs both with
and without X (it will work fine both ways). You'll also need to install the
emacs-snapshot-common package in order to run Emacs.

%package el
Summary:	The sources for elisp programs included with Emacs
Group:		Editors
Requires:	emacs-snapshot-common = %version

%description el
Emacs-el contains the emacs-snapshot-elisp sources for many of the elisp
programs included with the main Emacs text editor package.

You need to install emacs-snapshot-el only if you intend to modify any of the
Emacs packages or see some elisp examples.

%package doc
Summary:	Emacs documentation
Group:		Editors
Requires:	emacs-snapshot-common = %version

%description doc
The Emacs documentation.

%package extras
Summary:	Files that Emacs snapshot has in common with stable Emacs
Group:		Editors
Requires:	emacs-snapshot-common = %version
Conflicts:	emacs < 22.0.50

%description extras
emacs-snapshot-extras includes files which are in stable emacs
and would conflict with it:
- binaries
- info pages
- man pages

%package leim
Summary:	Emacs Lisp code for input methods for internationalization
Group:		Editors
Requires:	emacs-snapshot-common = %version

%description leim
The Emacs Lisp code for input methods for various international
character scripts.

%package nox
Summary:	The Emacs text editor without support for the X Window System
Group:		Editors
Requires:	emacs-snapshot-common = %version
Provides:	emacs-bin

Requires(preun): /usr/sbin/update-alternatives
Requires(post):  /usr/sbin/update-alternatives

%description nox
Emacs-nox is the Emacs text editor program without support for
the X Window System.

You need to install this package only if you plan on exclusively using Emacs
without the X Window System (emacs-snapshot will work both in X and out of X,
but emacs-snapshot-nox will only work outside of X). You'll also need to
install the emacs-snapshot package in order to run Emacs.

%package gtk
Summary:	The Emacs text editor using GTK
Group:		Editors
Requires:	emacs-snapshot-common = %version
Provides:	emacs-bin

Requires(preun): /usr/sbin/update-alternatives
Requires(post):  /usr/sbin/update-alternatives

%description gtk
Emacs-gtk is the Emacs text editor program with support for
the X Window System and using GTK

%package common
Summary:	The libraries needed to run the GNU Emacs text editor
Group:		Editors
Requires:	emacs-snapshot-common = %version

Obsoletes:	gnus-emacs < 5.8.0
Provides:	gnus-emacs = 5.11.0

Conflicts:	emacs-speedbar < 1.0

Conflicts:	emacs-tramp
#Obsoletes:	emacs-tramp
#Provides:	emacs-tramp

Conflicts:	emacs-url
#Obsoletes:	emacs-url
#Provides:	emacs-url

Obsoletes:	emacs-pcomplete <= 2.4.2
Provides:	emacs-pcomplete = 1.1.1

Obsoletes:	eshell-emacs <= 2.4.2
Provides:	eshell-emacs = 2.1.2

#Obsoletes:	emacs < 22.0.50
#Provides:	emacs < 22.0.50

# conflicts due to %%_bindir/{b2m,etags,rcs-checkin}
Conflicts: xemacs-extras


%description common
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news and more without
leaving the editor.

This package includes the libraries you need to run the Emacs editor, so you
need to install this package if you intend to use Emacs. You also need to
install the actual Emacs program package (emacs-snapshot-nox or
emacs-snapshot). Install emacs-snapshot-nox if you are not going to use the X
Window System; install emacs-snapshot if you will be using X.

%prep

%if %{checkout_HEAD}
  rm -rf emacs emacs-snapshot
  cvs -z3 -d:pserver:anonymous@cvs.savannah.gnu.org:/cvsroot/emacs co emacs
  mv emacs emacs-snapshot
  tar cfj %SOURCE0 emacs-snapshot
  rm -rf emacs-snapshot
%endif

%setup -q -n emacs-%{version}

perl -p -i -e 's/ctags/gctags/g' etc/etags.1

%patch1 -p1 -b .loadup
%patch3 -p1 -b .ia64-2
%patch5 -p1 -b .bzip2
%patch6 -p1
%patch7 -p1 -b .rpath
%patch9 -p1 -b .sendmail-program

%ifarch ppc
%patch20 -p1
%patch21 -p1
%patch22 -p1
%endif

%patch100 -p1
%patch101 -p1
%patch103 -p1 -b .x86_64
%patch104 -p1
%patch111 -p1
%patch114 -p1

%build

libtoolize --force --copy
autoconf

PUREDEF="-DNCURSES_OSPEED_T"
XPUREDEF="-DNCURSES_OSPEED_T"
CONFOPTS="--prefix=%{_prefix} --libexecdir=%{_libdir} --sharedstatedir=/var --with-gcc --with-pop --mandir=%{_mandir} --infodir=%{_infodir}"

./configure ${CONFOPTS} --with-x=no ${RPM_ARCH}-mandrake-linux --libdir=%_libdir
make bootstrap

make distclean
#Build binary without X support
CFLAGS="$RPM_OPT_FLAGS $PUREDEF -fno-zero-initialized-in-bss" LDFLAGS=-s \
  ./configure ${CONFOPTS} --with-x=no ${RPM_ARCH}-mandrake-linux --libdir=%_libdir
make
mv src/emacs src/nox-emacs

make distclean
#Build binary with GTK support
CFLAGS="$RPM_OPT_FLAGS $XPUREDEF -fno-zero-initialized-in-bss" LDFLAGS=-s \
  ./configure ${CONFOPTS} --with-x-toolkit=gtk ${RPM_ARCH}-mandrake-linux --libdir=%_libdir
make
mv src/emacs src/gtk-emacs

make distclean
#Build binary with X support
CFLAGS="$RPM_OPT_FLAGS $XPUREDEF -fno-zero-initialized-in-bss" LDFLAGS=-s \
  ./configure ${CONFOPTS} --with-x-toolkit ${RPM_ARCH}-mandrake-linux --libdir=%_libdir
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr

PATH=$PATH:/sbin
ARCHDIR=${RPM_ARCH}-mandrake-linux
%old_makeinstall sharedstatedir=$RPM_BUILD_ROOT/var

rm -f $RPM_BUILD_ROOT%_bindir/emacs
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm $RPM_BUILD_ROOT%{_libdir}/emacs/%version/%_arch-mandrake-linux/fakemail
# remove sun specific stuff
rm -f $RPM_BUILD_ROOT%{_datadir}/emacs/%version/etc/{emacstool.1,emacs.1,ctags.1,etags.1,sex.6}

# move some man page to the right place
mv $RPM_BUILD_ROOT%{_datadir}/emacs/%version/etc/emacsclient.1 $RPM_BUILD_ROOT%{_mandir}/man1/

# rename ctags to gctags
mv $RPM_BUILD_ROOT%{_mandir}/man1/ctags.1 $RPM_BUILD_ROOT%{_mandir}/man1/gctags.1
mv $RPM_BUILD_ROOT%{_bindir}/ctags $RPM_BUILD_ROOT%{_bindir}/gctags

# is that needed?
install -d $RPM_BUILD_ROOT%{_libdir}/emacs/site-lisp

  
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/emacs
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start-snapshot.el
(cd $RPM_BUILD_ROOT%{_datadir}/emacs/%version/lisp; ln -s ../../../../..%{_sysconfdir}/emacs/site-start-snapshot.el site-start.el)

install -d $RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start.d


install -m755 src/nox-emacs $RPM_BUILD_ROOT%{_bindir}/emacs-nox
install -m755 src/gtk-emacs $RPM_BUILD_ROOT%{_bindir}/emacs-gtk
chmod -t $RPM_BUILD_ROOT%{_bindir}/emacs*


# Menu support
mkdir -p $RPM_BUILD_ROOT{%_menudir,%_liconsdir,%_miconsdir}
cat > $RPM_BUILD_ROOT%{_menudir}/emacs << EOF
?package(%{name}): needs=x11 section="More Applications/Editors" icon=emacs.png title=Emacs longtitle="Powerful editor" command=emacs-%version xdg="true"
EOF
cat > $RPM_BUILD_ROOT%{_menudir}/emacs-gtk << EOF
?package(%{name}-gtk): needs=x11 section="More Applications/Editors" icon=emacs-gtk.png title="Emacs gtk" longtitle="Powerful editor (using gtk)" command=emacs-gtk xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-emacs.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Emacs
Comment="Powerful editor"
Exec=emacs-%version
Icon=emacs
Terminal=false
Type=Application
Categories=TextEditor;X-MandrivaLinux-MoreApplications-Editors;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-emacs-gtk.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Emacs GTK
Comment="Powerful editor"
Exec=emacs-gtk
Icon=emacs
Terminal=false
Type=Application
Categories=TextEditor;X-MandrivaLinux-MoreApplications-Editors;
EOF

install -m 644 %SOURCE2 $RPM_BUILD_ROOT%_miconsdir/emacs.png
install -m 644 %SOURCE3 $RPM_BUILD_ROOT%_iconsdir/emacs.png
install -m 644 %SOURCE4 $RPM_BUILD_ROOT%_liconsdir/emacs.png

install -m 644 %SOURCE2 $RPM_BUILD_ROOT%_miconsdir/emacs-gtk.png
install -m 644 %SOURCE3 $RPM_BUILD_ROOT%_iconsdir/emacs-gtk.png
install -m 644 %SOURCE4 $RPM_BUILD_ROOT%_liconsdir/emacs-gtk.png



# create file lists

#
# emacs-doc file list
#
# 3.22MB of docs from emacs-common to emacs-doc to reduce size (tutorials, news, postscript files, ...)
# NB: etc/ps-prin{0,1}.ps are needed by ps-print
find $RPM_BUILD_ROOT%{_datadir}/emacs/%version/etc/ -type f | \
  egrep 'TUTORIAL\.|NEWS|ONEWS|.ps$'|fgrep -v /etc/ps-prin | \
  sed "s^$RPM_BUILD_ROOT^^" > doc-filelist

#
# emacs-el file list
#

# take every .el and .el.gz which have a corresponding .elc
find $RPM_BUILD_ROOT%{_datadir}/emacs -name '*.el' -o -name '*.el.gz' | \
  grep -v /leim/ | while read I; do
  f=`basename $I .gz`
  f=`basename $f .el`
  if [ -e `dirname $I`/$f.elc ]; then 
    echo $I | sed "s^$RPM_BUILD_ROOT^^"
  fi
done > el-filelist

# add this
echo %{_datadir}/emacs/%version/etc/termcap.src >> el-filelist

#
# emacs-common file list
#

# everything not in previous filelists, and remove a few things listed in %files
find $RPM_BUILD_ROOT%{_datadir}/emacs/%version -type f -print -o -type d -printf "%%%%dir %%p\n" | \
  grep -v /leim/ | sed "s^$RPM_BUILD_ROOT^^" > common-filelist.raw
while read I; do
  grep -qxF $I doc-filelist el-filelist || echo $I
done < common-filelist.raw > common-filelist

find $RPM_BUILD_ROOT%{_libdir}/emacs -type f -print -o -type d -printf "%%%%dir %%p\n" | \
  egrep -v 'movemail$|update-game-score$' | sed "s^$RPM_BUILD_ROOT^^" >> common-filelist


%define info_files ada-mode autotype calc ccmode cl dired-x ebrowse ediff efaq eintr elisp emacs emacs-mime erc eshell eudc flymake forms gnus idlwave info message mh-e newsticker org pcl-cvs pgg rcirc reftex sc ses sieve smtpmail speedbar tramp url vip viper widget woman

have_info_files=$(echo $(ls $RPM_BUILD_ROOT%{_infodir} | egrep -v -- '-[0-9]+$' | sort))

[ "$have_info_files" = "%info_files" ] || { 
  echo "you must modify the spec file, %%info_files should be: $have_info_files"
  exit 1
}


%clean
rm -rf $RPM_BUILD_ROOT

%post extras
# --section="GNU Emacs"
for f in %info_files; do  %_install_info $f
done
:

%preun extras
for f in %info_files; do  %_remove_install_info $f
done
:


%post nox
update-alternatives --install %_bindir/emacs emacs %_bindir/emacs-nox 9

[[ ! -f %_bindir/emacs ]] && update-alternatives --auto emacs
:

%postun nox
[[ ! -f %_bindir/emacs-nox ]] && \
    /usr/sbin/update-alternatives --remove emacs %_bindir/emacs-nox
:

%post gtk
update-alternatives --install %_bindir/emacs emacs %_bindir/emacs-gtk 29

[[ ! -f %_bindir/emacs ]] && update-alternatives --auto emacs

%{update_menus}

%postun gtk
[[ ! -f %_bindir/emacs-gtk ]] && \
    /usr/sbin/update-alternatives --remove emacs %_bindir/emacs-gtk

%{clean_menus}


%post
/usr/sbin/update-alternatives --install %_bindir/emacs emacs %_bindir/emacs-%version 19

%{update_menus}


%postun
%{clean_menus}

[[ ! -f %{_bindir}/emacs-%{version} ]] && \
    /usr/sbin/update-alternatives --remove emacs %{_bindir}/emacs-%{version}|| :


%files -f common-filelist common
%defattr(-,root,root)
%doc BUGS README src/COPYING
%{_localstatedir}/games/emacs
%dir %{_sysconfdir}/emacs/site-start.d
%dir %{_sysconfdir}/emacs
%config(noreplace) %{_sysconfdir}/emacs/site-start-snapshot.el
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/%version/lisp/site-start.el
%attr(2755,root,mail) %{_libdir}/emacs/%version/%_arch-mandrake-linux/movemail
%attr(4755,games,root) %{_libdir}/emacs/%version/%_arch-mandrake-linux/update-game-score

%files extras
%defattr(-,root,root)
%{_bindir}/b2m
%{_bindir}/emacsclient
%{_bindir}/etags
%{_bindir}/ebrowse
%{_bindir}/grep-changelog
%{_bindir}/gctags
%{_bindir}/rcs-checkin
%{_mandir}/*/*
%{_infodir}/*

%files -f doc-filelist doc
%defattr(-,root,root)

%files -f el-filelist el
%defattr(-,root,root)
%doc src/COPYING
/usr/share/emacs/%version/site-lisp/subdirs.el
/usr/share/emacs/site-lisp/subdirs.el
%{_datadir}/emacs/%version/leim/ja-dic/*.el.gz
%{_datadir}/emacs/%version/leim/quail/*.el.gz

%files leim
%defattr(-,root,root)
%doc src/COPYING
%{_datadir}/emacs/%version/leim/leim-list.el
%dir %{_datadir}/emacs/%version/leim/ja-dic
%{_datadir}/emacs/%version/leim/ja-dic/*.elc
%dir %{_datadir}/emacs/%version/leim/quail
%{_datadir}/emacs/%version/leim/quail/*.elc

%files nox
%defattr(-,root,root)
%doc src/COPYING
%{_bindir}/emacs-nox

%files gtk
%defattr(-,root,root)
%doc src/COPYING
%{_bindir}/emacs-gtk
%{_datadir}/applications/mandriva-emacs-gtk.desktop
%{_menudir}/emacs-gtk
%{_iconsdir}/emacs-gtk.png
%{_miconsdir}/emacs-gtk.png
%{_liconsdir}/emacs-gtk.png

%files
%defattr(-,root,root)
%doc src/COPYING
%{_bindir}/emacs-%version
%{_datadir}/applications/mandriva-emacs.desktop
%{_menudir}/emacs
%{_iconsdir}/emacs.png
%{_miconsdir}/emacs.png
%{_liconsdir}/emacs.png


