<!-- SPDX-License-Identifier: MPL-2.0 -->
<!-- © 2019 Kirill Elagin <kirelagin@gmail.com> -->

_This tool is WIP_

macOS keyboard layout generator
================================

This small tool simplifies creating custom keyboard layouts for macOS.


Typography layouts
-------------------

This repository also contains everything needed to build a typography layout. The
typography layer is based on the [`typo` modifier from `xkeyboard-config`][typo-xkbd],
which in turn is based on the [Typography Layout by Ilya Birman][typo-birman].

[typo-xkbd]: https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config/blob/master/symbols/typo
[typo-birman]: https://ilyabirman.net/projects/typography-layout/

You can build an English Typography layout by doing:

* `PYTHONPATH=src python3 src/layouts/typo/english.py > english_typo.keylayout`

Then install it with:

* `cp english_typo.keylayout ~/Library/"Keyboard Layouts"/`
