Summary:	dqlite library - distributed SQLite engine
Summary(pl.UTF-8):	Biblioteka dqlite - rozproszony silnik SQLite
Name:		dqlite
Version:	1.6.0
Release:	3
License:	LGPL v3 with exception
Group:		Libraries
#Source0Download: https://github.com/canonical/dqlite/releases
Source0:	https://github.com/canonical/dqlite/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f5735eabb1f7176351d8bafd3bb9a055
URL:		https://github.com/canonical/dqlite
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.11
BuildRequires:	libtool >= 2:2
BuildRequires:	libuv-devel >= 1.8.0
BuildRequires:	pkgconfig
BuildRequires:	raft-devel >= 0.9.25
BuildRequires:	sqlite3-devel >= 3.22.0
Requires:	libuv >= 1.8.0
Requires:	raft >= 0.9.25
Requires:	sqlite3 >= 3.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides the dqlite C library (libdqlite), which can be
used to expose a dqlite database over the network and replicate it
across a cluster of peers, using the Raft algorithm.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę C dqlite (libdqlite), którą można
wykorzystywać do udostępnienia bazy danych dqlite przez sieć i
replikować ją na klaster partnerów przy użyciu algorytmu Raft.

%package devel
Summary:	Header files for dqlite development
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dqlite
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libuv-devel >= 1.8.0
Requires:	raft-devel >= 0.9.25
Requires:	sqlite3-devel >= 3.22.0

%description devel
This package contains development files for the dqlite library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki dqlite.

%package static
Summary:	Static dqlite library
Summary(pl.UTF-8):	Statyczna biblioteka dqlite
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static dqlite library.

%description static -l pl.UTF-8
Ten pakiet zawiera bibliotekę statyczną dqlite.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libdqlite.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%attr(755,root,root) %{_libdir}/libdqlite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdqlite.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdqlite.so
%{_includedir}/dqlite.h
%{_pkgconfigdir}/dqlite.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdqlite.a
