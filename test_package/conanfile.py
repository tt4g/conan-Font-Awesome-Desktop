import os

from conans import ConanFile


class ConanfontawesomedesktopTestConan(ConanFile):

    def build(self):
        pass

    def imports(self):
        self.copy("LICENSE.txt", dst="", src="licenses", keep_path=False)
        self.copy("*", dst="metadata", src="metadata", keep_path=True)
        self.copy("*", dst="otfs", src="otfs", keep_path=True)
        self.copy("*", dst="svgs", src="svgs", keep_path=True)

    def _expected_exists(self, path):
        if not os.path.exists(path):
            raise Exception("file is not exists: {0}".format(path))

    def test(self):
        self._expected_exists("LICENSE.txt")
        self._expected_exists("metadata/icons.json")
        self._expected_exists("otfs/Font Awesome 5 Brands-Regular-400.otf")
        self._expected_exists("svgs/brands/accessible-icon.svg")
        self._expected_exists("svgs/regular/address-book.svg")
        self._expected_exists("svgs/solid/ad.svg")
