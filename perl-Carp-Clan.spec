#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Carp
%define	pnam	Clan
Summary:	Carp::Clan - report errors from perspective of caller of a "clan" of modules
Summary(pl):	Carp::Clan - zg³aszanie b³êdów z perspektywy wywo³uj±cego "klan" modu³ów
Name:		perl-%{pdir}-%{pnam}
Version:	5.3
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d0a0431921b2c786aac234dfb6fe02ca
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

%description -l pl
Modu³ zg³asza b³êdy z perspektywy wykonywuj±cego modu³, podobnie jak
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
%doc CHANGES.txt README.txt
%{perl_vendorlib}/Carp/*.pm
%{_mandir}/man3/*
