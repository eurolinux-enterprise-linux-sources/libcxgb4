%define ver 1.3.5

Name: libcxgb4
Version: 1.3.5
Release: 1%{?dist}
Summary: Chelsio T4/T5 RNIC Open Fabrics Userspace Library

Group: System Environment/Libraries
License: GPL/BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/cxgb4/%{name}-%{ver}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libibverbs-devel

%description
libcxgb4 provides a device-specific userspace driver for Chelsio T4
RNICs for use with the libibverbs library.

%package devel
Summary: Development files for the libcxgb4 driver
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Static version of libcxgb4 that may be linked directly to an
application, which may be useful for debugging.

%prep
%setup -q -n %{name}-%{ver}

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libcxgb4*.so
%doc AUTHORS COPYING ChangeLog README
%config %{_sysconfdir}/libibverbs.d/cxgb4.driver

%files devel
%defattr(-,root,root,-)
%{_libdir}/libcxgb4*.a

%changelog
