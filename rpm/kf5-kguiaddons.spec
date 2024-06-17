%global kf5_version 5.116.0

Name: opt-kf5-kguiaddons
Version: 5.116.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 1 addon with various classes on top of QtGui

License: GPLv2+ and LGPLv2+
URL:     https://invent.kde.org/frameworks/kguiaddons

Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros >= %{kf5_version}
BuildRequires: plasma-wayland-protocols-devel
BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qtbase-private-devel
BuildRequires: opt-qt5-qtwayland-devel
BuildRequires: pkgconfig(wayland-client)

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui
Requires: opt-qt5-qtwayland

%description
KGuiAddons provides convenience classes on top of QtGui.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5 -DWITH_X11=OFF
%cmake_build

%install
%cmake_install


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_bindir}/kde-geo-uri-handler
%{_opt_kf5_datadir}/qlogging-categories5/*categories
%{_opt_kf5_libdir}/libKF5GuiAddons.so.*
%{_opt_kf5_datadir}/applications/*-handler.desktop

%files devel
%{_opt_kf5_includedir}/KF5/KGuiAddons/
%{_opt_kf5_libdir}/libKF5GuiAddons.so
%{_opt_kf5_libdir}/cmake/KF5GuiAddons/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KGuiAddons.pri
