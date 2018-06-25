#!/bin/sh

cd /tmp

git clone -b patch-1 https://github.com/mkhl/xcodesnippet /tmp/xcodesnippet

cd xcodesnippet && rake build gem

gem install xcodesnippet-0.0.2.gem