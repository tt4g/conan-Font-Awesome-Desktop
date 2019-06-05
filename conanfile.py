#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class ConanfontawesomedesktopConan(ConanFile):
    name = "Font-Awesome-Desktop"
    version = "5.9.0"
    settings = None
    description = "The iconic SVG, font, and CSS toolkit https://fontawesome.com"
    url = "https://github.com/tt4g/conan-Font-Awesome-Desktop"
    homepage = "https://github.com/FortAwesome/Font-Awesome/"
    license = "Font Awesome Free License"
    author = "tt4g"
    topics = ("conan", "Font-Awesome")
    exports = "LICENSE"
    _source_subfolder = "source_subfolder"

    def source(self):
        extracted_dir = "fontawesome-free-{0}-desktop".format(self.version)
        sha256 = "8ec9355ee65736e02ec75574e4d5dc5119506ca9cb287d6e5747366d75cdf7be"
        tools.get("{0}/releases/download/{1}/{2}.zip".format(self.homepage, self.version, extracted_dir),
                  sha256=sha256)
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        pass

    def package(self):
        self.copy("LICENSE.txt", dst="licenses", src=self._source_subfolder)
        self.copy("*", dst="", src=self._source_subfolder,
                  excludes="LICENSE.txt", keep_path=True)

    def package_info(self):
        pass
