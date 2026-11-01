// SPDX-License-Identifier: BSD-2-Clause-Patent
//
// libpicasso-sb.dylib (probe): a do-nothing library the kernel inserts into
// SpringBoard on this board (boot-arg picasso_inject_sb=PATH, see
// bsd/kern/kern_exec.c). Its only job is to prove the injection pipeline works
// end to end: the kernel added DYLD_INSERT_LIBRARIES, AMFI allowed an ad-hoc
// signed library into the process (amfi_allow_any_signature / cs_enforcement_
// disable boot-args), and dyld mapped it and ran its constructor.
//
// It writes one line to /dev/console (the only log that reaches the USB
// console this early) and returns. No SpringBoard class, method, or state is
// touched here. The device-specific logic that would belong in a real
// injected library is NOT in this file.
#include <fcntl.h>
#include <string.h>
#include <unistd.h>

__attribute__((constructor))
static void picasso_sb_probe(void)
{
    static const char line[] = "PICASSO_SBINJECT probe library loaded into SpringBoard\n";
    int fd = open("/dev/console", O_WRONLY);
    if (fd >= 0) {
        (void)write(fd, line, strlen(line));
        close(fd);
    }
}
