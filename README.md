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

* `cd src`
* `python3 -c 'from layout import write_english_typo; write_english_typo()' > typo.keylayout`

Then install it with:

* `cp typo.keylayout ~/Library/"Keyboard Layouts"/`


TODO
-----

* Support dead keys for combining diacritics
* Figure out how to handle ISO keyboards (ISO Section key)
