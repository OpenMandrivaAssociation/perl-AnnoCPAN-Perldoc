%define upstream_name    AnnoCPAN-Perldoc
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    Integrate AnnoCPAN notes locally into perldoc
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/AnnoCPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBI)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(IO::String)
BuildRequires: perl(Pod::Perldoc)
BuildRequires: perl(Test::Pod)
BuildRequires: perl-devel

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
AnnoCPAN is a web interface for the documentation of all the modules on
CPAN, where users can add annotations on the margin of specific paragraphs
throughout the POD. The master AnnoCPAN site is located at
http://annocpan.org/.

AnnoCPAN-Perldoc provides a substitute for the 'perldoc' command that
displays the annotations locally and without requiring a connection to the
Internet. It works by using a local note database that can be downloaded
from

    http://annocpan.org/annopod.db

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/annopod


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 654862
- rebuild for updated spec-helper

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 503915
- rebuild using %%perl_convert_version

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10-2mdv2010.0
+ Revision: 376126
- fixing man1 %%files
- rebuild

* Tue Mar 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10-1mdv2009.1
+ Revision: 362925
- adding missing prereq
- import perl-AnnoCPAN-Perldoc


* Tue Mar 31 2009 cpan2dist 0.10-1mdv
- initial mdv release, generated with cpan2dist

