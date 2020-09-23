// SPDX-License-Identifier: MPL-2.0
// © 2019 Kirill Elagin <kirelagin@gmail.com>

/* Outputs the keyboard hardware ID.
 *
 * When multiple keyboards are connected, apparently, the id will
 * be that of the keyboard used most recently.
 *
 * Compile with:
 *   clang -framework CoreGraphics
 */

#include <CoreGraphics/CGEventSource.h>
#include <CoreGraphics/CGEventTypes.h>
#include <stdio.h>


int main() {
  // Not sure what the constant used to create an event source means,
  // but it doesn’t seem to affect the result.
  CGEventSourceRef eventSource = CGEventSourceCreate(kCGEventSourceStatePrivate);
  CGEventSourceKeyboardType kbdt = CGEventSourceGetKeyboardType(eventSource);

  printf("Keyboard type: %d\n", kbdt);

  return 0;
}
