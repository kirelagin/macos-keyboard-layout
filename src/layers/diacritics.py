# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>

# Diacritics layer.
# This is layer is different from others, as it is not meant to be ovarlayed
# on top of other layers (although it can be used this way too). Its primary
# purpose is providing a map of diacrticis that is later handled in
# a non-trivial manner (using dead-keys) in the Typography layout.
#
# Based on the Typography Layout by Ilya Birman.
#
# The differences are:
# * No acute on / to avoid duplication

layer = {
  "'": '´',
  'q': '˘',
}
