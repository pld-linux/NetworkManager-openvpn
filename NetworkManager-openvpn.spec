# TODO
# - uses openvpn user/group, but pld does not have any
#   see NetworkManager-openvpn-0.8/properties/import-export.c
#   add in openvpn.spec? switch to nobody/nobody?
Summary:	NetworkManager VPN integration for OpenVPN
Summary(pl.UTF-8):	Integracja NetworkManagera z OpenVPN-em
Name:		NetworkManager-openvpn
Version:	0.9.10.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openvpn/0.9/%{name}-%{version}.tar.xz
# Source0-md5:	e85cf325233c10a692d976d2cecdc702
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	NetworkManager-devel >= 2:0.9.10.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 0.9.10.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gtk+3-devel >= 3.4
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libsecret-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:0.9.10.0
Requires:	NetworkManager-gtk-lib >= 0.9.10.0
Requires:	dbus-glib >= 0.74
Requires:	glib2 >= 1:2.32
Requires:	gtk+3 >= 3.4
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
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-openvpn-properties.so
%attr(755,root,root) %{_libdir}/nm-openvpn-auth-dialog
%attr(755,root,root) %{_libdir}/nm-openvpn-service
%attr(755,root,root) %{_libdir}/nm-openvpn-service-openvpn-helper
%{_sysconfdir}/NetworkManager/VPN/nm-openvpn-service.name
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/nm-openvpn-service.conf
%{_datadir}/gnome-vpn-properties/openvpn
