#
# Conditional build:
%bcond_with	hwdata_check	# check hwdata usb.ids freshness
#
Summary:	Linux USB utilities
Summary(pl.UTF-8):	Linuksowe narzędzia do USB
Summary(pt_BR.UTF-8):	Utilitários Linux USB
Name:		usbutils
Version:	007
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.xz
# Source0-md5:	c9df5107ae9d26b10a1736a261250139
Patch0:		hwdata.patch
URL:		http://www.linux-usb.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
%{?with_hwdata_check:BuildRequires:	hwdata >= 0.249}
BuildRequires:	libtool
BuildRequires:	libusb-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	hwdata >= 0.249
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		hwdatadir	/lib/hwdata
%define		_datadir	%{hwdatadir}

%description
usbutils contains a utility for inspecting devices connected to the
USB bus. It requires a Linux kernel version 2.3.15 or newer
(supporting the '/proc/bus/usb' interface) or patched PLD's 2.2
kernel.

%description -l pl.UTF-8
Pakiet usbutils zawiera narzędzie do przeglądania urządzeń
podłączonych do szyny USB. Wymaga jądra w werji 2.3.15 lub nowszej (z
obsługą interfejsu /proc/bus/usb) lub jądra 2.2 z PLD.

%description -l pt_BR.UTF-8
Este pacote contém utilitários para inspecionar dispositivos
conectados a um barramento USB.

%prep
%setup -q
%patch0 -p1

%if %{with hwdata_check}
# paranoid check whether usb.ids in system isn't too old
if [ usb.ids -nt %{hwdatadir}/usb.ids ]; then
	: usb.ids needs to be updated
	exit 1
fi
%endif
%{__rm} usb.ids

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-usbids \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	pkgconfigdir=%{_pkgconfigdir} \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/lsusb.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/lsusb
%attr(755,root,root) %{_bindir}/usb-devices
%attr(755,root,root) %{_bindir}/usbhid-dump
%{_mandir}/man1/usb-devices.1*
%{_mandir}/man8/lsusb.8*
%{_mandir}/man8/usbhid-dump.8*
# there is no devel package for now and the dir is part of filesystem
%{_pkgconfigdir}/usbutils.pc
