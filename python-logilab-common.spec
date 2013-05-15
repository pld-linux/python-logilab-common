
%define	module	logilab-common
Summary:	Logilab common modules
Summary(pl.UTF-8):	Wspólne moduły Logilab
Name:		python-logilab-common
Version:	0.59.1
Release:	2
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://download.logilab.org/pub/common/%{module}-%{version}.tar.gz
# Source0-md5:	614f0a5cd78242dad3317fd83d54ccc4
URL:		http://www.logilab.org/project/logilab-common
BuildRequires:	python-devel
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
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

%prep
%setup -q -n %{module}-%{version}
# drop python 2.5 egg deps
rm */*/*py2.5.egg

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# because some logilab's software depend on this package
# and some not, so they all provide the __init__.py and we
# have to remove it in dependent software
touch $RPM_BUILD_ROOT%{py_sitescriptdir}/logilab/__init__.py
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/logilab/
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/logilab/

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

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
