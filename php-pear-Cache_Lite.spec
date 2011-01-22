%include	/usr/lib/rpm/macros.php
%define		_class		Cache
%define		_subclass	Lite
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Fast and Safe little cache system
Summary(pl.UTF-8):	%{_pearname} - Szybki i bezpieczny system buforujący
Name:		php-pear-%{_pearname}
Version:	1.7.8
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	75c142769a4ca68afc72dcf4f494bdd6
URL:		http://pear.php.net/package/Cache_Lite/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 4:1.0-21
Requires:	php-pear-PEAR-core
Obsoletes:	php-pear-Cache_Lite-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a little cache system optimized for file containers.
It is fast and safe (because it uses file locking and/or
anti-corruption tests).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet zawiera mały system buforujący zoptymalizowany dla
kontenerów plików. Jest szybki i bezpieczny (ponieważ używa blokowania
plików i/lub testów anti-corruption).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/{docs/*,TODO}
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
