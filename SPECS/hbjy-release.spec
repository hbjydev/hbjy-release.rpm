Name:       hbjy-release
Version:    1
Release:    2%{?dist}
Summary:    Hayden Young's RPMs repository configuration.

License:    BSD

URL:        https://rpm.hbjy.io
Source0:    %{URL}/RPM-GPG-KEY-hbjy
Source1:    hbjy-rpm.repo

%description
This package contains the Hayden Young's RPMs repository configuration as well
as the paired GPG key.

%prep
%setup -q -c -T

%install
# gpg key
install -Dpm 644 %{SOURCE0} \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-hbjy

# repo
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/hbjy-rpm.repo
%{_sysconfdir}/pki/rpm-gpg/*

%changelog
* Sun Jun 20 2021 Hayden Young <hi@hbjy.dev>
- Create initial repo config package.

