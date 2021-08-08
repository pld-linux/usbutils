# NOTE: usbutils>=008 requires udev; for udevless usage use usbutils-007
Summary:	Linux USB utilities
Summary(pl.UTF-8):	Linuksowe narzędzia do USB
Summary(pt_BR.UTF-8):	Utilitários Linux USB
Name:		usbutils
Version:	014
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.xz
# Source0-md5:	f21aa68ee7870b161921a590be7765e6
Patch0:		hwdata.patch
URL:		http://www.linux-usb.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.9
BuildRequires:	libtool
BuildRequires:	libusb-devel >= 1.0.14
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.507
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel >= 1:196
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	libusb >= 1.0.14
Requires:	udev-core >= 1:196
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
usbutils contains a utility for inspecting devices connected to the
USB bus.

%description -l pl.UTF-8
Pakiet usbutils zawiera narzędzie do przeglądania urządzeń
podłączonych do szyny USB.

%description -l pt_BR.UTF-8
Este pacote contém utilitários para inspecionar dispositivos
conectados a um barramento USB.

%package python
Summary:	Python based lsusb program
Summary(pl.UTF-8):	Program lsusb napisany w Pythonie
Group:		Applications/System
Requires:	hwdata >= 0.249

%description python
Python based lsusb program.

%description python -l pl.UTF-8
Program lsusb napisany w Pythonie.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' lsusb.py.in

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd usbhid-dump
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/lsusb
%attr(755,root,root) %{_bindir}/usb-devices
%attr(755,root,root) %{_bindir}/usbhid-dump
%{_mandir}/man1/usb-devices.1*
%{_mandir}/man8/lsusb.8*
%{_mandir}/man8/usbhid-dump.8*

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lsusb.py
