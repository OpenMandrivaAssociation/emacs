%define _localstatedir /var/lib

Summary:	GNU Emacs text editor with X11 support

Name:		emacs
Version:	23.3
Release:	4
License:	GPLv3+
Group:		Editors
URL:		http://www.gnu.org/software/emacs/

Source0:	ftp://ftp.gnu.org/pub/gnu/emacs/emacs-%{version}.tar.bz2
Source2:	gnu-mini.png
Source3:	gnu-normal.png
Source4:	gnu-large.png
Source5:	emacs-config

Patch1: 	emacs-20.5-loadup.patch
Patch3: 	emacs-23.0.94-ia64-1.patch
Patch5:		emacs-23.0.94-bzip2.patch
Patch6:		emacs-snapshot-same-etc-DOC-for-all.patch
Patch7:		emacs-22.0.90-rpath.patch
Patch9:		emacs-22.0.90-force-sendmail-program.patch

Patch20:	emacs-20.4-ppc-config.patch
Patch21:	emacs-20.4-ppc.patch
Patch22:	emacs-21.1-omit-nocombreloc-ppc.patch

Patch100:	emacs-23.3-infofix.patch
Patch101:	emacs-23.1.92-version.patch
Patch103:	emacs-23.0.94-x86_64.patch
Patch104:	emacs-23.2-hide-toolbar.patch
Patch111:	emacs-23.1.92-ispell-dictionaries-list-iso-8859-15.patch
Patch114:	emacs-23.0.94-ppc64.patch
Patch115:	emacs-23.0.94-lzma-support.patch
Patch116:	emacs-22.3-fix-str-fmt.patch

BuildRoot:	%_tmppath/%name-root
BuildRequires:	libxaw-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	x11-server-common
BuildRequires:	libx11-devel
BuildRequires:	gcc
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	ncurses-devel
BuildRequires:	ungif-devel
BuildRequires:  texinfo
BuildRequires:	xpm-devel
BuildRequires:	gtk+2-devel

Requires(preun): update-alternatives
Requires(post):  update-alternatives

Requires:	%{name}-common = %version
Provides:	emacs = %{version}-%{release}
Provides:	emacs-bin emacs-gtk

Conflicts:	emacs-snapshot < %{version}-%{release}
Obsoletes:	emacs-gtk <= 22.3
Obsoletes:	emacs-X11 < 22.0.50
Provides:	emacs-X11 < 22.0.50

%description
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor. 

This package provides an emacs binary with support for X Windows. 

%package el
Summary:	GNU Emacs Lisp source files
Group:		Editors
Requires:	%{name}-common = %version
Conflicts:	emacs-snapshot-el

%description el
The emacs-snapshot-el package contains the emacs elisp sources for
many of the elisp programs included with the main Emacs text editor
package.

You need to install this package only if you intend to modify any of
the Emacs packages or see some elisp examples.

%package doc
Summary:	GNU Emacs documentation
Group:		Editors
Requires:	%{name}-common = %version
Conflicts:	emacs-snapshot-doc

%description doc
Documentation for GNU Emacs.

%package leim
Summary:	GNU Emacs Lisp code for international input methods
Group:		Editors
Requires:	%{name}-common = %version
Conflicts:	emacs-snapshot-leim

%description leim
This package contains Emacs Lisp code for input methods for various
international character scripts.

%package nox
Summary:	GNU Emacs text editor without support for X11
Group:		Editors
Requires:	%{name}-common = %version
Provides:	emacs-bin

Conflicts:	emacs-snapshot-nox

Requires(preun): update-alternatives
Requires(post):  update-alternatives

%description nox
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor. 

This package provides an emacs binary with no X Windows support for
running on a terminal.

%package common
Summary:	Common files for GNU Emacs
Group:		Editors

Obsoletes:	gnus-emacs < 5.13.0
Provides:	gnus-emacs = 5.13.0

Obsoletes:	emacs-cedet < 1.0-0.pre7
Provides:	emacs-cedet = 1.0-0.pre7

Conflicts:	emacs-speedbar < 1.0
Provides:	emacs-speedbar = 1.0

Obsoletes:	emacs-tramp < 2.1.18-pre
Provides:	emacs-tramp = 2.1.18-pre

Obsoletes:	emacs-url
Provides:	emacs-url

# (Lev) This doesn't look correct:
Obsoletes:	emacs-pcomplete <= 2.4.2
Provides:	emacs-pcomplete = 1.1.1

Obsoletes:	eshell-emacs <= 2.4.2
Provides:	eshell-emacs = 2.4.2

Obsoletes:	emacs-easypg < 1.0.0
Provides:	emacs-easypg = 1.0.0

Obsoletes:	emacs-erc < 5.3
Provides:	emacs-erc = 5.3

Conflicts:	emacs-snapshot-common

