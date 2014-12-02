Name:          efl-theme-tizen-hd
Summary:       Tizen theme files
Version:       1.0.204r07
Release:       1
Group:         System/Libraries
License:       Apache-2.0
Source0:       %{name}-%{version}.tar.gz
BuildRequires: perl, edje, edje-bin, embryo, embryo-bin
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
mkdir -p %{buildroot}%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/LICENSE %{buildroot}%{_datadir}/license/%{name}
cp %{buildroot}%{_datadir}/elementary/themes/tizen-HD-dark.edj %{buildroot}%{_datadir}/elementary/themes/tizen-hd.edj

%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/tizen-HD-dark.edj
%{_datadir}/elementary/themes/tizen-HD-light.edj
%{_datadir}/elementary/themes/tizen-hd.edj
%manifest %{name}.manifest
%{_datadir}/license/%{name}

%files -n efl-theme-tizen-devel
%defattr(-,root,root,-)
/opt/var/efl-theme-tizen-edc/*
