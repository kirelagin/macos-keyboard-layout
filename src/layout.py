# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>

import re
import xml.etree.cElementTree as ET

from layer import combine_layers, resolve_map
from layers import english, typo
from maps import other, special


doctype = '<!DOCTYPE keyboard SYSTEM "file://localhost/System/Library/DTDs/KeyboardLayout.dtd">'

# This is a temporary function.
# TODO: Generalise it.
def write_english_typo():
  keyboard = ET.Element("keyboard", group="126", id="-8324", name="English (US) Typo", maxout="1")

  layouts = ET.SubElement(keyboard, "layouts")
  layout = ET.SubElement(layouts, "layout", first="0", last="17", mapSet="ANSI", modifiers="Mods")

  modMap = ET.SubElement(keyboard, "modifierMap", id="Mods", defaultIndex="0")
  mod0 = ET.SubElement(modMap, "keyMapSelect", mapIndex="0")
  ET.SubElement(mod0, "modifier", keys="")
  mod1 = ET.SubElement(modMap, "keyMapSelect", mapIndex="1")
  ET.SubElement(mod1, "modifier", keys="anyShift")
  mod2 = ET.SubElement(modMap, "keyMapSelect", mapIndex="2")
  ET.SubElement(mod2, "modifier", keys="anyOption")
  mod3 = ET.SubElement(modMap, "keyMapSelect", mapIndex="3")
  ET.SubElement(mod3, "modifier", keys="anyShift anyOption")

  kms = ET.SubElement(keyboard, "keyMapSet", id="ANSI")

  write_map(ET.SubElement(kms, "keyMap", index="0"), combine_layers(special.id_char, other.id_char, resolve_map(english.normal)))
  write_map(ET.SubElement(kms, "keyMap", index="1"), combine_layers(special.id_char, other.id_char, resolve_map(english.shifted)))
  write_map(ET.SubElement(kms, "keyMap", index="2"), combine_layers(special.id_char, resolve_map(typo.normal)))
  write_map(ET.SubElement(kms, "keyMap", index="3"), combine_layers(special.id_char, resolve_map(typo.shifted)))

  tree = ET.ElementTree(keyboard)
  print('<?xml version="1.1" encoding="UTF-8"?>')
  print(doctype)

  s = ET.tostring(keyboard, encoding='unicode')
  #s = re.sub(r'"\\x(..)"', r'"&#x\1;"', s)
  s = re.sub(r'"&#10;"', r'"&#x0D;"', s)  # TODO: wtf?
  s = re.sub(r'"&#09;"', r'"&#x09;"', s)  # TODO: wtf?
  #s = re.sub(r'"&[a-z]*;"', r'"X"', s)
  s = re.sub(r'><', '>\n<', s)
  print(s)


def write_map(el, layer):
  for k, v in layer.items():
    ET.SubElement(el, "key", code=str(k), output=v)
