# https://github.com/rocker-org/rocker-versioned2/blob/master/scripts/install_geospatial.sh
# * 已包含 python, data.table, fst
# FROM rocker/geospatial:latest
# * 指定 R 版本 221222
# FROM rocker/geospatial:4.2.2

# https://rocker-project.org/images/devcontainer/images.html#how-to-use
# https://github.com/rocker-org/devcontainer-images/pkgs/container/devcontainer%2Fgeospatial
# * 比前面的另加 dev container 需要的東西
FROM ghcr.io/rocker-org/devcontainer/geospatial:4

# https://rocker-project.org/use/extending.html#options
RUN install2.r --error --skipmissing --skipinstalled --ncpus -1 \
    bit64 \
    BiocManager \
    styler \
    stringr \
    readxl \
    languageserver \
    httpgd \
    vscDebugger \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/downloaded_packages \
    && strip /usr/local/lib/R/site-library/*/libs/*.so
