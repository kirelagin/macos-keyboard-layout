# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>

from maps import main
from maps import other
from maps import special


def resolve_map(key_map):
  """Translate ANSI human-readable key names to ids.

  >>> resolve_map({'a': 'A', '/': '?'})
  {0: 'A', 44: '?'}
  """

  user_id = {main.key_id[k]: v for k, v in key_map.items()}

  # User is not trying to map a special key
  assert(not(special.id_char.keys() & user_id.keys()))
  # User is not trying to map an other key
  assert(not(other.id_char.keys() & user_id.keys()))

  return user_id


def combine_layers(*layers):
  """Merge multiple id maps into one, left to right.

  >>> combine_layers({1: 'A', 2: '?'}, {2: 'B', 3: 'C'})
  {1: 'A', 2: 'B', 3: 'C'}
  """

  result = {}
  for layer in layers:
    layer = {k: v for k, v in layer.items() if v is not None}
    result.update(layer)

  return result
