Name: libcxgb4
Version: 1.2.0
Release: 3%{?dist}
Summary: Chelsio T4 iWARP HCA Userspace Driver
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/cxgb4/%{name}-%{version}.tar.gz
Source1: libcxgb4-modprobe.conf
Patch0:  libcxgb4-1.1.0-type.patch
Patch1:	 libcxgb4-1.2.0-alias.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libibverbs-devel >= 1.1.3, libtool
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
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -p -m 644 -D %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/modprobe.d/libcxgb4.conf
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_sysconfdir}/libibverbs.d/*.driver
%{_sysconfdir}/modprobe.d/libcxgb4.conf
%doc AUTHORS COPYING README

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%changelog
* Thu Feb 7 2013 Jay Fenlason <fenlason@redhat.com> - 1.2.0-3
- Include the -alias patch to fix
  Resolves: rhbz884075 - Package libcxgb4-1.2.0-1.el7 failed RHEL7 RPMdiff testing
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
