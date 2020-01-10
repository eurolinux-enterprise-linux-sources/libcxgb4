Name: libcxgb4
Version: 1.3.5
Release: 2%{?dist}
Summary: Chelsio T4 iWARP HCA Userspace Driver
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/cxgb4/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libibverbs-devel >= 1.1.3, libtool
Obsoletes: %{name}-devel
Requires: rdma
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
%{__make} %{?_smp_mflags} CFLAGS="$CFLAGS -fno-strict-aliasing"

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
* Tue Dec 23 2014 Doug Ledford <dledford@redhat.com> - 1.3.5-2
- Rebuild without modprobe file
- Add requires on rdma package that now contains modprobe file
- Related: bz1164618

* Fri Oct 17 2014 Doug Ledford <dledford@redhat.com> - 1.3.5-1
- Update to latest upstream release and rebuild against latest libibverbs
- Related: bz1137044

* Mon Mar 03 2014 Doug Ledford <dledford@redhat.com> - 1.2.0-6
- Our -fno-strict-alias option patch was lost, and we discovered it
  was lost when I rebuilt the package.  Put it back and rebuild
  again.
- Related: bz1062281

* Mon Mar 03 2014 Doug Ledford <dledford@redhat.com> - 1.2.0-5
- Bump and rebuild against latest libibverbs
- Related: bz1062281

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.0-4
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 03 2012 Doug Ledford <dledford@redhat.com> - 1.2.0-1
- Update to latest upstream release
- Initial submission to Fedora

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