# conflicts due to %%_bindir/{b2m,etags,rcs-checkin}
Conflicts: xemacs-extras

%description common
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor. 

This package contains all of the common files needed by emacs-snapshot
or emacs-snapshot-nox

%prep

%setup -q -n emacs-%{version}

%__perl -p -i -e 's/ctags/gctags/g' etc/etags.1

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
%patch101 -p1 -b .version
%patch103 -p1 -b .x86_64
%patch104 -p1 -b .toolbar
%patch111 -p1
%patch114 -p1 -b .ppc
%patch115 -p1 -z .lzma-support
%patch116 -p0 -b .str

%build
autoreconf -fi

PUREDEF="-DNCURSES_OSPEED_T"
XPUREDEF="-DNCURSES_OSPEED_T"

export CFLAGS="$RPM_OPT_FLAGS $PUREDEF -fno-zero-initialized-in-bss"

%configure2_5x --with-x=no
%make bootstrap

%make distclean
# Build binary without X support
%configure2_5x --with-x=no
%make
mv src/emacs src/nox-emacs

%make distclean
# Build binary with X support
%configure2_5x --with-x-toolkit
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr

PATH=$PATH:/sbin
ARCHDIR=%{_target_platform}
%old_makeinstall sharedstatedir=%{buildroot}/var

rm -f %{buildroot}%_bindir/emacs
rm -f %{buildroot}%{_infodir}/dir
rm %{buildroot}%{_libdir}/emacs/%version/%{_target_platform}/fakemail

# remove sun specific stuff
rm -f %{buildroot}%{_datadir}/emacs/%{version}/etc/{emacstool.1,emacs.1,ctags.1,etags.1,sex.6}

# rename ctags to gctags
mv %{buildroot}%{_mandir}/man1/ctags.1 %{buildroot}%{_mandir}/man1/gctags.1
mv %{buildroot}%{_bindir}/ctags %{buildroot}%{_bindir}/gctags

# is that needed?
install -d %{buildroot}%{_libdir}/emacs/site-lisp

mkdir -p %{buildroot}%{_sysconfdir}/emacs
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/emacs/site-start.el
(cd %{buildroot}%{_datadir}/emacs/%{version}/lisp; ln -s ../../../../..%{_sysconfdir}/emacs/site-start.el site-start.el)

install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d


install -m755 src/nox-emacs %{buildroot}%{_bindir}/emacs-nox
chmod -t %{buildroot}%{_bindir}/emacs*

# create file lists

#
# emacs-doc file list
#
# 3.22MB of docs from emacs-common to emacs-doc to reduce size (tutorials, news, postscript files, ...)
# NB: etc/ps-prin{0,1}.ps are needed by ps-print
find %{buildroot}%{_datadir}/emacs/%version/etc/ -type f | \
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
find %{buildroot}%{_datadir}/emacs/%version -type f -print -o -type d -printf "%%%%dir %%p\n" | \
  grep -v /leim/ | sed "s^%{buildroot}^^" > common-filelist.raw
while read I; do
  grep -qxF $I doc-filelist el-filelist || echo $I
done < common-filelist.raw > common-filelist

find %{buildroot}%{_libdir}/emacs -type f -print -o -type d -printf "%%%%dir %%p\n" | \
  egrep -v 'movemail$|update-game-score$' | sed "s^%{buildroot}^^" >> common-filelist


%define info_files ada-mode auth autotype calc ccmode cl dbus dired-x ebrowse ede ediff edt efaq eieio eintr elisp emacs emacs-mime epa erc eshell eudc flymake forms gnus idlwave info mairix-el message mh-e newsticker nxml-mode org pcl-cvs pgg rcirc reftex remember sasl sc semantic ses sieve smtpmail speedbar tramp url vip viper widget woman
have_info_files=$(echo $(ls %{buildroot}%{_infodir} | egrep -v -- '-[0-9]+$' | sort))

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
/usr/sbin/update-alternatives --install %_bindir/emacs emacs %_bindir/emacs-%version 21

%if %mdkversion < 200900
%{update_menus}
%endif

%postun
%if %mdkversion < 200900
%{clean_menus}
%endif

[[ ! -f %{_bindir}/emacs-%{version} ]] && \
    /usr/sbin/update-alternatives --remove emacs %{_bindir}/emacs-%{version}|| :

