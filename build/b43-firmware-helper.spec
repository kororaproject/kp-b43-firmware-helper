Name:     b43-firmware-helper
Version:  5.100.138
Release:  1%{?dist}
Summary:  Broadcom Firmware installer
License:  Proprietary
Requires: b43-fwcutter wget
Source0:  %{name}-%{version}.tar.gz

%description
This is a helper package to download, extract and install the
firmware for Broadcom 802.11 B/G/N family of wireless chips.

Requires direct access to the Internet to work. If it fails due
to lack of Internet access, you can yum reinstall this package
once Internet access is available.

%prep
%setup -q

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%post
# Run the script automatically on first install, but not upgrades
if [ "$1" == "1" ]
then
  %{_bindir}/%{name} 2>/dev/null
fi

%files
%{_bindir}/%{name}

%changelog
* Fri Aug 23 2013 Chris Smart <csmart@kororaproject.org> 5.100.138-1
- Initial spec.

