%define common_packages compiz-fusion metisse

Name: task-3ddesktop
Version: 2011.0
Release: %mkrel 1
Summary: Metapackage for 3D desktop
Group: System/X11
License: GPL
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running 3D desktop.

%package kde
Summary: Metapackage for 3D desktop in KDE environment
Group: System/X11
Requires: %{common_packages}
Requires: compiz-decorator-kde4 compiz-decorator-gtk
Obsoletes: task-3ddesktop

%description kde
This package is a meta-package, meaning that its purpose is to contain
dependencies for running 3D desktop in the KDE environment.

%package gtk
Summary: Metapackage for 3D desktop in GTK environment
Group: System/X11
Requires: %{common_packages}
Requires: compiz-decorator-gtk

%description gtk
This package is a meta-package, meaning that its purpose is to contain
dependencies for running 3D desktop in the GTK environment.

%files kde
%files gtk


%changelog
* Tue Apr 19 2011 Antoine Ginies <aginies@mandriva.com> 2011.0-1mdv2011.0
+ Revision: 655950
- bumpo t 2011 release

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2009.1-4mdv2011.0
+ Revision: 607974
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2009.1-3mdv2010.1
+ Revision: 524161
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.1-2mdv2010.0
+ Revision: 427281
- rebuild

* Sun Nov 30 2008 Thierry Vignaud <tv@mandriva.org> 2009.1-1mdv2009.1
+ Revision: 308652
- drop require on x11-server-xgl

* Tue Jun 24 2008 Olivier Blin <oblin@mandriva.com> 2009.0-1mdv2009.0
+ Revision: 228565
- use compiz-decorator-kde4 for the kde task package

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2008.1-2mdv2009.0
+ Revision: 225611
- rebuild

* Thu Mar 13 2008 Olivier Blin <oblin@mandriva.com> 2008.1-1mdv2008.1
+ Revision: 187516
- split as task-3ddesktop-kde and task-3ddesktop-gtk

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2008.0-0.3mdv2008.1
+ Revision: 179635
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Olivier Blin <oblin@mandriva.com> 2008.0-0.2mdv2008.0
+ Revision: 60452
- require compiz-fusion instead of compiz

* Wed Jul 11 2007 Olivier Blin <oblin@mandriva.com> 2008.0-0.1mdv2008.0
+ Revision: 51303
- 2008.0
- do not require fusion packages yet, they are in contrib

  + Colin Guthrie <cguthrie@mandriva.org>
    - Update for Compiz Fusion


* Wed Mar 28 2007 Olivier Blin <oblin@mandriva.com> 2007.1-0.2mdv2007.1
+ Revision: 149202
- require compiz-decorator-kde and compiz-decorator-gtk

* Wed Feb 07 2007 Olivier Blin <oblin@mandriva.com> 2007.1-0.1mdv2007.1
+ Revision: 117024
- require compiz and metisse
- require the compositing-wm virtual provides
- Import task-3ddesktop

* Sun Aug 20 2006 Olivier Blin <blino@mandriva.com> 2007-1mdv2007.0
- initial Mandriva release

