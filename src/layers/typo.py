# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>

# Typography layer.
# Based on the `typo` modifier from `xkeyboard-config`,
# which in turn is based on the Typography Layout by Ilya Birman.
#
# We closely follow `typo`, except for the following changes:
#
# * Added ₽ for h as in the Typography Layout
# * TODO: implement combining dead keys

normal = {
  '1': '¹',
  '2': '²',
  '3': '³',
  '4': '$',
  '5': '‰',
  '6': '↑',
  '7': '&',
  '8': '∞',
  '9': '←',
  '0': '→',
  '-': '—',
  '=': '≠',

  'e': '€',
  'r': '®',
  't': '™',
  'y': '¥',
  'p': '´',
  '[': '[',
  ']': ']',

  # 'a': '\x0301',  # combining acute accent
  's': '§',
  'd': '°',
  'f': '£',
  'j': '„',
  'k': '“',
  'l': '”',
  ';': '‘',
  "'": "’",

  'x': '×',
  'c': '©',
  'v': '↓',
  'm': '−',
  ',': '«',
  '.': '»',
  '/': '…',

  ' ': ' ',
}

shifted = {
  '`': '≈',
  '1': '¡',
  '2': '½',
  '3': '⅓',
  '4': '¼',
  '6': None,  # TODO: replace with dead
  '7': '¿',
  '8': '⅛',
  '-': '–',
  '=': '±',

  'q': None,  # TODO: replace with dead
  'r': None,  # TODO: replace with dead
  'p': '˝',
  '[': '{',
  ']': '}',
 '\\': None,  # TODO: replace with dead

  'd': '÷',
  'h': '₽',
  'j': '‚',
  'k': '‘',
  'l': '’',
  ';': '′',  # TODO: replace with dead
  "'": '″',

  'z': None,  # TODO: replace with dead
  'x': '·',
  'c': '¢',
  'v': '◊',  # TODO: replace with dead
  'm': '•',
  'n': None,  # TODO: replace with dead
  ',': '<',
  '.': '>',
  '/': None,  # TODO: replace with dead

  ' ': ' ',
}