%files -f common-filelist common
%defattr(-,root,root)
%doc BUGS README src/COPYING
%{_localstatedir}/games/emacs
%dir %{_sysconfdir}/emacs/site-start.d
%dir %{_sysconfdir}/emacs
%config(noreplace) %{_sysconfdir}/emacs/site-start.el
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/%version/lisp/site-start.el
%attr(2755,root,mail) %{_libdir}/emacs/%version/%{_target_platform}/movemail
%attr(4755,games,root) %{_libdir}/emacs/%version/%{_target_platform}/update-game-score
%{_bindir}/b2m
%{_bindir}/emacsclient
%{_bindir}/etags
%{_bindir}/ebrowse
%{_bindir}/grep-changelog
%{_bindir}/gctags
%{_bindir}/rcs-checkin
%{_mandir}/*/*
%{_infodir}/*
%exclude %{_datadir}/emacs/%{version}/site-lisp/subdirs.el

%files -f doc-filelist doc
%defattr(-,root,root)

%files -f el-filelist el
%defattr(-,root,root)
%doc src/COPYING
%{_datadir}/emacs/%{version}/site-lisp/subdirs.el
%{_datadir}/emacs/site-lisp/subdirs.el
%{_datadir}/emacs/%{version}/leim/ja-dic/*.el.gz
%{_datadir}/emacs/%{version}/leim/quail/*.el.gz

%files leim
%defattr(-,root,root)
%doc src/COPYING
%{_datadir}/emacs/%{version}/leim/leim-list.el
%dir %{_datadir}/emacs/%{version}/leim/ja-dic
%{_datadir}/emacs/%{version}/leim/ja-dic/*.elc
%dir %{_datadir}/emacs/%{version}/leim/quail
%{_datadir}/emacs/%{version}/leim/quail/*.elc

%files nox
%defattr(-,root,root)
%doc src/COPYING
%{_bindir}/emacs-nox

%files
%defattr(-,root,root)
%doc src/COPYING
%{_bindir}/emacs-%{version}
%{_datadir}/applications/emacs.desktop
%{_iconsdir}/hicolor/*/apps/emacs*.png
%{_iconsdir}/hicolor/scalable/apps/emacs.svg
%{_iconsdir}/hicolor/scalable/mimetypes/emacs-document.svg


%changelog
* Thu May 12 2011 Funda Wang <fwang@mandriva.org> 23.3-1mdv2011.0
+ Revision: 673925
- new version 23.3
  rediff infofix patch
  gtk menus patch dropped, fix in other ways by upstream

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 23.2-3
+ Revision: 664133
- mass rebuild

* Fri Aug 06 2010 Funda Wang <fwang@mandriva.org> 23.2-2mdv2011.0
+ Revision: 567184
- conflicts with snapshot package
- merge snapshot branch into 23.2 stable

* Tue Apr 20 2010 Oden Eriksson <oeriksson@mandriva.com> 23.1-14mdv2010.1
+ Revision: 537034
- P119: security fix for CVE-2010-0825 (ubuntu)

* Thu Mar 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 23.1-13mdv2010.1
+ Revision: 518049
- only enable toobar for gtk emacs

* Fri Feb 19 2010 Lev Givon <lev@mandriva.org> 23.1-12mdv2010.1
+ Revision: 507945
- Add patch from Fedora bug #517272 to fix Mdv bug #52794.

