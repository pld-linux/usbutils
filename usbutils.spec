Summary:	Linux USB utilities
Summary(pl):	Linuksowe narzêdzia do USB
Summary(pt_BR):	Utilitários Linux USB
Name:		usbutils
Version:	0.11
Release:	4
License:	GPL
Group:		Applications/System
Source0:	http://usb.in.tum.de/download/usbutils/%{name}-%{version}.tar.gz
# Source0-md5:	05157bed61af65749f02713c10b8ef26
Source1:	http://www.linux-usb.org/usb.ids
# NoSource1-md5: a11983a44b69cd942978ec4fa073e2f0
Patch0:		%{name}-no_external_getopt.patch
Patch1:		%{name}-hwdata_in_misc.patch
Patch2:		%{name}-ignore-HCC.patch
Patch3:		%{name}-ids.patch
URL:		http://usb.in.tum.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch0 -p1
%patch1 -p1
%patch2 -p1

# paranoid check whether usb.ids in _sourcedir isn't too old
if [ "`wc -l < %{SOURCE1}`" -lt "`wc -l < usb.ids`" ] ; then
	echo "usb.ids needs to be updated"
	exit 1
fi
cp -f %{SOURCE1} .
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd libusb
%{__aclocal}
%{__autoconf}
# don't use --force here!
automake -a -c --foreign
cd ..
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
%{_datadir}/misc/usb.ids
