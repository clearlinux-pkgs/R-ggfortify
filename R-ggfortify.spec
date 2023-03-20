#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-ggfortify
Version  : 0.4.16
Release  : 15
URL      : https://cran.r-project.org/src/contrib/ggfortify_0.4.16.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ggfortify_0.4.16.tar.gz
Summary  : Data Visualization Tools for Statistical Analysis Results
Group    : Development/Tools
License  : MIT
Requires: R-dplyr
Requires: R-ggplot2
Requires: R-gridExtra
Requires: R-scales
Requires: R-stringr
Requires: R-tibble
Requires: R-tidyr
BuildRequires : R-dplyr
BuildRequires : R-ggplot2
BuildRequires : R-gridExtra
BuildRequires : R-scales
BuildRequires : R-stringr
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
time series, PCA families, clustering and survival analysis. The package offers
    a single plotting interface for these analysis results and plots in a unified
    style using 'ggplot2'.

%prep
%setup -q -n ggfortify
cd %{_builddir}/ggfortify

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679329638

%install
export SOURCE_DATE_EPOCH=1679329638
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
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ggfortify/CITATION
/usr/lib64/R/library/ggfortify/DESCRIPTION
/usr/lib64/R/library/ggfortify/INDEX
/usr/lib64/R/library/ggfortify/LICENSE
/usr/lib64/R/library/ggfortify/Meta/Rd.rds
/usr/lib64/R/library/ggfortify/Meta/features.rds
/usr/lib64/R/library/ggfortify/Meta/hsearch.rds
/usr/lib64/R/library/ggfortify/Meta/links.rds
/usr/lib64/R/library/ggfortify/Meta/nsInfo.rds
/usr/lib64/R/library/ggfortify/Meta/package.rds
/usr/lib64/R/library/ggfortify/Meta/vignette.rds
/usr/lib64/R/library/ggfortify/NAMESPACE
/usr/lib64/R/library/ggfortify/NEWS.md
/usr/lib64/R/library/ggfortify/R/ggfortify
/usr/lib64/R/library/ggfortify/R/ggfortify.rdb
/usr/lib64/R/library/ggfortify/R/ggfortify.rdx
/usr/lib64/R/library/ggfortify/doc/basics.R
/usr/lib64/R/library/ggfortify/doc/basics.Rmd
/usr/lib64/R/library/ggfortify/doc/basics.html
/usr/lib64/R/library/ggfortify/doc/index.html
/usr/lib64/R/library/ggfortify/doc/plot_dist.R
/usr/lib64/R/library/ggfortify/doc/plot_dist.Rmd
/usr/lib64/R/library/ggfortify/doc/plot_dist.html
/usr/lib64/R/library/ggfortify/doc/plot_lm.R
/usr/lib64/R/library/ggfortify/doc/plot_lm.Rmd
/usr/lib64/R/library/ggfortify/doc/plot_lm.html
/usr/lib64/R/library/ggfortify/doc/plot_map.R
/usr/lib64/R/library/ggfortify/doc/plot_map.Rmd
/usr/lib64/R/library/ggfortify/doc/plot_map.html
/usr/lib64/R/library/ggfortify/doc/plot_pca.R
/usr/lib64/R/library/ggfortify/doc/plot_pca.Rmd
/usr/lib64/R/library/ggfortify/doc/plot_pca.html
/usr/lib64/R/library/ggfortify/doc/plot_surv.R
/usr/lib64/R/library/ggfortify/doc/plot_surv.Rmd
/usr/lib64/R/library/ggfortify/doc/plot_surv.html
/usr/lib64/R/library/ggfortify/doc/plot_ts.R
/usr/lib64/R/library/ggfortify/doc/plot_ts.Rmd
/usr/lib64/R/library/ggfortify/doc/plot_ts.html
/usr/lib64/R/library/ggfortify/help/AnIndex
/usr/lib64/R/library/ggfortify/help/aliases.rds
/usr/lib64/R/library/ggfortify/help/ggfortify.rdb
/usr/lib64/R/library/ggfortify/help/ggfortify.rdx
/usr/lib64/R/library/ggfortify/help/paths.rds
/usr/lib64/R/library/ggfortify/html/00Index.html
/usr/lib64/R/library/ggfortify/html/R.css
/usr/lib64/R/library/ggfortify/tests/test-all.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-MSwM.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-backcompat.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-base-infer.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-base.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-base_ts.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-basis.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-changepoint.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-cluster.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-forecast.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-glmnet.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-maps.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-performance.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-plotlib.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-raster.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-spatial.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-stats-density.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-stats-lm.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-stats.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-surv.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-ts.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-tslib.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-util.R
/usr/lib64/R/library/ggfortify/tests/testthat/test-vars.R
