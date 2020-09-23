# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>


class State:
  """Internal keyboard layout state.

  This can be used to make the same key output different characters
  based on previous actions.

  Current implementation is very trivial and does not support multiple
  transitions, i.e. you cannot move from one custom state to another,
  you can only produce output.
  """

  def __init__(self, terminator):
    self._terminator = terminator

  def __getitem__(self, key):
    return self._transitions[key]

  def __setitem__(self, key, val):
    return self._transitions[key] = val

  @property
  def terminator(self):
    return self._terminator
