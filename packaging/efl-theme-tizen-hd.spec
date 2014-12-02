Name:          efl-theme-tizen-hd
Summary:       Tizen theme files
Version:       1.0.204r07
Release:       0
Group:         Graphics & UI Framework/Configuration
License:       Apache-2.0
Source0:       %{name}-%{version}.tar.gz
BuildRequires: perl, edje, edje-bin, embryo, embryo-bin
BuildRequires: pkgconfig(elementary)
%define _unpackaged_files_terminate_build 0

%description
Tizen HD theme for EFL


%package -n efl-theme-tizen-devel
Summary: Development package


%description -n efl-theme-tizen-devel
Development package


%prep
%setup -q


%build
export CFLAGS="${CFLAGS} --fPIC"
export LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=%{_prefix}/lib"

%__make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
cp %{buildroot}%{_datadir}/elementary/themes/tizen-HD-dark.edj %{buildroot}%{_datadir}/elementary/themes/tizen-hd.edj

%files
%defattr(-,root,root,-)
%license LICENSE
%{_datadir}/elementary/themes/tizen-HD-dark.edj
%{_datadir}/elementary/themes/tizen-HD-light.edj
%{_datadir}/elementary/themes/tizen-hd.edj
%manifest %{name}.manifest


%files -n efl-theme-tizen-devel
%defattr(-,root,root,-)
%license LICENSE
/opt/var/efl-theme-tizen-edc/*
