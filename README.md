# C3-rpm

This repository contains RPM packaging files for [the C3 COPR](https://copr.fedorainfracloud.org/coprs/sisyphus1813/c3/) which contains an unofficial package for the C3 compiler.  
[C3 Upstream repository](https://github.com/c3lang/c3c)  


## Installation

```bash
sudo dnf copr enable sisyphus1813/c3
sudo dnf install -y c3
```
This installs the C3 compiler and standard library.

## Compatibility
C3 currently only builds on F43. F44 is broken due to toolchain issues (LLVM/Clang + RPM flags). Looking into this further but we are most likely waiting on upstream Fedora fixes.