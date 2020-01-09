Name: libcxgb4
Version: 1.3.5
Release: 1%{?dist}
Summary: Chelsio T4 iWARP HCA Userspace Driver
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/cxgb4/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libibverbs-devel >= 1.1.3, libtool
Requires: rdma
Obsoletes: %{name}-devel
ExcludeArch: s390 s390x
Provides: libibverbs-driver.%{_arch}
%description
Userspace hardware driver for use with the libibverbs InfiniBand/iWARP verbs
library.  This driver enables Chelsio T4 based iWARP capable Ethernet devices.

%package static
Summary: Static version of the libcxgb4 driver
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
%description static
Static version of libcxgb4 that may be linked directly to an application.

%prep
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_sysconfdir}/libibverbs.d/*.driver
%doc AUTHORS COPYING README

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%changelog
* Thu Mar 12 2015 Doug Ledford <dledford@redhat.com> - 1.3.5-1
- Update to latest upstream release
- Move modprobe setup to rdma package
- Resolves: bz1165842
- Related: bz1163527

* Wed Jun 18 2014 Doug Ledford <dledford@redhat.com> - 1.3.3-1
- Bump and rebuild against new libibverbs, update our sources while we
  are at it
- Related: bz854655

* Mon Jan 23 2012 Doug Ledford <dledford@redhat.com> - 1.2.0-1
- Update to latest upstream release while rebuilding against latest
  libibverbs
- Related: bz750609

* Mon Jul 25 2011 Doug Ledford <dledford@redhat.com> - 1.1.1-3
- Add missing arch macro to libibverbs-driver provide
- Related: bz725016

* Wed Apr 27 2011 Doug Ledford <dledford@redhat.com> - 1.1.1-2
- Fix package description to differentiate the fact that this is for the T4
  Chelsio based adapters instead of the previous T3 generation

* Fri Mar 25 2011 Doug Ledford <dledford@redhat.com> - 1.1.1-1
- Update to later upstream version
- Resolves: bz685058

* Thu Feb 03 2011 Doug Ledford <dledford@redhat.com> - 1.1.0-1
- Initial import of libcxgb4 driver
- Resolves: bz675024
