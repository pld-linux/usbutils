Summary:	Linux USB utilities
Summary(pl):	Linuksowe narzêdzia do USB
Summary(pt_BR):	Utilitários Linux USB
Name:		usbutils
Version:	0.70
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/linux-usb/%{name}-%{version}.tar.gz
# Source0-md5:	05276dc307a0297904bc892e9998bf59
Source1:	http://www.linux-usb.org/usb.ids
# NoSource1-md5: d811f8a376c84a3a377dd8b71fbea41d
Patch0:		%{name}-ids.patch
URL:		http://www.linux-usb.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusb-devel >= 0.1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	/usr/share/misc

%description
usbutils contains a utility for inspecting devices connected to the
USB bus. It requires a Linux kernel version 2.3.15 or newer
(supporting the '/proc/bus/usb' interface) or patched PLD's 2.2
kernel.

%description -l pl
Pakiet usbutils zawiera narzêdzie do przegl±dania urz±dzeñ
pod³±czonych do szyny USB. Wymaga j±dra w werji 2.3.15 lub nowszej (z
obs³ug± interfejsu /proc/bus/usb) lub j±dra 2.2 z PLD.

%description -l pt_BR
Este pacote contém utilitários para inspecionar dispositivos
conectados a um barramento USB.

%prep
%setup -q

# paranoid check whether usb.ids in _sourcedir isn't too old
if [ "`wc -l < %{SOURCE1}`" -lt "`wc -l < usb.ids`" ] ; then
	echo "usb.ids needs to be updated"
	exit 1
fi
cp -f %{SOURCE1} .
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%{_datadir}/usb.ids
