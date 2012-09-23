Summary:	Interface to Linux IEEE-1394 subsystem
Name:		libraw1394
Version:	2.1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.kernel.org/pub/linux/libs/ieee1394/%{name}-%{version}.tar.bz2
# Source0-md5:	2f8d06a826b658bd0f3f0697e930dd52
URL:		http://ieee1394.wiki.kernel.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libraw1394 is the only supported interface to the kernel side raw1394
of the Linux IEEE-1394 subsystem, which provides direct access to the
connected 1394 buses to user space. Through libraw1394/raw1394,
applications can directly send to and receive from other nodes without
requiring a kernel driver for the protocol in question.

%package devel
Summary:	libraw1394 header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libraw1394 devel package.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libraw1394.so.??
%attr(755,root,root) %{_libdir}/libraw1394.so.*.*.*
%{_mandir}/man1/*
%{_mandir}/man5/isodump.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libraw1394.so
%{_libdir}/libraw1394.la
%{_includedir}/libraw1394
%{_pkgconfigdir}/libraw1394.pc

