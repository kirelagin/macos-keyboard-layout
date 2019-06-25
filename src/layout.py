# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>

from collections import OrderedDict
import re
import xml.etree.cElementTree as ET

from key_map import IdMap
from layers import english, typo
from maps import other, special


class Layout:
  """A keyboard layout consisting of multiple levels."""

  def __init__(self, group, id, name, levels):
    """Create a new keyboard layout.

    levels: ordered map from modifiers list to IdMap
    """
    self._group = group
    self._id = id
    self._name = name
    self._levels = levels

  # XML
  def yield_xml(self):
    yield '<?xml version="1.1" encoding="UTF-8"?>'
    yield '<!DOCTYPE keyboard SYSTEM "file://localhost/System/Library/DTDs/KeyboardLayout.dtd">'
    yield '<keyboard group="{}" id="{}" name="{}" maxout="1">'.format(self._group, self._id, self._name)

    def yield_layouts():
      yield '<layouts>'
      yield '<layout first="0" last="17" mapSet="ANSI" modifiers="Mods"/>'
      yield '</layouts>'
    for line in yield_layouts():
      yield line

    def yield_modifier_map():
      yield '<modifierMap id="Mods" defaultIndex="0">'
      for index, mods in enumerate(self._levels.keys()):
        yield '  <keyMapSelect mapIndex="{}">'.format(index)
        yield '    <modifier keys="{}"/>'.format(mods)
        yield '  </keyMapSelect>'
      yield '</modifierMap>'
    for line in yield_modifier_map():
      yield line

    def yield_key_map_sets():
      yield '<keyMapSet id="ANSI">'
      for index, id_map in enumerate(self._levels.values()):
        for line in id_map.yield_xml(index):
          yield '  ' + line
      yield '</keyMapSet>'
    for line in yield_key_map_sets():
      yield line

    yield '</keyboard>'

# This is a temporary function.
# TODO: Generalise it.
def write_english_typo():
  layers = OrderedDict([
    ('', IdMap(special.id_char) | IdMap(other.id_char) | IdMap.from_keymap(english.normal)),
    ('anyShift', IdMap(special.id_char) | IdMap(other.id_char) | IdMap.from_keymap(english.shifted)),
    ('anyOption', IdMap(special.id_char) | IdMap.from_keymap(typo.normal)),
    ('anyShift anyOption', IdMap(special.id_char) | IdMap.from_keymap(typo.shifted)),
  ])

  layout = Layout(0, -8324, 'English (US) Typo', layers)

  print('\n'.join(layout.yield_xml()))
