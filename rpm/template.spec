%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-generate-parameter-library-py
Version:        0.3.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS generate_parameter_library_py package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-yaml
Requires:       python3-jinja2
Requires:       python3-typeguard
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-yaml
BuildRequires:  python3-jinja2
BuildRequires:  python3-typeguard
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-humble-ament-copyright
%endif

%description
Python to generate ROS parameter library.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Feb 21 2023 Paul Gesel <paul.gesel@picknik.ai> - 0.3.1-1
- Autogenerated by Bloom

* Tue Nov 15 2022 Paul Gesel <paul.gesel@picknik.ai> - 0.3.0-1
- Autogenerated by Bloom

* Thu Nov 03 2022 Paul Gesel <paul.gesel@picknik.ai> - 0.2.8-1
- Autogenerated by Bloom

* Fri Oct 28 2022 Paul Gesel <paul.gesel@picknik.ai> - 0.2.7-1
- Autogenerated by Bloom

* Wed Sep 28 2022 Paul Gesel <paul.gesel@picknik.ai> - 0.2.6-1
- Autogenerated by Bloom

* Tue Sep 27 2022 Paul Gesel <paul.gesel@picknik.ai> - 0.2.5-2
- Autogenerated by Bloom

* Tue Sep 20 2022 Paul Gesel <paul.gesel@picknik.ai> - 0.2.5-1
- Autogenerated by Bloom

