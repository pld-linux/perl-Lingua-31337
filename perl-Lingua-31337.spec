#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Lingua-31337
Summary:	P3RL M0DU1E 7O c0NVer7 7ext 7O C0o1 741k
Summary(pl):	M0DU� P3R14 d0 k0nw3r5j1 7ek57u n4 C0o1 m0w�
Name:		perl-Lingua-31337
Version:	0.02
Release:	0.1
License:	same as perl
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CW/CWEST/%{pnam}-%{version}.tar.gz
# Source0-md5:	ed62044e9fc6df817d52a3d838497819
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
P3RL M0DU1E 7O c0NVer7 7ext 7O C0o1 741k.

%description -l pl
M0DU� P3R14 d0 k0nw3r5j1 7ek57u n4 C0o1 m0w�.

%prep
%setup -q -n %{pnam}-%{version}

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
%doc Changes
%{perl_vendorlib}/Lingua/31337.pm
%{_mandir}/man3/*
