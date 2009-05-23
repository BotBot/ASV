#!/bin/sh
rm -f doxygen/default.cfg &&
ln -s libwebcam.cfg doxygen/default.cfg &&
rm -rf doxygen-output &&
mkdir -p doxygen-output/libwebcam &&
sed -i -r -e 's/^\s*(rm -rf doxygen-output)$/# Automake sucks ... $1/' Makefile &&
make doxygen-doc &&
cp -v doxygen/res/* doxygen-output/libwebcam/html/
