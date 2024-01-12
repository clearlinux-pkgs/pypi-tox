#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v3
# autospec commit: ab27b0e
#
Name     : pypi-tox
Version  : 4.12.0
Release  : 210
URL      : https://files.pythonhosted.org/packages/18/fc/01680767b408a51031fa9d9f19a87baefab172f60daf9597aea1d13d7fef/tox-4.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/18/fc/01680767b408a51031fa9d9f19a87baefab172f60daf9597aea1d13d7fef/tox-4.12.0.tar.gz
Summary  : tox is a generic virtualenv management and test command line tool
Group    : Development/Tools
License  : MIT
Requires: pypi-tox-bin = %{version}-%{release}
Requires: pypi-tox-license = %{version}-%{release}
Requires: pypi-tox-python = %{version}-%{release}
Requires: pypi-tox-python3 = %{version}-%{release}
Requires: pypi(importlib_metadata)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cachetools)
BuildRequires : pypi(chardet)
BuildRequires : pypi(colorama)
BuildRequires : pypi(devpi_process)
BuildRequires : pypi(distlib)
BuildRequires : pypi(filelock)
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
BuildRequires : pypi(pyproject_api)
BuildRequires : pypi(virtualenv)
BuildRequires : pypi-pytest
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# tox
[![PyPI](https://img.shields.io/pypi/v/tox)](https://pypi.org/project/tox/)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/tox.svg)](https://pypi.org/project/tox/)
[![Downloads](https://static.pepy.tech/badge/tox/month)](https://pepy.tech/project/tox)
[![Documentation
status](https://readthedocs.org/projects/tox/badge/?version=latest)](https://tox.readthedocs.io/en/latest/?badge=latest)
[![check](https://github.com/tox-dev/tox/actions/workflows/check.yml/badge.svg)](https://github.com/tox-dev/tox/actions/workflows/check.yml)

%package bin
Summary: bin components for the pypi-tox package.
Group: Binaries
Requires: pypi-tox-license = %{version}-%{release}

%description bin
bin components for the pypi-tox package.


%package license
Summary: license components for the pypi-tox package.
Group: Default

%description license
license components for the pypi-tox package.


%package python
Summary: python components for the pypi-tox package.
Group: Default
Requires: pypi-tox-python3 = %{version}-%{release}

%description python
python components for the pypi-tox package.


%package python3
Summary: python3 components for the pypi-tox package.
Group: Default
Requires: python3-core
Provides: pypi(tox)
Requires: pypi(cachetools)
Requires: pypi(chardet)
Requires: pypi(colorama)
Requires: pypi(filelock)
Requires: pypi(packaging)
Requires: pypi(platformdirs)
Requires: pypi(pluggy)
Requires: pypi(pyproject_api)
Requires: pypi(virtualenv)

%description python3
python3 components for the pypi-tox package.


%prep
%setup -q -n tox-4.12.0
cd %{_builddir}/tox-4.12.0
pushd ..
cp -a tox-4.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1705074358
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])")
pytest --verbose --no-network || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tox
cp %{_builddir}/tox-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tox/57b7b1ca99152770f11d8ffb65996badc6cd322f || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tox

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tox/57b7b1ca99152770f11d8ffb65996badc6cd322f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
