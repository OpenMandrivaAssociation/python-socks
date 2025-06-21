%global	module socks

Name:           python-%{module}
Version:        2.7.1
Release:        1
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python

License:        Apache 2
URL:            https://github.com/romis2012/python-socks
Source:         %url/archive/refs/tags/v%version.tar.gz#/%{name}/%{name}-%{version}.tar.gz

BuildSystem:    python

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
%{python_sitelib}/python_socks-%version.dist-info/

#----------------------------------------------------------------------------
