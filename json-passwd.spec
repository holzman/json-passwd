Name:           json-passwd
Group:          System Environment/Libraries
Version:        1.0.0
Release:        0%{?dist}
Summary:        Manage passwd and group database files from json URLs

License:        Perl Artistic 2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       python

Provides:       json-passwd = %{version}-%{release}

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

rsync -Crlpt --delete ./etc ${RPM_BUILD_ROOT}
rsync -Crlpt --delete ./usr ${RPM_BUILD_ROOT}

%clean
# Adding empty clean section per rpmlint.  In this particular case, there is 
# nothing to clean up as there is no build process

%files
%defattr(-,root,root)
%{_sbindir}/*
/etc/json-passwd/config

%changelog
* Wed Sep  9 2015 Tim Skirvin <tskirvin@fnal.gov>       1.0.0
- initial version
