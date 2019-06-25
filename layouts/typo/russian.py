# SPDX-License-Identifier: MPL-2.0
# © 2019 Kirill Elagin <kirelagin@gmail.com>

from layers import russian, typo
from layout import TypoLayout


layout = TypoLayout(
  25, 28911, 'Russian',
  alpha=russian.alpha, alpha_shifted={k: v.upper() for k,v in russian.alpha.items()},
  numsym=russian.numsym, numsym_shifted=russian.numsym_shifted,
  typo=typo.normal, typo_shifted=typo.shifted
)

if __name__ == '__main__':
  print('\n'.join(layout.yield_xml()))
