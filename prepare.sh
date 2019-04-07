#!/bin/bash

ln -sf "$PWD" /usr/local/rpm-specs/automake116

. /usr/local/rpm-specs/setup_env.sh

yum -y install scl-utils-build

build_package automake116

