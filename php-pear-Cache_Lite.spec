%include	/usr/lib/rpm/macros.php
%define		_class		Cache
%define		_subclass	Lite
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Fast and Safe little cache system
Summary(pl):	%{_pearname} - Szybki i bezpieczny system buforuj±cy
Name:		php-pear-%{_pearname}
Version:	1.3.1
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	678b9ac6267fb6b18b1b1c7a53316fbd
URL:		http://pear.php.net/package/Cache_Lite/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a little cache system optimized for file containers.
It is fast and safe (because it uses file locking and/or
anti-corruption tests).

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet zawiera ma³y system buforuj±cy zoptymalizowany dla
kontenerów plików. Jest szybki i bezpieczny (poniewa¿ u¿ywa blokowania
plików i/lub testów anti-corruption).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{tests,docs/*,TODO}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
