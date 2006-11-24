
%define	module	logilab-common
Summary:	Logilab common modules
Summary(pl):	Wspólne moduły Logilab
Name:		python-logilab-common
Version:	0.21.0
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.logilab.fr/pub/common/%{module}-%{version}.tar.gz
# Source0-md5:	623d0a4e78361a2ccd0b85e3eac53132
URL:		http://www.logilab.org/projects/common/view
BuildRequires:	python-devel
BuildRequires:	python-modules >= 2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package logilab.common contains several modules providing low
level functionalities shared among several Python projects developed
by Logilab.

%description -l pl
Pakiet logilab.common zawiera różne moduły dostarczające
niskopoziomową funkcjonalność wykorzystywaną przez różne pythonowe
projekty tworzone przez Logilab.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
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
%{py_sitescriptdir}/*
