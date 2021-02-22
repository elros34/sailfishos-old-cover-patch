Name:       sailfishos-old-cover-patch

BuildArch: noarch

Summary:    Old cover patch
Version:    0.1.1
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfish-version >= 4.0.1
Requires:   patchmanager
Requires:   sailfish-content-graphics-default-z2.0

%description
Patch returns gesture based covers from Sailfish 1.1 (inspired by Jolla's proprietary code) and adds 'hold and swipe' to close window. Also enables always swipeable notifications in events view.


%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}

