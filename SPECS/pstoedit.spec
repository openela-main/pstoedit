Name:           pstoedit
Version:        3.70
Release:        9%{?dist}
Summary:        Translates PostScript and PDF graphics into other vector formats

Group:          Applications/Productivity
License:        GPLv2+
URL:            http://www.pstoedit.net/
Source0:        http://downloads.sourceforge.net/pstoedit/pstoedit-%{version}.tar.gz

Patch0:         pstoedit-pkglibdir.patch

Requires:       ghostscript
BuildRequires:  gd-devel
BuildRequires:  libpng-devel
BuildRequires:  dos2unix
BuildRequires:  ghostscript
BuildRequires:  plotutils-devel
%ifnarch ia64
BuildRequires:  libEMF-devel
%endif

%description
Pstoedit converts PostScript and PDF files to various vector graphic
formats. The resulting files can be edited or imported into various
drawing packages. Pstoedit comes with a large set of integrated format
drivers


%package devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       libpng-devel

%description devel
This package contains the header files needed for developing %{name}
applications


%prep
%setup -q

# correctly load plugins (#1247187)
%patch0 -p1 -b .pkglibdir

dos2unix doc/*.htm doc/readme.txt


%build
# Buildling without ImageMagick support, to work around bug 507035
%configure --disable-static --with-emf --without-swf --without-magick

# http://fedoraproject.org/wiki/Packaging/Guidelines#Removing_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/pstoedit.1 $RPM_BUILD_ROOT%{_mandir}/man1/
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc copying doc/readme.txt doc/pstoedit.htm
%{_datadir}/pstoedit
%{_mandir}/man1/*
%{_bindir}/pstoedit
%{_libdir}/*.so.*
%{_libdir}/pstoedit


%files devel
%doc doc/changelog.htm
%{_includedir}/pstoedit
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4


%changelog
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

