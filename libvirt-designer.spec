#
# Conditional build:
%bcond_without	vala	# Vala binding

Summary:	Libvirt configuration designer
Summary(pl.UTF-8):	Biblioteka do projektowania konfiguracji libvirt
Name:		libvirt-designer
Version:	0.0.2
Release:	5
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://libvirt.org/libvirt/designer/%{name}-%{version}.tar.gz
# Source0-md5:	53e0b1e3f28dbf927c68c03e675967c9
URL:		http://libvirt.org/
BuildRequires:	gobject-introspection-devel >= 0.10.8
BuildRequires:	libosinfo-devel >= 0.2.7
BuildRequires:	libvirt-glib-devel >= 0.1.7
BuildRequires:	pkgconfig >= 1:0.9.0
%if %{with vala}
BuildRequires:	vala >= 2:0.13
BuildRequires:	vala-libosinfo >= 0.2.7
BuildRequires:	vala-libvirt-glib >= 0.1.7
%endif
Requires:	libosinfo >= 0.2.7
Requires:	libvirt-glib >= 0.1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libvirt-designer package provides an API to facilitate policy
based configuration of libvirt objects. It uses libosinfo to drive the
configuration of virtual machines with hardware that is optimized for
the current hypervisor platform.

%description -l pl.UTF-8
Pakiet libvirt-designer udostępnia API ułatwiające konfigurację
obiektów libvirt w oparciu o politykę. Wykorzystuje libosinfo do
sterowania konfiguracją maszyn wirtualnych ze sprzętem
zoptymalizowanym dla bieżącej platformy hipernadzorcy.

%package devel
Summary:	Header files for libvirt-designer library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvirt-designer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libosinfo-devel >= 0.2.7
Requires:	libvirt-glib-devel >= 0.1.7

%description devel
Header files for libvirt-designer library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvirt-designer.

%package static
Summary:	Static libvirt-designer library
Summary(pl.UTF-8):	Statyczna biblioteka libvirt-designer
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libvirt-designer library.

%description static -l pl.UTF-8
Statyczna biblioteka libvirt-designer.

%package apidocs
Summary:	libvirt-designer API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libvirt-designer
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
libvirt-designer API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libvirt-designer.

%package -n vala-libvirt-designer
Summary:	Vala API for libvirt-designer library
Summary(pl.UTF-8):	API języka Vala do biblioteki libvirt-designer
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala-libosinfo >= 0.2.7
Requires:	vala-libvirt-glib >= 0.1.7
BuildArch:	noarch

%description -n vala-libvirt-designer
Vala API for libvirt-designer library.

%description -n vala-libvirt-designer -l pl.UTF-8
API języka Vala do biblioteki libvirt-designer.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--enable-vala%{!?with_vala:=no} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/virt-designer
%attr(755,root,root) %{_libdir}/libvirt-designer-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvirt-designer-1.0.so.1
%{_libdir}/girepository-1.0/LibvirtDesigner-1.0.typelib
%{_mandir}/man1/virt-designer.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvirt-designer-1.0.so
%{_includedir}/libvirt-designer-1.0
%{_datadir}/gir-1.0/LibvirtDesigner-1.0.gir
%{_pkgconfigdir}/libvirt-designer-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvirt-designer-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libvirt-designer

%if %{with vala}
%files -n vala-libvirt-designer
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libvirt-designer-1.0.deps
%{_datadir}/vala/vapi/libvirt-designer-1.0.vapi
%endif
