Summary:	GNU Emacs text editor with X11 support
Name:		emacs
Version:	24.3
Release:	1
License:	GPLv3+
Group:		Editors
Url:		http://www.gnu.org/software/emacs/
Source0:	ftp://ftp.gnu.org/pub/gnu/emacs/emacs-%{version}.tar.xz
Source2:	gnu-mini.png
Source3:	gnu-normal.png
Source4:	gnu-large.png
Source5:	emacs-config
Patch1:		emacs-20.5-loadup.patch
Patch6:		emacs-snapshot-same-etc-DOC-for-all.patch
Patch7:		emacs-24.3-giflib5.patch

Patch100:	emacs-23.3-infofix.patch
Patch101:	emacs-23.1.92-version.patch
Patch111:	emacs-24.2-ispell-dictionaries-list-iso-8859-15.patch
Patch115:	emacs-24.2-lzma-support.patch

BuildRequires:  texinfo
BuildRequires:	x11-server-common
BuildRequires:	jpeg-devel
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xaw3d)
BuildRequires:	pkgconfig(xpm)
Requires(post,preun):	update-alternatives
Requires:	%{name}-common = %{version}
Provides:	emacs = %{version}-%{release}
Provides:	emacs-bin
Provides:	emacs-gtk

%description
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor. 

This package provides an emacs binary with support for X Windows. 

%package	el
Summary:	GNU Emacs Lisp source files
Group:		Editors
Requires:	%{name}-common = %{version}

%description	el
The emacs-snapshot-el package contains the emacs elisp sources for
many of the elisp programs included with the main Emacs text editor
package.

You need to install this package only if you intend to modify any of
the Emacs packages or see some elisp examples.

%package	doc
Summary:	GNU Emacs documentation
Group:		Editors
Requires:	%{name}-common = %{version}

%description	doc
Documentation for GNU Emacs.

%package	leim
Summary:	GNU Emacs Lisp code for international input methods
Group:		Editors
Requires:	%{name}-common = %{version}

%description	leim
This package contains Emacs Lisp code for input methods for various
international character scripts.

%package	nox
Summary:	GNU Emacs text editor without support for X11
Group:		Editors
Requires:	%{name}-common = %{version}
Provides:	emacs-bin
Requires(post,preun):	update-alternatives

%description	nox
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor. 

This package provides an emacs binary with no X Windows support for
running on a terminal.

%package	common
Summary:	Common files for GNU Emacs
Group:		Editors
Obsoletes:	emacs-cedet < 1.0-0.pre7
Provides:	emacs-cedet = 1.0-0.pre7
Obsoletes:	emacs-easypg < 1.0.0
Provides:	emacs-easypg = 1.0.0

%description	common
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor. 

This package contains all of the common files needed by emacs-snapshot
or emacs-snapshot-nox

%prep
%setup -q
%__perl -p -i -e 's/ctags/gctags/g' etc/etags.1

%patch1 -p1 -b .loadup
%patch6 -p1
%patch7 -p1

%patch100 -p1
%patch101 -p1 -b .version
%patch111 -p1

%ifarch ppc
%patch20 -p1
%patch21 -p1
%patch22 -p1
%endif

%patch115 -p1 -z .lzma-support

autoreconf -fi -I m4

%build
PUREDEF="-DNCURSES_OSPEED_T"
XPUREDEF="-DNCURSES_OSPEED_T"

export CFLAGS="$RPM_OPT_FLAGS $PUREDEF -fno-zero-initialized-in-bss"

%configure2_5x\
	--with-x=no\
	--localstatedir=%{_localstatedir}/lib
%make bootstrap

%make distclean
# Build binary without X support
%configure2_5x\
	--with-x=no\
	--localstatedir=%{_localstatedir}/lib
%make
mv src/emacs src/nox-emacs

%make distclean
# Build binary with X support
%configure2_5x\
	--with-x-toolkit\
	--localstatedir=%{_localstatedir}/lib
%make

%install
mkdir -p %{buildroot}/usr

PATH=$PATH:/sbin
ARCHDIR=%{_target_platform}
%old_makeinstall sharedstatedir=%{buildroot}/var/lib localstatedir=%{buildroot}/var/lib

rm -f %{buildroot}%_bindir/emacs
rm -f %{buildroot}%{_infodir}/dir

# remove sun specific stuff
rm -f %{buildroot}%{_datadir}/emacs/%{version}/etc/{emacstool.1,emacs.1,ctags.1,etags.1,sex.6}

# rename ctags to gctags
mv %{buildroot}%{_mandir}/man1/ctags.1.gz %{buildroot}%{_mandir}/man1/gctags.1.gz
mv %{buildroot}%{_bindir}/ctags %{buildroot}%{_bindir}/gctags

# is that needed?
install -d %{buildroot}%{_libdir}/emacs/site-lisp

mkdir -p %{buildroot}%{_sysconfdir}/emacs
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/emacs/site-start.el
(cd %{buildroot}%{_datadir}/emacs/%{version}/lisp; ln -s ../../../../..%{_sysconfdir}/emacs/site-start.el site-start.el)

install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d

install -m755 src/nox-emacs %{buildroot}%{_bindir}/emacs-nox
chmod -t %{buildroot}%{_bindir}/emacs*

