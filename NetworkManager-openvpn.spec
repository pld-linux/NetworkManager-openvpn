# TODO
# - uses openvpn user/group, but pld does not have any
#   see NetworkManager-openvpn-0.8/properties/import-export.c
#   add in openvpn.spec? switch to nobody/nobody?
Summary:	NetworkManager VPN integration for OpenVPN
Summary(pl.UTF-8):	Integracja NetworkManagera z OpenVPN-em
Name:		NetworkManager-openvpn
Version:	0.8.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openvpn/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	0995450e31d1a47c3e3767de9773b7a7
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	NetworkManager-devel >= 0.8
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	NetworkManager >= 0.8
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-openvpn-properties.so
%attr(755,root,root) %{_libdir}/nm-openvpn-auth-dialog
%attr(755,root,root) %{_libdir}/nm-openvpn-service
%attr(755,root,root) %{_libdir}/nm-openvpn-service-openvpn-helper
%{_sysconfdir}/NetworkManager/VPN/nm-openvpn-service.name
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/nm-openvpn-service.conf
%{_datadir}/gnome-vpn-properties/openvpn
