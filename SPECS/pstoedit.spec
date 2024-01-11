%if 0%{?el7}
%global dts devtoolset-9-
%endif

Name:           pstoedit
Version:        3.75
Release:        5%{?dist}
Summary:        Translates PostScript and PDF graphics into other vector formats
License:        GPLv2+
URL:            http://www.pstoedit.net
Source0:        https://sourceforge.net/projects/pstoedit/files/pstoedit/%{version}/pstoedit-%{version}.tar.gz

# Fix cflags of the pkg-config file
Patch0:         pstoedit-pkglibdir.patch

BuildRequires: make
BuildRequires:  gd-devel
BuildRequires:  dos2unix
BuildRequires:  ghostscript
BuildRequires:  plotutils-devel
BuildRequires:  %{?dts}gcc-c++, %{?dts}gcc
BuildRequires:  libzip-devel
%if ! 0%{?rhel} >= 8
BuildRequires:  ImageMagick-c++-devel
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  libEMF-devel
%endif
%if 0%{?fedora}
BuildRequires:  ming-devel
%endif
Requires:       ghostscript%{?_isa}

%description
Pstoedit converts PostScript and PDF files to various vector graphic
formats. The resulting files can be edited or imported into various
drawing packages. Pstoedit comes with a large set of integrated format
drivers


%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files needed for developing %{name}
applications


%prep
%autosetup -p1

dos2unix doc/*.htm doc/readme.txt

%build
%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-9/enable}
%endif

%configure --disable-static --enable-docs=no --with-libzip-include=%{_includedir} \
%if 0%{?rhel} == 7
 --without-emf
%endif

%make_build

%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 doc/pstoedit.1 $RPM_BUILD_ROOT%{_mandir}/man1/
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%if 0%{?el7}
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/pstoedit
%endif


%files
%doc doc/readme.txt doc/pstoedit.htm doc/changelog.htm doc/pstoedit.pdf
%license copying
%{_datadir}/pstoedit/
%{_mandir}/man1/*
%{_bindir}/pstoedit
%{_libdir}/*.so.*
%{_libdir}/pstoedit/

%files devel
%doc doc/changelog.htm
%{_includedir}/pstoedit/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4


%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 3.75-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 3.75-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Tomas Popela <tpopela@redhat.com> - 3.75-2
- Disable ImageMagick support in ELN/RHEL 8+ as ImageMagick isn't part of it

* Mon Oct 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.75-1
- Rebase to 3.75

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.73-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.73-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Sebastian Kisela <skisela@redhat.com> - 3.73-3
- Add explicit gcc-c++ BuildRequires, as it has been removed from
the buildroot default packages set.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Sebastian Kisela <skisela@redhat.com> - 3.73-1
- Rebase to 3.73
- Add automake call to regenerate Makefile, as libpstoedit.so was not generated at the right time.

* Mon Apr 16 2018 Sebastian Kisela <skisela@redhat.com> - 3.70-11
- Revert back due to unnoticed ABI changes

* Fri Apr 13 2018 Sebastian Kisela <skisela@redhat.com> - 3.70-10
- Drop unused libpng dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Jiri Popelka <jpopelka@redhat.com> - 3.70-4
- correctly load plugins (#1247187)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.70-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 05 2015 Jiri Popelka <jpopelka@redhat.com> - 3.70-1
- 3.70

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.62-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 3.62-2
- rebuild for new GD 2.1.0

* Mon Apr 29 2013 Jiri Popelka <jpopelka@redhat.com> - 3.62-1
- 3.62
- remove autoreconf

* Mon Mar 25 2013 Jiri Popelka <jpopelka@redhat.com> - 3.61-3
- Run autoreconf prior to running configure (#926382)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 28 2012 Jiri Popelka <jpopelka@redhat.com> - 3.61-1
- 3.61

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.60-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Jiri Popelka <jpopelka@redhat.com> - 3.60-2
- Correct source url.

* Mon Aug 29 2011 Jiri Popelka <jpopelka@redhat.com> - 3.60-1
- Update to new upstream 3.60, bugfix release
- Remove Rpath

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.45-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.45-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul  9 2009 Denis Leroy <denis@poolshark.org> - 3.45-8
- Fix parallel build (#510281)
- Remove ImageMagick support, to work around bug 507035

* Tue Mar 10 2009 Denis Leroy <denis@poolshark.org> - 3.45-7
- Removed EMF BR for ia64 arch (#489412)
- Rebuild for ImageMagick

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  7 2009 Denis Leroy <denis@poolshark.org> - 3.45-5
- Added patch for improved asymptote support (#483503)
- Added patch to fix incorrect cpp directive

* Wed Sep 24 2008 Denis Leroy <denis@poolshark.org> - 3.45-4
- Fixed cxxflags patch fuziness issue

* Wed May 14 2008 Denis Leroy <denis@poolshark.org> - 3.45-3
- Rebuild for new ImageMagick

* Sun Feb 17 2008 Denis Leroy <denis@poolshark.org> - 3.45-2
- Added patch for gcc 4.3 rebuild

* Thu Sep 20 2007 Denis Leroy <denis@poolshark.org> - 3.45-1
- Update to new upstream 3.45, bugfix release
- Updated quiet patch for 3.45

* Mon Aug 20 2007 Denis Leroy <denis@poolshark.org> - 3.44-7
- License tag update

* Sun Mar 25 2007 Denis Leroy <denis@poolshark.org> - 3.44-6
- Added patch to add -quiet option

* Wed Nov 22 2006 Denis Leroy <denis@poolshark.org> - 3.44-5
- Added libEMF support

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 3.44-4
- FE6 Rebuild

* Fri Aug 18 2006 Denis Leroy <denis@poolshark.org> - 3.44-3
- Added svg/libplot support

* Thu Jun 15 2006 Denis Leroy <denis@poolshark.org> - 3.44-2
- Added missing Requires and BuildRequires
- Patched configure to prevent CXXFLAGS overwrite

* Thu Jun  8 2006 Denis Leroy <denis@poolshark.org> - 3.44-1
- First version
