Summary:	GNU Emacs text editor with X11 support

Name:		emacs
Version:	29.3
Release:	1
License:	GPLv3+
Group:		Editors
Url:		https://www.gnu.org/software/emacs/
Source0:	https://ftp.gnu.org/pub/gnu/emacs/emacs-%{version}.tar.xz
Source2:	gnu-mini.png
Source3:	gnu-normal.png
Source4:	gnu-large.png
Source5:	emacs-config
Source100:	emacs.rpmlintrc
Patch0:		emacs-28.2-clang.patch
Patch1:		emacs-28.2-l10n.patch
Patch101:	emacs-28.2-version.patch
Patch111:	emacs-29.2-ispell-dictionaries-list-iso-8859-15.patch
Patch115:	emacs-29.1-lzma-support.patch

BuildRequires:	acl-devel
BuildRequires:	git-core
BuildRequires:	giflib-devel
BuildRequires:	gomp-devel
BuildRequires:	gpm-devel
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(harfbuzz-cairo)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(jansson)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libotf)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(m17n-core)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw3d)
BuildRequires:	pkgconfig(xaw7)
#BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(webkit2gtk-4.0)
BuildRequires:	texinfo
BuildRequires:	x11-server-common

Requires(post,postun):	update-alternatives

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

%files
%doc src/COPYING
%{_bindir}/emacs-%{version}
%{_datadir}/applications/emacs*.desktop
%{_iconsdir}/hicolor/*/apps/emacs*.png
%{_iconsdir}/hicolor/scalable/apps/emacs.svg
%{_iconsdir}/hicolor/scalable/apps/emacs.ico
%{_iconsdir}/hicolor/scalable/mimetypes/emacs-document*.svg
%dir %{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/locked-encrypted.xpm
%{_metainfodir}/emacs.metainfo.xml

#----------------------------------------------------------------------

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

%files -f el-filelist el
%doc src/COPYING
%{_datadir}/emacs/%{version}/site-lisp/subdirs.el
%{_datadir}/emacs/site-lisp/subdirs.el
%{_datadir}/emacs/%{version}/lisp/leim/ja-dic/*.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/*.el.gz

#----------------------------------------------------------------------

%package	doc
Summary:	GNU Emacs documentation

Group:		Editors
Requires:	%{name}-common = %{version}

%description	doc
Documentation for GNU Emacs.

%files -f doc-filelist doc

#----------------------------------------------------------------------

%package	leim
Summary:	GNU Emacs Lisp code for international input methods

Group:		Editors
Requires:	%{name}-common = %{version}

%description	leim
This package contains Emacs Lisp code for input methods for various
international character scripts.

%files leim
%doc src/COPYING
%{_datadir}/emacs/%{version}/lisp/leim/leim-list.el
%dir %{_datadir}/emacs/%{version}/lisp/leim/ja-dic
%{_datadir}/emacs/%{version}/lisp/leim/ja-dic/*.elc
%dir %{_datadir}/emacs/%{version}/lisp/leim/quail
%{_datadir}/emacs/%{version}/lisp/leim/quail/*.elc

#----------------------------------------------------------------------

%package	nox
Summary:	GNU Emacs text editor without support for X11

Group:		Editors
Requires:	%{name}-common = %{version}
Provides:	emacs-bin
Requires(post,postun):	update-alternatives

%description	nox
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor. 

This package provides an emacs binary with no X Windows support for
running on a terminal.

%files nox
%doc src/COPYING
%{_bindir}/emacs-nox

#----------------------------------------------------------------------

%package	common
Summary:	Common files for GNU Emacs

Group:		Editors
Obsoletes:	emacs-cedet < 1.0-0.pre7
Provides:	emacs-cedet = 1.0-0.pre7
Obsoletes:	emacs-easypg < 1.0.0
Provides:	emacs-easypg = 1.0.0
Requires(post,postun):	update-alternatives

%description	common
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor. 

This package contains all of the common files needed by emacs-snapshot
or emacs-snapshot-nox

%files -f common-filelist common
%doc BUGS README src/COPYING
%dir %{_sysconfdir}/emacs/site-start.d
%dir %{_sysconfdir}/emacs
%config(noreplace) %{_sysconfdir}/emacs/site-start.el
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/%{version}/lisp/site-start.el
%attr(2755,root,mail) %{_libexecdir}/emacs/%{version}/%{_target_platform}/movemail
%{_bindir}/emacsclient
%{_bindir}/%{name}-etags
%{_bindir}/ebrowse
%{_bindir}/gctags
%{_mandir}/*/*
%{_infodir}/*
%exclude %{_datadir}/emacs/%{version}/site-lisp/subdirs.el
%{_includedir}/emacs-module.h
%{_libdir}/systemd/user/emacs.service

#----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure \
	--with-x=no \
	--localstatedir=%{_localstatedir}/lib
%make_build bootstrap

# Build binary without X support
%make_build distclean
%configure \
	--with-x=no\
	--localstatedir=%{_localstatedir}/lib
%make_build
mv src/emacs src/nox-emacs

# Build binary with X support
%make_build distclean
%configure \
	--with-gif \
	--with-imagemagick \
	--with-jpg \
	--with-json \
	--with-png \
	--with-rsvg \
	--with-tiff \
	--with-xft \
	--with-xwidgets \
	--with-x-toolkit=gtk3\
	--with-modules \
	--localstatedir=%{_localstatedir}/lib
%make_build

%install
%make_install

rm -f %{buildroot}%{_bindir}/emacs
rm -f %{buildroot}%{_infodir}/dir

# remove sun specific stuff
rm -f %{buildroot}%{_datadir}/emacs/%{version}/etc/{emacstool.1,emacs.1,ctags.1,etags.1,sex.6}

# rename ctags to gctags
mv %{buildroot}%{_mandir}/man1/ctags.1.gz %{buildroot}%{_mandir}/man1/gctags.1.gz
mv %{buildroot}%{_bindir}/ctags %{buildroot}%{_bindir}/gctags
mv -f %{buildroot}%{_bindir}/{etags,emacs-etags}

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
	grep -E 'TUTORIAL\.|NEWS|ONEWS|.ps$'|grep -F -v /etc/ps-prin | \
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

find %{buildroot}%{_libdir}/emacs %{buildroot}%{_libexecdir}/emacs -type f -print -o -type d -printf "%%%%dir %%p\n" | \
	grep -E -v 'movemail$|update-game-score$' | sed "s^%{buildroot}^^" >> common-filelist

# this conflicts with the info package
rm -f %{buildroot}%{_infodir}/info.info.gz

# info files
have_info_files=$(echo $(ls %{buildroot}%{_infodir} | sed -e 's/\.info\.gz$//' | grep -E -v -- '-[0-9]+$' | LC_ALL=C sort))

%define info_files auth autotype bovine calc ccmode cl dbus dired-x ebrowse ede ediff edt efaq eglot eieio eintr elisp emacs emacs-gnutls emacs-mime epa erc ert eshell eudc eww flymake forms gnus htmlfontify idlwave ido mairix-el message mh-e modus-themes newsticker nxml-mode octave-mode org pcl-cvs pgg rcirc reftex remember sasl sc semantic ses sieve smtpmail speedbar srecode todo-mode tramp transient url use-package vhdl-mode vip viper vtable widget wisent woman


[ "$have_info_files" = "%info_files" ] || {
	echo "you must modify the spec file, %%info_files should be: $have_info_files"
	exit 1
}

%post nox
update-alternatives --install %{_bindir}/emacs emacs %{_bindir}/emacs-nox 10

[[ ! -f %{_bindir}/emacs ]] && update-alternatives --auto emacs
:

%postun nox
[[ ! -f %{_bindir}/emacs-nox ]] && \
	/usr/sbin/update-alternatives --remove emacs %{_bindir}/emacs-nox
:

%post
/usr/sbin/update-alternatives --install %{_bindir}/emacs emacs %{_bindir}/emacs-%{version} 21

%post common
/usr/sbin/update-alternatives --install %{_bindir}/etags etags %{_bindir}/%{name}-etags 1

%postun
[[ ! -f %{_bindir}/emacs-%{version} ]] && \
	/usr/sbin/update-alternatives --remove emacs %{_bindir}/emacs-%{version}|| :

%postun common
[[ ! -f %{_bindir}/%{name}-etags ]] && \
	/usr/sbin/update-alternatives --remove etags %{_bindir}/%{name}-etags || :

