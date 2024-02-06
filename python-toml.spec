# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-toml
Epoch: 100
Version: 0.10.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Python Library for Tom's Obvious, Minimal Language
License: MIT
URL: https://github.com/uiri/toml/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Python toml allows to parse and create toml configuration files. See
below the toml specification link.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-toml
Summary: Python Library for Tom's Obvious, Minimal Language
Requires: python3
Provides: python3-toml = %{epoch}:%{version}-%{release}
Provides: python3dist(toml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-toml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(toml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-toml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(toml) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-toml
Python toml allows to parse and create toml configuration files. See
below the toml specification link.

%files -n python%{python3_version_nodots}-toml
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-toml
Summary: Python Library for Tom's Obvious, Minimal Language
Requires: python3
Provides: python3-toml = %{epoch}:%{version}-%{release}
Provides: python3dist(toml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-toml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(toml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-toml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(toml) = %{epoch}:%{version}-%{release}

%description -n python3-toml
Python toml allows to parse and create toml configuration files. See
below the toml specification link.

%files -n python3-toml
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
