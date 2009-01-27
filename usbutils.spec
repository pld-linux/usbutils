Summary:	Linux USB utilities
Summary(pl.UTF-8):	Linuksowe narzędzia do USB
Summary(pt_BR.UTF-8):	Utilitários Linux USB
Name:		usbutils
Version:	0.73
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/linux-usb/%{name}-%{version}.tar.gz
# Source0-md5:	88978b4ad891f610620b1b8e5e0f43eb
Source1:	http://www.linux-usb.org/usb.ids
# NoSource1-md5:	af2f7c85cdb2757b62bdcc21efe8c9d5
Patch0:		%{name}-ids.patch
URL:		http://www.linux-usb.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusb-devel >= 0.1.8
BuildRequires:	zlib-devel
Requires:	libusb >= 0.1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	/etc

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

# keep uncompressed database for compatibility with other tools
gzip -d $RPM_BUILD_ROOT%{_datadir}/usb.ids.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/lsusb
%{_mandir}/man8/lsusb.8*
%{_datadir}/usb.ids
