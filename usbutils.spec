%define name usbutils
%define version 0.7
%define release 1mdk

Summary: Linux USB utilities
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://usb.in.tum.de/download/usbutils/usbutils-%{version}.tar.bz2
Copyright: GPL
Group: System/Kernel and hardware
Packager: Pixel <pixel@mandrakesoft.com>
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}

%description
usbutils contains a utility for inspecting devices connected to the USB bus. 
It requires a Linux kernel version 2.3.15 or newer (supporting the '/proc/bus/usb' interface).

%prep
%setup

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{_datadir}/usb.ids
%{_sbindir}/*


%changelog
* Sat Dec 16 2000 Pixel <pixel@mandrakesoft.com> 0.7-1mdk
- initial spec


# end of file
