#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-tox
Version  : 4.0.11
Release  : 158
URL      : https://files.pythonhosted.org/packages/22/bc/48c9b2864d5229205312ea23f840a2098fb3b17a12c7e59e74d7ffc3f46a/tox-4.0.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/22/bc/48c9b2864d5229205312ea23f840a2098fb3b17a12c7e59e74d7ffc3f46a/tox-4.0.11.tar.gz
Summary  : tox is a generic virtualenv management and test command line tool
Group    : Development/Tools
License  : MIT
Requires: pypi-tox-bin = %{version}-%{release}
Requires: pypi-tox-license = %{version}-%{release}
Requires: pypi-tox-python = %{version}-%{release}
Requires: pypi-tox-python3 = %{version}-%{release}
Requires: pypi(importlib_metadata)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
BuildRequires : pypi-pytest

%description
# tox
[![PyPI](https://img.shields.io/pypi/v/tox)](https://pypi.org/project/tox/)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/tox.svg)](https://pypi.org/project/tox/)
[![Documentation
status](https://readthedocs.org/projects/tox/badge/?version=latest)](https://tox.readthedocs.io/en/latest/?badge=latest)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/tox/month)](https://pepy.tech/project/tox/month)
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
%setup -q -n tox-4.0.11
cd %{_builddir}/tox-4.0.11
pushd ..
cp -a tox-4.0.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671121067
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
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
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tox
cp %{_builddir}/tox-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tox/57b7b1ca99152770f11d8ffb65996badc6cd322f || :
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
