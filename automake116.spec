# automake116 SCL metapackage

%global scl_name_prefix ribose-
%global scl_name_base automake
%global scl_name_version 116
%global scl %{scl_name_prefix}%{scl_name_base}%{scl_name_version}

%global nfsmountable 1

%global _scl_prefix /opt/ribose
%scl_package %scl

# do not produce empty debuginfo package
%global debug_package %{nil}

Summary: Package that installs %scl
Name: %scl_name
Version: 1
Release: 1%{?dist}
License: GPLv2+ and GFDL and Public Domain and MIT
BuildRequires: scl-utils-build
Requires: %{scl_prefix}automake

%description
This is the main package for %scl Software Collection.

%package runtime
Summary: Package that handles %scl Software Collection.
Requires: scl-utils

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

%package build
Summary: Package shipping basic build configuration
Requires: scl-utils-build

%description build
Package shipping essential configuration macros to build %scl Software Collection.

%prep
%setup -T -c

%install
%scl_install

cat >> %{buildroot}%{_scl_scripts}/enable <<'EOF'
export PATH=%{_bindir}${PATH:+:${PATH}}
export LD_LIBRARY_PATH=%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export MANPATH=%{_mandir}:$MANPATH
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig${PKG_CONFIG_PATH:+:${PKG_CONFIG_PATH}}
export XDG_DATA_DIRS="%{_datadir}:${XDG_DATA_DIRS:-/usr/local/share:/usr/share}"
EOF

%files

%files runtime -f filelist
%scl_files

%files build
%defattr(-,root,root)
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%changelog
* Tue Oct 30 2018 Daniel Wyatt <daniel.wyatt@ribose.com> - 1.0-1
- Create automake116 metapackage.

