Summary:	Linux USB utilities
Summary(pl):	Linuksowe narzêdzia do USB
Name:		usbutils
Version:	0.11
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://usb.in.tum.de/download/usbutils/%{name}-%{version}.tar.gz
Patch0:		%{name}-no_external_getopt.patch
Patch1:		%{name}-hwdata_in_misc.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch0 -p1
%patch1 -p1
ln -s ../ltmain.sh libusb/ltmain.sh

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
cd libusb
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%{__libtoolize}
cd ..
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%{_datadir}/misc/usb.ids
