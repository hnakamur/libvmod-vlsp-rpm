%global libvmod_vslp_git_branch master

Name:              libvmod-vslp
Version:           20151209
Release:           1%{?dist}
Summary:           Varnish consistent hashing director VMOD
License:           FreeBSD
Source:            https://code.uplex.de/uplex-varnish/libvmod-vslp/archive-tarball/%{libvmod_vslp_git_branch}#/uplex-varnish-libvmod-vslp.tar.gz
URL:               https://www.varnish-cache.org/vmod/vlsp-consistent-hashing-director-vmod
Requires:          varnish >= 4.1.0
BuildRequires:     varnish-libs-devel >= 4.1.0
BuildRequires:     git
BuildRequires:     automake
BuildRequires:     autoconf
BuildRequires:     libtool
BuildRequires:     python-docutils

%description
Similar to the hash director, but provides more hashing stability when backend health state changes. Also provides additional control over backend selection and smooth ramp up for backends having become healthy again.

%prep
%setup -q -n uplex-varnish-%{name}

%build
./autogen.sh
./configure --prefix=%{_prefix}
make

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/varnish/vmods/libvmod_vslp.la

%files
%doc %{_docdir}/libvmod-vslp/LICENSE
%doc %{_docdir}/libvmod-vslp/README.rst
%doc %{_mandir}/man3/vmod_vslp.3.gz
%{_libdir}/varnish/vmods/libvmod_vslp.so

%changelog
* Wed Dec  9 2015 Hiroaki Nakamura <hnakamur@gmail.com> - 20151209-1
- Initial package
