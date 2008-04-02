#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Carp
%define		pnam	Clan
Summary:	Carp::Clan - report errors from perspective of caller of a "clan" of modules
Summary(pl.UTF-8):	Carp::Clan - zgłaszanie błędów z perspektywy wywołującego "klan" modułów
Name:		perl-%{pdir}-%{pnam}
Version:	6.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3a1ea3da42ee62e4db20a8fbf80a74bf
URL:		http://search.cpan.org/dist/Carp-Clan/
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.40}
BuildRequires:	rpm-perlprov >= 4.1-13
Conflicts:	perl-Bit-Vector < 6.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module reports errors from the perspective of the caller of a
"clan" of modules, similar to "Carp.pm" itself.

%description -l pl.UTF-8
Moduł zgłasza błędy z perspektywy wykonywującego moduł, podobnie jak
Carp.pm.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Carp/*.pm
%{_mandir}/man3/*
