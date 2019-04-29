## Package Status

| Bintray | Windows | Linux & macOS |
|:--------:|:---------:|:-----------------:|
| [![Download](https://api.bintray.com/packages/tt4g/conan-Font-Awesome-Desktop/Font-Awesome%3Att4g/images/download.svg)](https://bintray.com/tt4g/conan-Font-Awesome-Desktop/Font-Awesome%3Att4g/_latestVersion) | [![Build status](https://ci.appveyor.com/api/projects/status/ts6jqrxye3kw3lhx?svg=true)](https://ci.appveyor.com/project/tt4g/conan-font-awesome-desktop) | [![Build Status](https://travis-ci.com/tt4g/conan-Font-Awesome-Desktop.svg)](https://travis-ci.com/tt4g/conan-Font-Awesome-Desktop) |

## Overview

conan recipe of download Font Awesome Free Desktop.

## Add remote

`conan remote add tt4g-Font-Awesome-Desktop https://api.bintray.com/conan/tt4g/conan-Font-Awesome-Desktop`

## Example

`conanfile.txt`:

```plaintext
[build_requires]
Font-Awesome/5.8.1@tt4g/stable

[imports]
# Copy Font-Awesome icon svg.
., *.svg -> ./resources/icons @ root_package=Font-Awesome, folder=True, ignore_case=True, keep_path=True
., license* -> ./licenses @ folder=True, ignore_case=True, excludes=*.html *.jpeg
```
