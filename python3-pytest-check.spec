#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	pytest plugin that allows multiple failures per test
Summary(pl.UTF-8):	Wtyczka pytesta pozwalająca na wiele niepowodzeń z jednego testu
Name:		python3-pytest-check
Version:	2.1.4
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-check/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-check/pytest-check-%{version}.tar.gz
# Source0-md5:	bbc65a525885581375623fbf187700c6
URL:		https://pypi.org/project/pytest-check/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pytest plugin that allows multiple failures per test.

This plugin was a rewrite and a rename of pytest-expect.

%description -l pl.UTF-8
Wtyczka pytesta pozwalająca na wiele niepowodzeń z jednego testu.

Ta wtyczka była przepisaną wtyczką pytest-expect, z nową nazwą.

%prep
%setup -q -n pytest-check-%{version}

# stub to build with setuptools instead of flit
cat >setup.py <<EOF
from setuptools import setup
setup()
EOF

sed -ne 's/^Summary: //p' PKG-INFO > summary.txt

cat >>pyproject.toml <<EOF
[tool.setuptools.dynamic]
description = {file = ["summary.txt"]}
version = {attr = "pytest_check.__version__"}
EOF

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_check.plugin,pytester" \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md changelog.md
%{py3_sitescriptdir}/pytest_check
%{py3_sitescriptdir}/pytest_check-%{version}-py*.egg-info
