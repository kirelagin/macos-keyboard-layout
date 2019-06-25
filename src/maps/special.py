# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>


# Keys that are mapped to various special actions, i.e. they do not produce
# a printable character when typed.
#
# The idea is that these keys probably should be mapped on all levels.
#
# * The ones mapped not to None come from the default Ukelele layout.
#   I am not sure what is the meaning of those mysterious code points that
#   Ukelele maps them to, so we just do the same.
# * The ones mapped to None are not form Ukelele, but rather were added
#   by myself for completeness. We don’t map them because I have no idea
#   how to determine the correct code point.
id_char = {
  36: '\u000D',  # enter
  48: '\u0009',  # tab
  51: '\u0008',  # delete
  53: '\u001B',  # esc
  54: None,  # right command
  55: None,  # command
  56: None,  # shift
  57: None,  # caps lock
  58: None,  # option
  59: None,  # control
  60: None,  # right shift
  61: None,  # right option
  62: None,  # right control
  63: None,  # bottom-left fn

  72: '\u001F',  # volume up
  73: None,  # volume down
  74: None,  # mute

  # Arrows and block above them
  114: '\u0005',  # help (or top-right fn?)
  115: '\u0001',  # home
  116: '\u000B',  # page up
  117: '\u007F',  # delete forward
  119: '\u0004',  # end
  121: '\u000C',  # page down
  123: '\u001C',  # Left
  124: '\u001D',  # Right
  125: '\u001F',  # Down
  126: '\u001E',  # Up

  # F keys
  122: '\u0010',  # f1
  120: '\u0010',  # f2
  99:  '\u0010',  # f3
  118: '\u0010',  # f4
  96:  '\u0010',  # f5
  97:  '\u0010',  # f6
  98:  '\u0010',  # f7
  100: '\u0010',  # f8
  101: '\u0010',  # f9
  109: '\u0010',  # f10
  103: '\u0010',  # f11
  111: '\u0010',  # f12
  105: '\u0010',  # f13
  107: '\u0010',  # f14
  113: '\u0010',  # f15
  106: '\u0010',  # f16
  64:  '\u0010',  # f17
  79:  '\u0010',  # f18
  80:  '\u0010',  # f19
  90:  '\u0010',  # f20

  # Numpad keyboard on the right
  71: '\u001B',  # Clear
  76: '\u0003',  # Enter

  # Unknown (??)
  52:  None,
  66:  '\u001D',
  68:  None,
  70:  '\u001C',
  77:  '\u001E',
  108: None,
  110: None,
  112: None,
  127: None,
}

