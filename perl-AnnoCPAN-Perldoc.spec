%define upstream_name    AnnoCPAN-Perldoc
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Integrate AnnoCPAN notes locally into perldoc
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
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
