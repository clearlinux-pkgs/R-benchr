#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-benchr
Version  : 0.2.5
Release  : 43
URL      : https://cran.r-project.org/src/contrib/benchr_0.2.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/benchr_0.2.5.tar.gz
Summary  : High Precise Measurement of R Expressions Execution Time
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-benchr-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppProgress
BuildRequires : R-Rcpp
BuildRequires : R-RcppProgress
BuildRequires : buildreq-R

%description
the execution time of R expressions.

%package lib
Summary: lib components for the R-benchr package.
Group: Libraries

%description lib
lib components for the R-benchr package.


%prep
%setup -q -c -n benchr
cd %{_builddir}/benchr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640978748

%install
export SOURCE_DATE_EPOCH=1640978748
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library benchr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library benchr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library benchr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc benchr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/benchr/DESCRIPTION
/usr/lib64/R/library/benchr/INDEX
/usr/lib64/R/library/benchr/Meta/Rd.rds
/usr/lib64/R/library/benchr/Meta/features.rds
/usr/lib64/R/library/benchr/Meta/hsearch.rds
/usr/lib64/R/library/benchr/Meta/links.rds
/usr/lib64/R/library/benchr/Meta/nsInfo.rds
/usr/lib64/R/library/benchr/Meta/package.rds
/usr/lib64/R/library/benchr/NAMESPACE
/usr/lib64/R/library/benchr/NEWS.md
/usr/lib64/R/library/benchr/R/benchr
/usr/lib64/R/library/benchr/R/benchr.rdb
/usr/lib64/R/library/benchr/R/benchr.rdx
/usr/lib64/R/library/benchr/help/AnIndex
/usr/lib64/R/library/benchr/help/aliases.rds
/usr/lib64/R/library/benchr/help/benchr.rdb
/usr/lib64/R/library/benchr/help/benchr.rdx
/usr/lib64/R/library/benchr/help/paths.rds
/usr/lib64/R/library/benchr/html/00Index.html
/usr/lib64/R/library/benchr/html/R.css
/usr/lib64/R/library/benchr/tests/tinytest.R
/usr/lib64/R/library/benchr/tinytest/test-benchmark.R
/usr/lib64/R/library/benchr/tinytest/test-dots.R
/usr/lib64/R/library/benchr/tinytest/test-format.R
/usr/lib64/R/library/benchr/tinytest/test-mean.R
/usr/lib64/R/library/benchr/tinytest/test-order.R
/usr/lib64/R/library/benchr/tinytest/test-plot.R
/usr/lib64/R/library/benchr/tinytest/test-print.R
/usr/lib64/R/library/benchr/tinytest/test-summary.R
/usr/lib64/R/library/benchr/tinytest/test-timer.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/benchr/libs/benchr.so
/usr/lib64/R/library/benchr/libs/benchr.so.avx2
/usr/lib64/R/library/benchr/libs/benchr.so.avx512
