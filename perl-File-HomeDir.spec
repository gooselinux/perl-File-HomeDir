Name:           perl-File-HomeDir
Version:        0.86
Release:        3%{?dist}
Summary:        Get the home directory for yourself or other users

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/File-HomeDir/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/File-HomeDir-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Test::Pod), perl(Test::More), perl(Test::MinimumVersion)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
File::HomeDir is a module for dealing with issues relating to the
location of directories for various purposes that are "owned" by a
user, and to solve these problems consistently across a wide variety
of platforms.


%prep
%setup -q -n File-HomeDir-%{version}
chmod -c a-x Changes lib/File/{*.pm,HomeDir/*.pm}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
# These tests don't do anything really useful. Also, they are broken.
# AUTOMATED_TESTING=1 make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/File/
%{_mandir}/man3/*.3pm*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.86-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun  1 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.86-1
- update for Padre

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.84-1
- update to 0.84

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Marcela Mašláňová <mmaslano@redhat.com> - 0.82-1
- update to the latest version for Padre editor

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.67-3
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.67-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.67-1
- 0.67

* Fri Nov 30 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.66-1
- 0.66

* Wed May 30 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.65-1
- Update to 0.65.

* Sat Feb 10 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.64-1
- Update to 0.64.

* Thu Jan 11 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.63-1
- Update to 0.63.

* Thu Jan  4 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.62-1
- Update to 0.62.

* Thu Aug 03 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.58-1
- First build.
