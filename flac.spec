Summary:	Free Lossless Audio Codec
Name:		flac
Version:	1.2.1
Release:	13
License:	GPL/LGPL
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/flac/%{name}-%{version}.tar.gz
# Source0-md5:	153c8b15a54da428d1f0fadc756c22c7
URL:		http://flac.sourceforge.net/
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

%description devel
The package contains the development header files for FLAC libraries.

%package c++-devel
Summary:	FLAC++ - development files
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description c++-devel
The package contains the development header files for FLAC++ libraries.

%prep
%setup -q

sed -i -e 's|examples ||g' Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-static	\
	--disable-xmms-plugin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no makefiles in doc dirs
#rm -f doc/html/{Makefile*,images/Makefile*,ru/Makefile*}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%post   c++ -p /usr/sbin/ldconfig
%postun c++ -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/html/{*.html,images}
%lang(ru) %doc doc/html/ru
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
%{_libdir}/libFLAC.la
%{_includedir}/FLAC
%{_aclocaldir}/libFLAC.m4
%{_pkgconfigdir}/flac.pc

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libFLAC++.so
%{_libdir}/libFLAC++.la
%{_includedir}/FLAC++
%{_aclocaldir}/libFLAC++.m4
%{_pkgconfigdir}/flac++.pc

