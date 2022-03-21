Name:       sailfishos-old-cover-patch

BuildArch: noarch

Summary:    Old cover patch
Version:    0.1.3
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfish-version >= 4.0.1
Requires:   patchmanager
Requires:   sailfish-content-graphics-closed-z2.0
Requires:   sailfish-content-graphics-default-z2.0-base


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

# Precaution if patch is added to image, theme_pixel_ratio is different than z2.0 and it is installed before theme_pixel_ratio
%transfiletriggerin -- /usr/share/sailfish-minui/images
if grep -q "/usr/share/sailfish-minui/images/z2.0"; then
    theme_pixel_ratio=$(dconf read /desktop/sailfish/silica/theme_pixel_ratio)
    if [ $(readlink -f /usr/share/sailfish-minui/images/default | cut -d/ -f6) != z$theme_pixel_ratio ]; then
        echo "Changing /usr/share/sailfish-minui/images/default to z$theme_pixel_ratio"
        ln -sfn /usr/share/sailfish-minui/images/z$theme_pixel_ratio /usr/share/sailfish-minui/images/default
    fi
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}

