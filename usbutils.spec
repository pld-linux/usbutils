Summary:	Linux USB utilities
Summary(pl):	Linuksowe narzêdzia do USB
Name:		usbutils
Version:	0.8
Release:	2
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(pl):	Aplikacje/System
Group(pt_BR):	Aplicações/Sistema
Source0:	http://usb.in.tum.de/download/usbutils/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_prefix}/share/misc

%description
usbutils contains a utility for inspecting devices connected to the
USB bus. It requires a Linux kernel version 2.3.15 or newer
(supporting the '/proc/bus/usb' interface).

%description -l pl
Pakiet usbutils zawiera narzêdzie do przegl±dania urz±dzeñ
pod³±czonych do szyny USB. Wymaga j±dra w werji 2.3.15 lub nowszej (z
obs³ug± interfejsu /proc/bus/usb).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%{_datadir}/usb.ids
