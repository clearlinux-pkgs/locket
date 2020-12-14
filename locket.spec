#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : locket
Version  : 0.2.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/d0/22/3c0f97614e0be8386542facb3a7dcfc2584f7b83608c02333bced641281c/locket-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d0/22/3c0f97614e0be8386542facb3a7dcfc2584f7b83608c02333bced641281c/locket-0.2.0.tar.gz
Summary  : File-based locks for Python for Linux and Windows
Group    : Development/Tools
License  : BSD-2-Clause
Requires: locket-license = %{version}-%{release}
Requires: locket-python = %{version}-%{release}
Requires: locket-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=========
        
        Locket implements a lock that can be used by multiple processes provided they use the same path.

%package license
Summary: license components for the locket package.
Group: Default

%description license
license components for the locket package.


%package python
Summary: python components for the locket package.
Group: Default
Requires: locket-python3 = %{version}-%{release}

%description python
python components for the locket package.


%package python3
Summary: python3 components for the locket package.
Group: Default
Requires: python3-core
Provides: pypi(locket)

%description python3
python3 components for the locket package.


%prep
%setup -q -n locket-0.2.0
cd %{_builddir}/locket-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602133584
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/locket
cp %{_builddir}/locket-0.2.0/LICENSE %{buildroot}/usr/share/package-licenses/locket/0807415dbe135f77472bb52ce30089e124de4a60
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/locket/0807415dbe135f77472bb52ce30089e124de4a60

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
