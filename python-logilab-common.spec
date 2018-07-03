#
# Conditional build:
%bcond_without  python2 # Python 2.x module
%bcond_without  python3 # Python 3.x module

%define	module	logilab-common
Summary:	Logilab common modules
Summary(pl.UTF-8):	Wspólne moduły Logilab
Name:		python-logilab-common
Version:	0.63.2
Release:	7
License:	LGPL v2.1+
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/pypi/logilab-common
Source0:	https://pypi.python.org/packages/source/l/logilab-common/%{module}-%{version}.tar.gz
# Source0-md5:	2bf4599ae1f2ccf4603ca02c5d7e798e
URL:		http://www.logilab.org/project/logilab-common
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools >= 7.0
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:  python3-modules >= 1:3.3
BuildRequires:	python3-setuptools >= 7.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
Requires:	python-six >= 1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package logilab.common contains several modules providing low
level functionalities shared among several Python projects developed
by Logilab.

%description -l pl.UTF-8
Pakiet logilab.common zawiera różne moduły dostarczające
niskopoziomową funkcjonalność wykorzystywaną przez różne pythonowe
projekty tworzone przez Logilab.

%package -n python3-%{module}
Summary:	Logilab common modules
Summary(pl.UTF-8):	Wspólne moduły Logilab
Group:		Development/Languages/Python
Requires:	python3-six >= 1.4.0

%description -n python3-%{module}
The package logilab.common contains several modules providing low
level functionalities shared among several Python projects developed
by Logilab.

%description -n python3-%{module} -l pl.UTF-8
Pakiet logilab.common zawiera różne moduły dostarczające
niskopoziomową funkcjonalność wykorzystywaną przez różne pythonowe
projekty tworzone przez Logilab.

%prep
%setup -q -n %{module}-%{version}

# drop python 2.5 egg deps
%{__rm} */*/*py2.5.egg

%build
%if %{with python2}
%py_build
%endif
%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install

touch $RPM_BUILD_ROOT%{py3_sitescriptdir}/logilab/__init__.py
%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}/logilab/
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}/logilab/

mv $RPM_BUILD_ROOT%{_bindir}/pytest{,3}
%endif

%if %{with python2}
%py_install

# because some logilab's software depend on this package
# and some not, so they all provide the __init__.py and we
# have to remove it in dependent software
touch $RPM_BUILD_ROOT%{py_sitescriptdir}/logilab/__init__.py
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/logilab/
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/logilab/

%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ChangeLog README
# isn't name too generic?
%attr(755,root,root) %{_bindir}/pytest
%dir %{py_sitescriptdir}/logilab
%{py_sitescriptdir}/logilab/__init__.py[co]
%{py_sitescriptdir}/logilab/common
%{py_sitescriptdir}/logilab_common-%{version}-py*-nspkg.pth
%{py_sitescriptdir}/logilab_common-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ChangeLog README
# isn't name too generic?
%attr(755,root,root) %{_bindir}/pytest3
%{py3_sitescriptdir}/logilab
%{py3_sitescriptdir}/logilab_common-%{version}-py*-nspkg.pth
%{py3_sitescriptdir}/logilab_common-%{version}-py*.egg-info
%endif
