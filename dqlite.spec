Summary:	%{name} library
Summary(pl.UTF-8):	Biblioteka %{name}
Name:		dqlite
Version:	1.4.0
Release:	1
License:	LGPLv3
Group:		Libraries
Source0:	https://github.com/canonical/dqlite/archive/v%{version}.tar.gz
# Source0-md5:	43b7d1b8ccda54a379a6bfb92a98ae6f
URL:		https://github.com/canonical/dqlite
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libco-devel
BuildRequires:	libtool
BuildRequires:	raft-devel
BuildRequires:	sqlite3-devel(wal_replication)
Requires:	sqlite3(wal_replication)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This repository provides the dqlite C library (libdqlite), which can
be used to expose a %{name} database over the network and replicate it
across a cluster of peers, using the Raft algorithm.

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	sqlite3-devel(wal_replication)

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
