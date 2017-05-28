Summary:	NetworkManager VPN integration for OpenVPN
Summary(pl.UTF-8):	Integracja NetworkManagera z OpenVPN-em
Name:		NetworkManager-openvpn
Version:	1.2.10
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openvpn/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	f118226ed2bfbacfd64ac4d1e0bd0383
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.2.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gtk+3-devel >= 3.4
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libsecret-devel >= 0.18
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Provides:	group(nm-openvpn)
Provides:	user(nm-openvpn)
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	NetworkManager >= 2:1.2.0
Requires:	NetworkManager-gtk-lib >= 1.2.0
Requires:	glib2 >= 1:2.32
Requires:	gtk+3 >= 3.4
Requires:	libsecret >= 0.18
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

%pre
%groupadd -g 324 -r -f nm-openvpn
%useradd -u 324 -s /bin/false -c "Default user for running openvpn spawned by NetworkManager" -g nm-openvpn nm-openvpn

%postun
if [ "$1" = "0" ]; then
	%userremove nm-openvpn
	%groupremove nm-openvpn
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-openvpn.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-openvpn-editor.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-openvpn-properties.so
%attr(755,root,root) %{_libdir}/nm-openvpn-auth-dialog
%attr(755,root,root) %{_libdir}/nm-openvpn-service
%attr(755,root,root) %{_libdir}/nm-openvpn-service-openvpn-helper
%{_prefix}/lib/NetworkManager/VPN/nm-openvpn-service.name
%{_sysconfdir}/NetworkManager/VPN/nm-openvpn-service.name
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/nm-openvpn-service.conf
%{_datadir}/appdata/network-manager-openvpn.metainfo.xml
%{_datadir}/gnome-vpn-properties/openvpn
