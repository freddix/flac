# based on PLD Linux spec git://git.pld-linux.org/packages/.git
Summary:	Free Lossless Audio Codec
Name:		flac
Version:	1.3.0
Release:	1
License:	GPL/LGPL
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/flac/%{name}-%{version}.tar.xz
# Source0-md5:	13b5c214cee8373464d3d65dee362cdd
URL:		http://flac.sourceforge.net/
Patch0:		%{name}-divby0.patch
Patch1:		%{name}-realloc.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libogg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FLAC is an Open Source lossless audio codec developed by Josh Coalson.

%package c++
Summary:	FLAC++ - C++ API for FLAC codec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
FLAC++ - C++ API for FLAC codec.

%package devel
Summary:	FLAC - development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libogg-devel

%description devel
The package contains the development header files for FLAC libraries.

%package c++-devel
Summary:	FLAC++ - development files
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
The package contains the development header files for FLAC++
libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's|examples ||g' Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--disable-xmms-plugin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%check
%{__make} check

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%post   c++ -p /usr/sbin/ldconfig
%postun c++ -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/html/{*.html,images}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libFLAC.so.?
%attr(755,root,root) %{_libdir}/libFLAC.so.*.*.*
%{_mandir}/man1/*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libFLAC++.so.?
%attr(755,root,root) %{_libdir}/libFLAC++.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libFLAC.so
%{_includedir}/FLAC
%{_aclocaldir}/libFLAC.m4
%{_pkgconfigdir}/flac.pc

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libFLAC++.so
%{_includedir}/FLAC++
%{_aclocaldir}/libFLAC++.m4
%{_pkgconfigdir}/flac++.pc

