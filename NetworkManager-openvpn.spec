Summary:	NetworkManager VPN integration for OpenVPN
Name:		NetworkManager-OpenVPN
Version:	0.7
%define		_rev rev3104
Release:	0.%{_rev}.1
License:	GPL
Group:		X11/Applications
Source0:	NetworkManager-%{version}%{_rev}.tar.bz2
# Source0-md5:	261b0672dfd21d5a99cbaae12e502006
URL:		http://www.gnome.org/projects/NetworkManager/
BuildRequires:	GConf2-devel
BuildRequires:	NetworkManager-applet-devel >= 0.7
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.72
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	NetworkManager-applet >= 0.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
NetworkManager VPN integration for OpenVPN.

%prep
%setup -q -n NetworkManager-%{version}%{_rev}

%build
cd vpn-daemons/openvpn
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C vpn-daemons/openvpn install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang NetworkManager-openvpn

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f NetworkManager-openvpn.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nm-openvpn-service
%attr(755,root,root) %{_bindir}/nm-openvpn-service-openvpn-helper
%attr(755,root,root) %{_libdir}/libnm-openvpn-properties.so*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libexecdir}/nm-openvpn-auth-dialog
%{_sysconfdir}/NetworkManager/VPN/nm-openvpn-service.name
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/nm-openvpn-service.conf
%{_desktopdir}/nm-openvpn.desktop
%{_datadir}/gnome-vpn-properties/openvpn
%{_iconsdir}/hicolor/*/*/*.png
