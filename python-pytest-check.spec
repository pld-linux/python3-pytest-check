#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	pytest plugin that allows multiple failures per test
Summary(pl.UTF-8):	Wtyczka pytesta pozwalająca na wiele niepowodzeń z jednego testu
Name:		python-pytest-check
# keep 0.2.x for python2 support
Version:	0.2.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-check/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-check/pytest-check-%{version}.tar.gz
# Source0-md5:	21297eac5d350062aac1fc4eb1d081e5
URL:		https://pypi.org/project/pytest-check/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pytest plugin that allows multiple failures per test.

This plugin was a rewrite and a rename of pytest-expect.

%description -l pl.UTF-8
Wtyczka pytesta pozwalająca na wiele niepowodzeń z jednego testu.

Ta wtyczka była przepisaną wtyczką pytest-expect, z nową nazwą.

%package -n python3-pytest-check
Summary:	pytest plugin that allows multiple failures per test
Summary(pl.UTF-8):	Wtyczka pytesta pozwalająca na wiele niepowodzeń z jednego testu
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pytest-check
A pytest plugin that allows multiple failures per test.

This plugin was a rewrite and a rename of pytest-expect.

%description -n python3-pytest-check -l pl.UTF-8
Wtyczka pytesta pozwalająca na wiele niepowodzeń z jednego testu.

Ta wtyczka była przepisaną wtyczką pytest-expect, z nową nazwą.

%prep
%setup -q -n pytest-check-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/pytest_check
%{py_sitescriptdir}/pytest_check-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-check
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/pytest_check
%{py3_sitescriptdir}/pytest_check-%{version}-py*.egg-info
%endif
