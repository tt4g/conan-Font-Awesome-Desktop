#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class ConanfontawesomedesktopConan(ConanFile):
    name = "Font-Awesome-Desktop"
    version = "5.13.0"
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
        sha256 = "5d54c86956e7b118f14c03d080882fd76c17cbb577d53b74237af22114658da8"
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
