%define module socks
%define oname python_socks

Name:		python-socks
Version:	2.8.2
Release:	1
Summary:	Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python
License:	Apache-2.0
URL:		https://github.com/romis2012/python-socks
Source:		%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
The python-socks package provides a core proxy client functionality for Python. 
Supports SOCKS4(a), SOCKS5, HTTP (tunneling) proxy and provides sync and async (asyncio, trio, curio) APIs. 
You probably don't need to use python-socks directly. It is used internally by aiohttp-socks and httpx-socks packages.

%files
%license LICENSE.txt
%doc README.md
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%version.dist-info
