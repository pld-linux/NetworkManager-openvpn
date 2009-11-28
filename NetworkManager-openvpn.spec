Summary:	NetworkManager VPN integration for OpenVPN
Summary(pl.UTF-8):	Integracja NetworkManagera z OpenVPN-em
Name:		NetworkManager-openvpn
Version:	0.7.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openvpn/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	b27306c0350a7060377831ab4ebe97f5
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	NetworkManager-devel >= 0.7.2
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	NetworkManager >= 0.7.2
Requires:	openvpn
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager VPN integration for OpenVPN.

%description -l pl.UTF-8
Integracja NetworkManagera z OpenVPN-em.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-openvpn-properties.so
%attr(755,root,root) %{_libdir}/nm-openvpn-auth-dialog
%attr(755,root,root) %{_libdir}/nm-openvpn-service
%attr(755,root,root) %{_libdir}/nm-openvpn-service-openvpn-helper
%{_sysconfdir}/NetworkManager/VPN/nm-openvpn-service.name
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/nm-openvpn-service.conf
%{_desktopdir}/nm-openvpn.desktop
%{_datadir}/gnome-vpn-properties/openvpn
%{_iconsdir}/hicolor/*/*/*.png
