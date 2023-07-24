%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-parameter-traits
Version:        0.3.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS parameter_traits package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       fmt-devel
Requires:       ros-humble-rclcpp
Requires:       ros-humble-rsl
Requires:       ros-humble-tcb-span
Requires:       ros-humble-tl-expected
Requires:       ros-humble-ros-workspace
BuildRequires:  fmt-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rsl
BuildRequires:  ros-humble-tcb-span
BuildRequires:  ros-humble-tl-expected
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
%endif

%description
Functions and types for rclcpp::Parameter

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Mon Jul 24 2023 Tyler Weaver <maybe@tylerjw.dev> - 0.3.4-1
- Autogenerated by Bloom

* Thu Apr 13 2023 Tyler Weaver <maybe@tylerjw.dev> - 0.3.3-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Tyler Weaver <maybe@tylerjw.dev> - 0.3.2-1
- Autogenerated by Bloom

* Tue Feb 21 2023 Tyler Weaver <maybe@tylerjw.dev> - 0.3.1-1
- Autogenerated by Bloom

* Tue Nov 15 2022 Tyler Weaver <maybe@tylerjw.dev> - 0.3.0-1
- Autogenerated by Bloom

* Thu Nov 03 2022 Tyler Weaver <maybe@tylerjw.dev> - 0.2.8-1
- Autogenerated by Bloom

* Fri Oct 28 2022 Tyler Weaver <maybe@tylerjw.dev> - 0.2.7-1
- Autogenerated by Bloom

* Wed Sep 28 2022 Tyler Weaver <maybe@tylerjw.dev> - 0.2.6-1
- Autogenerated by Bloom

* Tue Sep 27 2022 Tyler Weaver <maybe@tylerjw.dev> - 0.2.5-2
- Autogenerated by Bloom

* Tue Sep 20 2022 Tyler Weaver <maybe@tylerjw.dev> - 0.2.5-1
- Autogenerated by Bloom

