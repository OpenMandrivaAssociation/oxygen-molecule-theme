Name:		oxygen-molecule-theme
Summary:	Oxygen Molecule theme for GTK
Version:	3.2
Release:	3
Source0:	http://www.kde-look.org/CONTENT/content-files/103741-Oxygen-Molecule_%{version}_theme.tar.gz
URL:		http://www.kde-look.org/content/show.php?content=103741
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
BuildRequires:	kde4-macros
Requires:	gtk2
Requires:	gtk-engines2
Suggests:	systemsettings-qt-gtk
BuildArch:	noarch

%description
Oxygen-Molecule is a theme for GTK+ applications to provide a uniform look when
used under the KDE 4 desktop environment.

%prep 
%setup -q -c -n %{name}-%{version}
%__tar -xzf kde44-oxygen-molecule.tar.gz
%__chmod 644 kde44-oxygen-molecule/gtk-2.0/*/* kde44-oxygen-molecule-flat/gtk-2.0/*/* Oxygen-Molecule_3.0.colors
%__rm -f Oxygen-Molecule\ %{version}\ setup\ guide.odt

%build

%install
%__rm -rf %{buildroot}
%__install -d %{buildroot}%{_datadir}/themes %{buildroot}%{_kde_appsdir}/color-schemes
%__mv kde44-oxygen-molecule %{buildroot}%{_datadir}/themes/Oxygen-Molecule
%__mv kde44-oxygen-molecule-flat %{buildroot}%{_datadir}/themes/Oxygen-Molecule-Flat
%__mv Oxygen-Molecule_3.0.colors %{buildroot}%{_kde_appsdir}/color-schemes/OxygenMolecule.colors

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc Oxygen-Molecule\ %{version}\ setup\ guide.pdf Oxygen-Molecule-screenshot1.png
%{_datadir}/themes/Oxygen-Molecule
%{_datadir}/themes/Oxygen-Molecule-Flat
%{_kde_appsdir}/color-schemes/OxygenMolecule.colors



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2-2mdv2011.0
+ Revision: 613546
- rebuild

* Thu Apr 08 2010 Luc Menut <lmenut@mandriva.org> 3.2-1mdv2010.1
+ Revision: 533257
- update to 3.2

* Sun Mar 21 2010 Luc Menut <lmenut@mandriva.org> 3.1-1mdv2010.1
+ Revision: 525946
- add kde4-macros as buildrequires
- update to 3.1
- updated theme to match KDE 4.4 widgets and shading
- update file list

* Wed Jan 13 2010 Luc Menut <lmenut@mandriva.org> 2.2-1mdv2010.1
+ Revision: 491063
- import oxygen-molecule-theme


