Summary:	LibMMS - mms:// and mmsh:// parsing library
Summary(pl):	LibMMS - biblioteka przetwarzaj�ca mms:// i mmsh://
Name:		libmms
Version:	0.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libmms/%{name}-%{version}.tar.gz
# Source0-md5:	ebd88537af9875265e41ee65603ecd1a
URL:		http://sourceforge.net/projects/libmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibMMS is mms:// and mmsh:// (Microsoft streaming protocols) parsing
library.

%description -l pl
LibMMS to biblioteka przetwarzaj�ca mms:// i mmsh:// (protoko�y
strumieni Microsoftu).

%package devel
Summary:	Header files for libmms library
Summary(pl):	Pliki nag��wkowe biblioteki libmms
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmms library.

%description devel -l pl
Pliki nag��wkowe biblioteki libmms.

%package static
Summary:	Static libmms library
Summary(pl):	Statyczna biblioteka libmms
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmms library.

%description static -l pl
Statyczna biblioteka libmms.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libmms
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
