%include	/usr/lib/rpm/macros.php
%define		_class		Cache
%define		_subclass	Lite
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Fast and Safe little cache system
Summary(pl):	%{_pearname} - Szybki i bezpieczny system buforuj±cy
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a little cache system optimized for file containers.
It is fast and safe (because it uses file locking and/or
anti-corruption tests).

%description -l pl
Ten pakiet zawiera ma³y system buforuj±cy zoptymalizowany dla
kontenerów plików. Jest szybki i bezpieczny (poniewa¿ u¿ywa blokowania
plików i/lub testów anti-corruption).

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}

install %{_pearname}-%{version}/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{tests,docs/*}
%dir %{php_pear_dir}/%{_pearname}
%{php_pear_dir}/%{_pearname}/*.php
