Summary:	%{name} library
Summary(pl.UTF-8):	Biblioteka %{name}
Name:		dqlite
Version:	0.2.4
Release:	0.1
License:	Public Domain
Group:		Libraries
Source0:	https://github.com/CanonicalLtd/dqlite/archive/v%{version}.tar.gz
# Source0-md5:	35a3001090b7df1a679bfc4ac996b8b6
URL:		https://github.com/CanonicalLtd/dqlite
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	sqlite3-devel >= PATCHED_VERSION_see_README
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This repository provides the dqlite C library (libdqlite), which can
be used to expose a %{name} database over the network and replicate it
across a cluster of peers, using the Raft algorithm.

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe %{name}
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains development files for the %{name} library.

%package static
Summary:	Static libraries for %{name} development
Summary(pl.UTF-8):	Statyczne biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static %{name} library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libdqlite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdqlite.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdqlite.so
%{_libdir}/libdqlite.la
%{_includedir}/dqlite.h
%{_pkgconfigdir}/dqlite.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdqlite.a
