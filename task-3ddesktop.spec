Name: task-3ddesktop
Version: 2007.1
Release: %mkrel 0.3
Summary: Metapackage for 3D desktop
Group: System/X11
License: GPL
Requires: x11-server-xgl
Requires: compiz
#Requires: compiz-fusion-main compiz-fusion-extra
Requires: compiz-decorator-kde compiz-decorator-gtk
#Requires: emerald
#Requires: ccsm
Requires: metisse
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running 3D desktop.

%files


