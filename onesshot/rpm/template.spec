Name:       onesshot

Summary:    oneSSHot Ambience
Version:    0.0.1
Release:    1
Group:      System/GUI/Other
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake

Requires:   ambienced

%description
This is a template ambience description

%package ts-devel
Summary:   Translation source for template ambience
License:   TBD
Group:     System/GUI/Other

%description ts-devel
Translation source for a template ambience

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post



%files
%defattr(-,root,root,-)
%{_datadir}/ambience/onesshot/onesshot.ambience
%{_datadir}/ambience/onesshot/sounds.index
%{_datadir}/ambience/onesshot/images/*
%{_datadir}/ambience/onesshot/sounds/*
%{_datadir}/translations/onesshot_eng_en.qm

%files -n onesshot-ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/onesshot.ts
