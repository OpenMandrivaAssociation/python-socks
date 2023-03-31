%global	module socks

Name:           python-%{module}
Version:        2.0.3
Release:        2
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python

License:        Apache 2
URL:            https://github.com/romis2012/python-socks
Source:         https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)

BuildArch:      noarch

%description
The python-socks package provides a core proxy client functionality for Python. 
Supports SOCKS4(a), SOCKS5, HTTP (tunneling) proxy and provides sync and async (asyncio, trio, curio) APIs. 
You probably don't need to use python-socks directly. It is used internally by aiohttp-socks and httpx-socks packages.

%files
%license LICENSE.txt
%doc README.md
%{python_sitelib}/python_socks/
%{python_sitelib}/python_socks-*.egg-info/

#----------------------------------------------------------------------------

%prep
%autosetup
rm -vrf *.egg-info
sed -i -e 's/\r//' README.md

%build
%py_build

%install
%py_install
