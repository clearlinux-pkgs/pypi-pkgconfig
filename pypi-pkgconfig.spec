#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pkgconfig
Version  : 1.5.5
Release  : 61
URL      : https://files.pythonhosted.org/packages/c4/e0/e05fee8b5425db6f83237128742e7e5ef26219b687ab8f0d41ed0422125e/pkgconfig-1.5.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/c4/e0/e05fee8b5425db6f83237128742e7e5ef26219b687ab8f0d41ed0422125e/pkgconfig-1.5.5.tar.gz
Summary  : Interface Python with pkg-config
Group    : Development/Tools
License  : MIT
Requires: pypi-pkgconfig-license = %{version}-%{release}
Requires: pypi-pkgconfig-python = %{version}-%{release}
Requires: pypi-pkgconfig-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
pkgconfig
=========
.. image:: https://travis-ci.org/matze/pkgconfig.png?branch=master
:target: https://travis-ci.org/matze/pkgconfig

%package license
Summary: license components for the pypi-pkgconfig package.
Group: Default

%description license
license components for the pypi-pkgconfig package.


%package python
Summary: python components for the pypi-pkgconfig package.
Group: Default
Requires: pypi-pkgconfig-python3 = %{version}-%{release}

%description python
python components for the pypi-pkgconfig package.


%package python3
Summary: python3 components for the pypi-pkgconfig package.
Group: Default
Requires: python3-core
Provides: pypi(pkgconfig)

%description python3
python3 components for the pypi-pkgconfig package.


%prep
%setup -q -n pkgconfig-1.5.5
cd %{_builddir}/pkgconfig-1.5.5
pushd ..
cp -a pkgconfig-1.5.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656394458
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pkgconfig
cp %{_builddir}/pkgconfig-1.5.5/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pkgconfig/6f33807d1075cf857dc91cf3cf8607894ebd11e0
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pkgconfig/6f33807d1075cf857dc91cf3cf8607894ebd11e0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