* Fri Feb 19 2010 Lev Givon <lev@mandriva.org> 23.1-11mdv2010.1
+ Revision: 507936
- Enable toolbar by default (#49289).

* Thu Feb 18 2010 Lev Givon <lev@mandriva.org> 23.1-10mdv2010.1
+ Revision: 507887
- Obsolete emacs-easypg < 1.0.0.

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - add suggests on -doc package (bug #57575)

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 23.1-8mdv2010.1
+ Revision: 488750
- rebuilt against libjpeg v8

* Tue Oct 13 2009 Lev Givon <lev@mandriva.org> 23.1-7mdv2010.0
+ Revision: 457187
- Obsolete emacs-erc < 5.3 (#54408).

* Tue Oct 06 2009 Pascal Terjan <pterjan@mandriva.org> 23.1-6mdv2010.0
+ Revision: 454364
- Add P117 fixing Gtk menus not refreshing

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 23.1-5mdv2010.0
+ Revision: 416651
- rebuilt against libjpeg v7

* Mon Aug 03 2009 GÃ¶tz Waschk <waschk@mandriva.org> 23.1-4mdv2010.0
+ Revision: 408332
- obsolete more subpackages of emacs-snapshot

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 23.1-3mdv2010.0
+ Revision: 408228
- enable upgrading from emacs-snahot < %%version (#52616)

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 23.1-2mdv2010.0
+ Revision: 408181
- stop loading auto-show on startup

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 23.1-1mdv2010.0
+ Revision: 408099
- new release
- drop mandriva menu entry (using upstream one)
- drop gtk build (standard emacs now use gtk+)
- merge some of the adjustments made by Lev Givon in emacs-snapshot

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 22.3-4mdv2009.1
+ Revision: 366757
- fix str fmt
- rediff ppc64
- rediff toolbar patch
- rediff version patch
- rediff bzip2 patch

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

  + JÃ©rÃ´me Soyer <saispo@mandriva.org>
    - Rebuild for 2009.1

  + Pixel <pixel@mandriva.com>
    - obsolete/provide emacs-tramp (should have been done long ago)

* Thu Sep 11 2008 Pixel <pixel@mandriva.com> 22.3-2mdv2009.0
+ Revision: 283838
- do not force stripping, otherwise emacs-debug is empty (#43291)

* Sat Sep 06 2008 Frederik Himpe <fhimpe@mandriva.org> 22.3-1mdv2009.0
+ Revision: 281838
- Update ot new version 22.3
- Remove CVE-2008-1694 and CVE-2008-2142, they were integrated
  upstream
- Use %%{buildroot} instead of $RPM_BUILD_ROOT in SPEC

* Fri Aug 29 2008 Pixel <pixel@mandriva.com> 22.2-12mdv2009.0
+ Revision: 277372
- adapt/fix %%info_files

  + Frederik Himpe <fhimpe@mandriva.org>
    - Update to new version 22.2
    - Remove patches integrated upstream
    - Rediff infofix patch

* Wed Aug 20 2008 Funda Wang <fwang@mandriva.org> 22.1-12mdv2009.0
+ Revision: 274358
- add patch fixing CVE-2008-2142

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 22.1-11mdv2009.0
+ Revision: 267853
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Thierry Vignaud <tv@mandriva.org> 22.1-9mdv2009.0
+ Revision: 218042
- fix build with _localstatedir
- rebuild

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Wed May 07 2008 Pixel <pixel@mandriva.com> 22.1-8mdv2009.0
+ Revision: 202778
- fix CVE-2008-1694 (#40613)

* Fri Feb 08 2008 Pixel <pixel@mandriva.com> 22.1-7mdv2008.1
+ Revision: 163963
- Patch23: security fix for CVE-2007-5795
- Patch24: security fix for CVE-2007-6109

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 01 2007 Funda Wang <fwang@mandriva.org> 22.1-6mdv2008.1
+ Revision: 114306
- fix desktop files

* Mon Sep 17 2007 Pixel <pixel@mandriva.com> 22.1-5mdv2008.0
+ Revision: 89234
- fix a segfault loading a gif (in gnus) (reported upstream)
- cleanup spec: factorize some variables

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 22.1-4mdv2008.0
+ Revision: 70209
- kill file require on update-alternatives

* Fri Aug 10 2007 Pixel <pixel@mandriva.com> 22.1-3mdv2008.0
+ Revision: 61612
- lzma support (in jka-compr and info)

* Thu Jun 07 2007 Pixel <pixel@mandriva.com> 22.1-2mdv2008.0
+ Revision: 36482
- obsolete & provide emacs-url (we have emacs-url-2001.11.08 in contrib)
- stable release 22.1
- replacing with emacs-snapshot
- new release, pretest 22.0.99
- new pretest release, 22.0.98

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags


* Thu Mar 01 2007 Pixel <pixel@mandriva.com> 22.0.94-1.20070301.1mdv2007.0
+ Revision: 130584
- new cvs version (fixes shell when prefer-coding-system 'utf-8)

* Thu Mar 01 2007 Pixel <pixel@mandriva.com> 22.0.94-1.20070223.1mdv2007.1
+ Revision: 130475
- disable pc-selection-mode (#28765)
  (it was not really enabled in emacs 21.4 (why?), so no "regression")
- new release (22.0.94 pretest)
- adapt some patches
- fix typo

* Mon Nov 20 2006 Thierry Vignaud <tvignaud@mandriva.com> 22.0.90-2.20061117.1mdv2007.1
+ Revision: 85619
- s/mandrake/mandriva/

  + Pixel <pixel@mandriva.com>
    - svn version

* Fri Nov 17 2006 Pixel <pixel@mandriva.com> 22.0.90-1mdv2007.1
+ Revision: 85141
- new release. update patches
- new release (22.0.90 pretest)
- adapt some patches

* Mon Sep 18 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 21.4-26mdv2007.0
- Rebuild

* Wed Aug 30 2006 Pixel <pixel@mandriva.com> 22.0.50-0.20060811.5mdv2007.0
+ Revision: 58608
- re-introduce patch9 (sendmail-program is *not* computed at runtime)
- Import emacs-snapshot

* Fri Aug 25 2006 Pixel <pixel@mandriva.com> 22.0.50-0.20060811.4mdv2007.0
- add BuildRequires libxaw-devel (Xaw3d-devel is not enough)

* Thu Aug 24 2006 Pixel <pixel@mandriva.com> 22.0.50-0.20060811.3mdv2007.0
- lower the priority for alternatives so that stable emacs is preferred

* Wed Aug 23 2006 Pixel <pixel@mandriva.com> 22.0.50-0.20060811.2mdv2007.0
- BuildRequires libx11-devel instead of XFree86-devel
- move files conflicting with stable emacs in emacs-snapshot-extras
  (allowing having both emacs-snapshot and stable emacs)

* Mon Aug 14 2006 Pixel <pixel@mandriva.com> 21.4-25mdv2007.0
- replace Prereq with Requires(post) and Requires(postun)
- remove useless provides
- switch to XDG menu

* Sat Aug 12 2006 Pixel <pixel@mandriva.com> 22.0.50-0.20060811.1mdv2007.0
- new snapshot (alas not fixing ediff-buffers)
- drop patch modifying BASE_PURESIZE (no more needed)

* Sat Jul 08 2006 Pixel <pixel@mandriva.com> 22.0.50-0.20060707.1mdv2007.0
- new snapshot
- switch to XDG menu
- add 30 bytes to BASE_PURESIZE (one needs at least 1210528 bytes)

* Fri Mar 31 2006 Pixel <pixel@mandriva.com> 22.0.50-0.20060330.1mdk
- new snapshot

* Fri Jan 13 2006 Pixel <pixel@mandriva.com> 22.0.50-0.20060113.1mdk
- conflicts with emacs-speedbar < 1.0 (esp. for emacs-speedbar 0.14 in contrib which is nolonger compatible)
- provides emacs-bin (and not emacs-snapshot-bin) to allow building other packages with this snapshot version
  (thanks to Nick Brown)
- new snapshot
- drop patch workaround-non-ascii-chars-in-rfc2231 (applied upstream)

* Fri Jan 13 2006 Pixel <pixel@mandriva.com> 21.4-24mdk
- patch 116: mouse-wheel-mode by default under X (backport from emacs CVS) (#16116)

* Sun Jan 08 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 21.4-23mdk
- Rebuild

* Wed Nov 23 2005 Pixel <pixel@mandriva.com> 22.0.50-0.20051122.3mdk
- conflicts with emacs-tramp and emacs-url (to replace with obsolete/provide when emacs-snapshot is stable)
- add a menu entry for emacs-gtk 
  (thanks to Nick Brown)

* Wed Nov 23 2005 Pixel <pixel@mandriva.com> 22.0.50-0.20051122.2mdk
- don't obsolete/provide stable emacs, only conflict with it
- better release
- add BuildRequires gtk+2-devel

* Tue Nov 22 2005 Pixel <pixel@mandriva.com> 22.0.50-0.20051122mdk
- dropped patch0: need more checking (what is MH??)
- dropped patch8: no more needed (?)
- dropped patch9: not needed anymore since it sendmail-program is now computed at runtime
- dropped patch102, patch105, patch106, patch107, patch112, patch115: applied upstream
- dropped patch108: partially applied upstream (is that enough?)
- dropped patch113: not needed anymore (was applied)
- dropped patch109: the patched regexp is no more
- refresh patch100, patch111
- dropped patch110: not needed anymore (why?)
- drop cperl-mode from CPAN which is not compatible anymore, use this version
- rename emacs to emacs-common and emacs-X11 to emacs
- new pkg emacs-gtk
- don't use %%make, it causes weird locks
- simplify build (inspiration: debian)
- put back TUTORIAL in emacs-common so that the spash screen is not empty
- cleanup file list creation
- add patch10 to workaround-non-ascii-chars file attachment name (gnus)

* Wed Nov 16 2005 Thierry Vignaud <tvignaud@mandriva.com> 21.4-22mdk
- patch 115: fix flyspell (#19767)
- remove X defaults (Nick Brown, #10168)

* Tue Oct  4 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 21.4-21mdk
- ppc64 support

* Thu Apr 28 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.4a-20mdk
- new release
- kill patch 114 (merged upstream)

* Wed Feb 16 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-20mdk
- patch 114: security update for CAN-2005-0100 (#13682)

* Mon Jan 17 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-19mdk
- patch 113: fix build with newer Xaw3d

* Tue Dec 21 2004 Pixel <pixel@mandrakesoft.com> 21.3-18mdk
- macro IsModifierKey() from <X11/Xutil.h> depends on XK_XKB_KEYS which is defined in <X11/keysym.h>,
  so include <X11/keysym.h> before <X11/Xutil.h>.
  This fixes AltGr not being a modifier anymore after rebuilding with Xorg

* Fri Dec 17 2004 Pixel <pixel@mandrakesoft.com> 21.3-17mdk
- change ispell dictionnaries list to use iso-8859-15 instead of iso-8859-1
  (fixes "Ispell misalignment" errors when using emacs so called 
   "Latin-9 language environment" as displayed by C-h C-l)
  (there are some encoding unification problems in emacs between iso-8859-1
  and iso-8859-15 charsets, being the same character represented differently in
  the emacs internal mule encoding)

* Tue Nov  9 2004 Pixel <pixel@mandrakesoft.com> 21.3-16mdk
- put latest cperl-mode and modify anonymous block indentation when
  cperl-indent-parens-as-block is set

* Fri Aug 20 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-15mdk
- split doc subpackage (#6650)
- typo fix in menu entry

* Mon Aug 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 21.3-14mdk
- Rebuild with new menu

* Wed Aug  4 2004 Frederic Lepied <flepied@mandrakesoft.com> 21.3-13mdk
- use aspell by default

* Thu Jul 15 2004 Pixel <pixel@mandrakesoft.com> 21.3-12mdk
- really fix the broken sent mail syndrom:
  - force sendmail-program to "/usr/sbin/sendmail" instead of looking on the build host
    and defaulting on fakemail which sendmail is not installed
  - remove this stupid fakemail which doesn't handle /bin/mail properly

* Thu Jul 08 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-11mdk
- rebuild with gcc-3.4.1 (hopefully fixing bugs)

* Fri Jul 02 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-10mdk
- build release
- prevent problem with gcc-3.4

* Thu Feb 12 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-9mdk
- fix unpackaged file

* Tue Feb 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-8mdk
- really apply patch 108 (fix removed file when canceling saving due to coding
  charset change)

* Mon Dec 01 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-7mdk
- source 5: enable to disable auto-fill (pixel)
- patch 105: fix raw-text coding problem
- patch 106: ACPI support in battery.el
- patch 107: do not hang if scroll-margin is set to non-0 
- patch 108: fix backup renaming to the original file when the coding system of
             the buffer has changed and saving has been canceled.
- patch 108: fix dired mode regarding br locale

* Wed Aug 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-6mdk
- build release

* Thu Jun 05 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-5mdk
- /usr/X11R6/lib/X11/app-defaults/Emacs: fix default encoding (#3224)

* Mon May 26 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-4mdk
- fix obsoletes/provides for new gnus

* Tue May 20 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-3mdk
- distlint fixes
- fix doble listing on --short-circuit

* Wed May 14 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-2mdk
- rebuild

* Tue Apr 01 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.3-1mdk
- new release

* Mon Jan 20 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2.93-1mdk
- new release
- fix unpackaged files
- add ebrowse (only info was present)

* Wed Nov 13 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2.92-1mdk
- new release
- fix url

* Thu Oct 31 2002 Stefan van der Eijk <stefan@eijk.nu> 21.2.91-3mdk
- BuildRequires: texinfo

* Mon Oct 28 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2.91-2mdk
- reduce recursion numbers while installing

* Thu Oct 10 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2.91-1mdk
- new pre version

* Sun Aug 18 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2-12mdk
- emacs-nox: always return 0 in scripts

* Sat Aug 10 2002 Pixel <pixel@mandrakesoft.com> 21.2-11mdk
- emacs-config: set default-major-mode to text-mode, not initial-major-mode (which is *scratch*)
  (thanks to huug)

* Fri Aug  9 2002 Pixel <pixel@mandrakesoft.com> 21.2-10mdk
- add hide-toolbar.patch: remove the toolbar inside emacs binary so that
there's no resizing of the window when the tool-bar is removed (as reported by
Thierry SAURA)

* Thu Aug  8 2002 Pixel <pixel@mandrakesoft.com> 21.2-9mdk
- emacs-config: remove the toolbar

* Mon Jul 22 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2-8mdk
- remove non applied patches (2, 4 and 6)
- fix configure-without-libdir-spec
- don't use useless subshell

* Tue Jul  9 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 21.2-7mdk
- Nuke BuildRequires: autoconf, smtpdaemon

* Fri Jun 07 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2-6mdk
- disable alt-meta patch

* Fri Apr 12 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2-5mdk
- add || : after update-alternative in  %%postun X11 in order to prevent
  this script to fail in case of alternatives problems, just like other
  %%postun
- faster regexps for building file lists
- leave ps-prin{0,1}.ps in main package for ps-print-buffer (Goetz Waschk)

* Mon Apr 08 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2-4mdk
- fix emacs-nox %%post

* Fri Apr 05 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2-3mdk
- fix %%clean to be --short-circuit aware
- enhance scripts readability :
	- use %%update_menus and %%postun in scripts
	- use info install macros
	- simplify a lot info pages managment in scripts
	- simplify tests
- remove sun specific man page emacstool(1) on Goetz Waschk request
- move 3.22b of docs from emacs to emacs-el to reduce emacs core size
 (tutorials, news, postscript files, ...)' 

* Tue Apr 02 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2-2mdk
- update browse-url.el : 
    * Fixes support for mozilla,
    * adds support for galeon,
    * and defaults to free browsers when available,
      rather than just trying netscape
- version indicates that the Mandrake package of Emacs has been
  altered by Mandrake (patch101)
- fix emacs(1) to reflect current installation path, not /usr/local
  (patch100)
- move emacsclient man page to the right dir (Goetz Waschk)
- by the way, move also emacstool(1) and gfdl(1) in %%_mandir/man1
- s!PACKAGE_VERSION!version!g

* Tue Mar 26 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2-1mdk
- new release

* Sat Mar  2 2002 Frederic Lepied <flepied@mandrakesoft.com> 21.1-10mdk
- corrected upgrade (update-alternatives pb)

* Thu Feb 28 2002 Juan Quintela <quintela@mandrakesoft.com> 21.1-9mdk
- Gnus info files back :)

* Sun Feb 17 2002 Stefan van der Eijk <stefan@eijk.nu> 21.1-8mdk
- BuildRequires

* Sun Feb  3 2002 Frederic Lepied <flepied@mandrakesoft.com> 21.1-7mdk
- rebuild

* Thu Jan 31 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.1-6mdk
- xpm -> png icons

* Mon Nov 26 2001 Stew Benedict <sbenedict@mandrakesoft.com> 21.1-5mdk
- patch to use autoconf-2.13, PPC patch, no combreloc linker option

* Mon Nov 19 2001 Frederic Lepied <flepied@mandrakesoft.com> 21.1-4mdk
- removed lesstif support as some functions are unimplemented (for removing
menu-bar).

* Fri Nov 16 2001 Frederic Lepied <flepied@mandrakesoft.com> 21.1-3mdk
- build with lesstif (Thomas LECLERC).
- turn on color event in term mode (Chmouel)
- correct the (de)compression activation.
- use %%old_makeinstall

* Tue Oct 23 2001 Frederic Lepied <flepied@mandrakesoft.com> 21.1-2mdk
- obsoletes: gnus-emacs <= 5.9.0
 obsoletes: emacs-pcomplete <= 2.4.2
 obsoletes: eshell-emacs <= 2.4.2

* Mon Oct 22 2001 Frederic Lepied <flepied@mandrakesoft.com> 21.1-1mdk
- 21.1

* Fri Oct 12 2001 Frederic Lepied <flepied@mandrakesoft.com> 20.7-21mdk
- rebuild to fix locale problem.

* Thu Oct 11 2001 Frederic Lepied <flepied@mandrakesoft.com> 20.7-20mdk
- rebuild as it seems that the upload has broken the archives...

* Thu Oct 11 2001 Frederic Lepied <flepied@mandrakesoft.com> 20.7-19mdk
- correct nox version to not require /usr/X11R6/lib/X11/locale/locale.alias (#5719).

* Fri Sep 28 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 20.7-18mdk
- Correct font for Euro support.

* Tue Jul 17 2001 Frederic Lepied <flepied@mandrakesoft.com> 20.7-17mdk
- fixed build

* Tue Apr  3 2001 Frederic Lepied <flepied@mandrakesoft.com> 20.7-16mdk
- added loading of jka-compr, save-place and auto-show to default config.

* Wed Mar 14 2001 Frederic Lepied <flepied@mandrakesoft.com> 20.7-15mdk
- oops. really apply patches.

* Tue Mar 13 2001 Frederic Lepied <flepied@mandrakesoft.com> 20.7-14mdk
- corrected mh patch (#2010)

* Mon Feb 26 2001 Francis Galiegue <fg@mandrakesoft.com> 20.7-13mdk
- Patch merge from RHm fixes build on ia64

* Sun Jan 21 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 20.7-12mdk
- Rebuild with last ncurses.

* Mon Dec 11 2000 Pixel <pixel@mandrakesoft.com> 20.7-11mdk
- modify emacs-config (source5): as show-paren-mode without arg is a toggle,
using (show-paren-mode t) is better

* Sun Oct 15 2000 David BAUDENS <baudens@mandrakesoft.com> 20.7-10mdk
- Fix build for PPC

* Tue Sep 05 2000 David BAUDENS <baudens@mandrakesoft.com> 20.7-9mdk
- Don't apply patch #21 (PPC)

* Thu Aug 24 2000 Pixel <pixel@mandrakesoft.com> 20.7-8mdk
- really remove gnus info files

* Thu Aug 24 2000 Pixel <pixel@mandrakesoft.com> 20.7-7mdk
- remove gnus info files (now in package gnus, maybe also remove gnus from emacs?)

* Thu Aug 17 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.7-6mdk
- config file in noreplace mode.
- laod config files in /etc/emacs/site-start.d

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.7-5mdk
- automatically added BuildRequires

* Thu Jul 20 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.7-4mdk
- removed rpath.
- BM
- corrected resources for cursor and pointer.

* Mon Jul 10 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.7-3mdk
- removed trigger scripts

* Fri Jul  7 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.7-2mdk
- corrected resources to be used only for emacs and not for xemacs.
- use update-alternatives

* Thu Jun 15 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.7-1mdk
- 20.7

* Fri May 26 2000 David BAUDENS <baudens@mandrakesoft.com> 20.6-11mdk
- Reput X ressources in odd directory (make XEmacs horrible)

* Fri May 26 2000 Adam Lebsack <adam@mandrakesoft.com> 20.6-10mdk
- PPC patches

* Tue May 23 2000 David BAUDENS <baudens@mandrakesoft.com> 20.6-9mdk
- Fix app-defaults

* Fri Apr 28 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.6-8mdk
- put all size of icons.

* Wed Apr 19 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.6-7mdk
- security patch.

* Wed Apr 19 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.6-6mdk
- rebuild to correct bad paths.

* Tue Apr 18 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.6-5mdk
- colors from resource file not from lisp file.

* Mon Apr  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 20.6-4mdk
- Fix menu.
- Add Xaw3d-devel as buildrequires.

* Sat Apr  1 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.6-3mdk
- added a patch to support more than 5 buttons (David M. Cooke).
- changed default setup.
- menu

* Tue Mar  7 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.6-2mdk
- map META on ALT.

* Mon Feb 28 2000 Frederic Lepied <flepied@mandrakesoft.com> 20.6-1mdk
- version 20.6.
- move .emacs stuff from etcskel to /etc/emacs/site-start.el

* Mon Dec 20 1999 Frederic Lepied <flepied@mandrakesoft.com> 20.5-3mdk
- corrected expand.el bug.
- remove bit t on emacs executable.

* Mon Dec 13 1999 Frederic Lepied <flepied@mandrakesoft.com>
- bunzip info files

* Mon Dec 6 1999 Frederic Lepied <flepied@mandrakesoft.com>
- 20.5

* Mon Nov 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- s/i386/%%\_arch/.

* Tue Nov 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- s/gz/bz2/

* Tue Nov 09 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Wed Oct 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Clean up specs and %%post.

* Mon Jul 19 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 20.4
- remove the emacs shell script; it's no longer needed.
- adapt patches

* Fri Jul  9 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix shell-script typo bugs.

* Wed May 26 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- move the /usr/bin/emacs script to the emacs package

* Wed May 26 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- s/arch-redhat-linux/arch-mandrake-linux
- replace emacs with a shell script that runs either emacs-nox or
  emacs-20.3
- s/emacs/emacs-20.3/ in emacs.wmconfig (wmconfig is always X)

* Fri Apr 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adpatations.
- Bzip2 info/man pages.
- Path to handle bzip2 on info files.

* Wed Mar 31 1999 Preston Brown <pbrown@redhat.com>
- updated mh-utils emacs lisp file to match our nmh path locations

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 9)

* Fri Feb 26 1999 Cristian Gafton <gafton@redhat.com>
- linker scripts hack to make it build on the alpha

* Fri Jan  1 1999 Jeff Johnson <jbj@redhat.com>
- add leim package (thanks to Pavel.Janik@inet.cz).

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Wed Sep 30 1998 Cristian Gafton <gafton@redhat.com>
- backed up changes to uncompress.el (it seems that the one from 20.2 works
  much better)

* Mon Sep 28 1998 Jeff Johnson <jbj@redhat.com>
- eliminate /tmp race in rcs2log

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- upgrade to 20.3

* Tue Jun  9 1998 Jeff Johnson <jbj@redhat.com>
- add --with-pop to X11 compile.
- include contents of /usr/share/.../etc with main package.

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Mon Jun 01 1998 David S. Miller <davem@dm.cobaltmicro.com>
- fix signals when linked with glibc on non-Intel architectures
  NOTE: This patch is not needed with emacs >20.2

* Thu May 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- added /usr/lib/emacs/20.2/*-mandrake-linux directory in the filelist

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- alpha started to like emacs-nox again :-)

* Thu Nov  6 1997 Michael Fulbright <msf@redhat.com>
- alpha just doesnt like emacs-nox, taking it out for now

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- added multibyte support back into emacs 20.2
- added wmconfig for X11 emacs
- fixed some errant buildroot references

* Thu Oct 23 1997 Michael Fulbright <msf@redhat.com>
- joy a new version of emacs! Of note - no lockdir any more.
- use post/preun sections to handle numerous GNU info files

* Mon Oct 06 1997 Erik Troan <ewt@redhat.com>
- stopped stripping it as it seems to break things

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- turned off ecoff support on the Alpha (which doesn't build anymore)

* Mon Jun 16 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Fri Feb 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved ctags to gctags to fit in the more powerful for C (but less
  general) exuberant ctags as the binary /usr/bin/ctags and the
  man page /usr/man/man1/ctags.1
