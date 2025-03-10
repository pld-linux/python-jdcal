# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		jdcal
Summary:	Julian dates from proleptic Gregorian and Julian calendars
Name:		python-%{module}
Version:	1.4.1
Release:	6
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jdcal/
Source0:	https://files.pythonhosted.org/packages/source/j/jdcal/%{module}-%{version}.tar.gz
# Source0-md5:	e05bdb60fa80f25bc60e73e0c6b7c5dc
URL:		https://github.com/phn/jdcal
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
This module contains functions for converting between Julian dates and
calendar dates.

%package -n python3-%{module}
Summary:	Julian dates from proleptic Gregorian and Julian calendars
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
This module contains functions for converting between Julian dates and
calendar dates.

%prep
%setup -q -n %{module}-%{version}

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
%{py_sitescriptdir}/%{module}.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
