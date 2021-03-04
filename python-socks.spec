%global pypi_name socks

Name:           python-%{pypi_name}
Version:        1.2.2
Release:        1
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python

License:        Apache 2
URL:            https://pypi.org/project/python-socks/
Source:         https://files.pythonhosted.org/packages/7e/32/86c580f89a2702014460a008ccf1c819db44a388a4de4ef4155b6a9b4b7b/python-socks-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Provides:	python-%{pypi_name} = %{EVRD}

%description
The python-socks package provides a core proxy client functionality for Python. 
Supports SOCKS4(a), SOCKS5, HTTP (tunneling) proxy and provides sync and async (asyncio, trio, curio) APIs. 
You probably don't need to use python-socks directly. It is used internally by aiohttp-socks and httpx-socks packages.


%prep
%autosetup -n %{name}-%{version}
rm -vrf *.egg-info
sed -i -e 's/\r//' README.md

%build
%py_build

%install
%py_install

%files -n python-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-*.egg-info/
