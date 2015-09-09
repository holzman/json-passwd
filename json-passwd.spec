Name:           json-passwd
Group:          System Environment/Libraries
Version:        1.0.0
Release:        0%{?dist}
Summary:        Manage passwd and group database files from json URLs

License:        BSD
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
URL:            http://github.com/tskirvin/json-passwd

BuildRequires:  rsync
Requires:       python

Source:         json-passwd-%{version}-%{release}.tar.gz

%description
Create and manage passwd.db and group.db entries (suitable for use with
nss_db) based on an externally-managed json data source.

%prep
%setup -q -c -n json-passwd

%build
# Empty build section added per rpmlint

%install
if [[ $RPM_BUILD_ROOT != "/" ]]; then
    rm -rf $RPM_BUILD_ROOT
fi

for i in etc usr; do
    rsync -Crlpt --delete ./${i} ${RPM_BUILD_ROOT}
done

for i in bin sbin; do
    if [ -d ${RPM_BUILD_ROOT}/$i ]; then
        chmod 0755 ${RPM_BUILD_ROOT}
    fi
done

mkdir -p ${RPM_BUILD_ROOT}/usr/share/man/man8
for i in `ls usr/sbin`; do
    pod2man --section 8 --center="System Commands" usr/sbin/${i} \
        > ${RPM_BUILD_ROOT}/usr/share/man/man8/${i}.8 ;
done

%clean
# Adding empty clean section per rpmlint.  In this particular case, there is 
# nothing to clean up as there is no build process

%post
mkdir -p /root/json-passwd

%files
%defattr(-,root,root)
%config(noreplace) /etc/json-passwd/config
/etc/json-passwd/Makefile
/usr/sbin/*
/usr/share/man/man8/*

%changelog
* Wed Sep  9 2015 Tim Skirvin <tskirvin@fnal.gov>       1.0.0-0.el6
- initial version
