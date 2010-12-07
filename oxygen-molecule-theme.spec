Name:		oxygen-molecule-theme
Summary:	Oxygen Molecule theme for GTK
Version:	3.2
Release:	%mkrel 2
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

