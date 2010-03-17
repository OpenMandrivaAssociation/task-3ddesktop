%define common_packages compiz-fusion metisse

Name: task-3ddesktop
Version: 2009.1
Release: %mkrel 3
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
