Name:		oxygen-molecule-theme
Summary:	Oxygen Molecule theme for GTK
Version:	2.2
Release:	%mkrel 1
Source0:	http://www.kde-look.org/CONTENT/content-files/103741-Oxygen-Molecule_%{version}_theme.tar.gz
URL:		http://www.kde-look.org/content/show.php?content=103741
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
Requires:	gtk2
Requires:	gtk-engines2
Suggests:	systemsettings-qt-gtk
BuildArch:	noarch

%description
Oxygen-Molecule is a theme for GTK+ applications to provide a uniform look when
used under the KDE 4 desktop environment.

%prep 
%setup -q -c -n %{name}-%{version}
%__tar -xzf kde43-oxygen-molecule.tar.gz
%__chmod 644 kde43-oxygen-molecule/gtk-2.0/*/* OxygenMolecule.colors
%__rm -f kde43-oxygen-molecule/gtk-2.0/*/.directory Oxygen-Molecule\ %{version}\ setup\ guide.odt

%build

%install
%__rm -rf %{buildroot}
%__install -d %{buildroot}%{_datadir}/themes
%__mv kde43-oxygen-molecule %{buildroot}%{_datadir}/themes/Oxygen-Molecule

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc Oxygen-Molecule\ %{version}\ setup\ guide.pdf  OxygenMolecule.colors  Oxygen-Molecule-screenshot2.png
%{_datadir}/themes/Oxygen-Molecule

