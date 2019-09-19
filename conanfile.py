#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class ConanfontawesomedesktopConan(ConanFile):
    name = "Font-Awesome-Desktop"
    version = "5.11.1"
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
        sha256 = "971cea4af2b57b214994a03e3ed69a32e65b5fa2146efa88f289e962d118abcc"
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
