Summary:	Linux USB utilities
Summary(pl):	Linuksowe narzêdzia do USB
Name:		usbutils
Version:	0.8
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://usb.in.tum.de/download/usbutils/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_prefix}/share/misc

%description
usbutils contains a utility for inspecting devices connected to the
USB bus. It requires a Linux kernel version 2.3.15 or newer
(supporting the '/proc/bus/usb' interface) or patched PLD's
2.2 kernel.

%description -l pl
Pakiet usbutils zawiera narzêdzie do przegl±dania urz±dzeñ
pod³±czonych do szyny USB. Wymaga j±dra w werji 2.3.15 lub nowszej (z
obs³ug± interfejsu /proc/bus/usb) lub kernela 2.2 z PLD.

%prep
%setup -q

%build
%{__libtoolize}
rm -f missing
aclocal
automake -a -c
%{__autoconf}
cd libusb
rm -f missing
aclocal
automake -a -c
%{__autoconf}
cd ..
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