#
# emacs-doc file list
#
# 3.22MB of docs from emacs-common to emacs-doc to reduce size (tutorials, news, postscript files, ...)
# NB: etc/ps-prin{0,1}.ps are needed by ps-print
find %{buildroot}%{_datadir}/emacs/%{version}/etc/ -type f | \
  egrep 'TUTORIAL\.|NEWS|ONEWS|.ps$'|fgrep -v /etc/ps-prin | \
  sed "s^%{buildroot}^^" > doc-filelist

#
# emacs-el file list
#

# take every .el and .el.gz which have a corresponding .elc
find %{buildroot}%{_datadir}/emacs -name '*.el' -o -name '*.el.gz' | \
  grep -v /leim/ | while read I; do
  f=`basename $I .gz`
  f=`basename $f .el`
  if [ -e `dirname $I`/$f.elc ]; then
    echo $I | sed "s^%{buildroot}^^"
  fi
done > el-filelist

#
# emacs-common file list
#
# everything not in previous filelists, and remove a few things listed in %files
find %{buildroot}%{_datadir}/emacs/%{version} -type f -print -o -type d -printf "%%%%dir %%p\n" | \
  grep -v /leim/ | sed "s^%{buildroot}^^" > common-filelist.raw
while read I; do
  grep -qxF $I doc-filelist el-filelist || echo $I
done < common-filelist.raw > common-filelist

find %{buildroot}%{_libdir}/emacs -type f -print -o -type d -printf "%%%%dir %%p\n" | \
  egrep -v 'movemail$|update-game-score$' | sed "s^%{buildroot}^^" >> common-filelist

# this conflicts with the info package
rm -f %{buildroot}%{_infodir}/info.info.gz

have_info_files=$(echo $(ls %{buildroot}%{_infodir} | sed -e 's/\.info\.gz$//' | egrep -v -- '-[0-9]+$' | LC_ALL=C sort))

%define info_files ada-mode auth autotype bovine calc ccmode cl dbus dired-x ebrowse ede ediff edt efaq eieio eintr elisp emacs emacs-gnutls emacs-mime epa erc ert eshell eudc flymake forms gnus htmlfontify idlwave mairix-el message mh-e newsticker nxml-mode org pcl-cvs pgg rcirc reftex remember sasl sc semantic ses sieve smtpmail speedbar srecode tramp url vip viper widget wisent woman

[ "$have_info_files" = "%info_files" ] || {
  echo "you must modify the spec file, %%info_files should be: $have_info_files"
  exit 1
}

%post nox
update-alternatives --install %_bindir/emacs emacs %_bindir/emacs-nox 10

[[ ! -f %_bindir/emacs ]] && update-alternatives --auto emacs
:

%postun nox
[[ ! -f %_bindir/emacs-nox ]] && \
    /usr/sbin/update-alternatives --remove emacs %_bindir/emacs-nox
:

%post
/usr/sbin/update-alternatives --install %_bindir/emacs emacs %_bindir/emacs-%{version} 21

%postun
[[ ! -f %{_bindir}/emacs-%{version} ]] && \
    /usr/sbin/update-alternatives --remove emacs %{_bindir}/emacs-%{version}|| :

%files -f common-filelist common
%doc BUGS README src/COPYING
%{_localstatedir}/lib/games/emacs/*
%dir %{_sysconfdir}/emacs/site-start.d
%dir %{_sysconfdir}/emacs
%config(noreplace) %{_sysconfdir}/emacs/site-start.el
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/%{version}/lisp/site-start.el
%attr(2755,root,mail) %{_libdir}/emacs/%{version}/%{_target_platform}/movemail
%attr(4755,games,root) %{_libdir}/emacs/%{version}/%{_target_platform}/update-game-score
%{_bindir}/emacsclient
%{_bindir}/etags
%{_bindir}/ebrowse
%{_bindir}/grep-changelog
%{_bindir}/gctags
%{_mandir}/*/*
%{_infodir}/*
%exclude %{_datadir}/emacs/%{version}/site-lisp/subdirs.el

%files -f doc-filelist doc

%files -f el-filelist el
%doc src/COPYING
%{_datadir}/emacs/%{version}/site-lisp/subdirs.el
%{_datadir}/emacs/site-lisp/subdirs.el
%{_datadir}/emacs/%{version}/leim/ja-dic/*.el.gz
%{_datadir}/emacs/%{version}/leim/quail/*.el.gz

%files leim
%doc src/COPYING
%{_datadir}/emacs/%{version}/leim/leim-list.el
%dir %{_datadir}/emacs/%{version}/leim/ja-dic
%{_datadir}/emacs/%{version}/leim/ja-dic/*.elc
%dir %{_datadir}/emacs/%{version}/leim/quail
%{_datadir}/emacs/%{version}/leim/quail/*.elc

%files nox
%doc src/COPYING
%{_bindir}/emacs-nox

%files
%doc src/COPYING
%{_bindir}/emacs-%{version}
%{_datadir}/applications/emacs.desktop
%{_iconsdir}/hicolor/*/apps/emacs*.png
%{_iconsdir}/hicolor/scalable/apps/emacs.svg
%{_iconsdir}/hicolor/scalable/mimetypes/emacs-document.svg
