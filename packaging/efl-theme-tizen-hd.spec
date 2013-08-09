Name:          efl-theme-tizen-hd
Summary:       Tizen theme files
Version:       1.0.157r04
Release:       1
Group:         System/Libraries
License:       APLv2
Source0:       %{name}-%{version}.tar.gz
BuildRequires: efl


%description
Tizen HD theme for EFL


%package -n efl-theme-tizen-devel
Summary: Development package


%description -n efl-theme-tizen-devel
Development package


%prep
%setup -q 


%build
export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"

make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/LICENSE %{buildroot}/usr/share/license/%{name}


%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/tizen-hd.edj
%manifest %{name}.manifest
/usr/share/license/%{name}


%files -n efl-theme-tizen-devel
%defattr(-,root,root,-)
/opt/var/efl-theme-tizen-edc/*

