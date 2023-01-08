
# Intro

List of rust libraries, currated by AOSP rust developers.
Script available in this repo finds the rust libraries in a aosp tree, sorted by crates.io categories
End of the file, you can also find the list of aosp component written in rust along with the open source libraries that they use

# Contents

## available crates sorted by categories

- [API bindings](#api-bindings)
- [Algorithms](#algorithms)
- [Asynchronous](#asynchronous)
- [Command-line interface](#command-line-interface)
- [Compression](#compression)
- [Concurrency](#concurrency)
- [Cryptography](#cryptography)
- [Data structures](#data-structures)
- [Database interfaces](#database-interfaces)
- [Date and time](#date-and-time)
- [Development tools](#development-tools)
- [Development tools::Build Utils](#development-toolsbuild-utils)
- [Development tools::Debugging](#development-toolsdebugging)
- [Development tools::FFI](#development-toolsffi)
- [Development tools::Procedural macro helpers](#development-toolsprocedural-macro-helpers)
- [Development tools::Profiling](#development-toolsprofiling)
- [Development tools::Testing](#development-toolstesting)
- [Embedded development](#embedded-development)
- [Emulators](#emulators)
- [Encoding](#encoding)
- [External FFI bindings](#external-ffi-bindings)
- [Filesystem](#filesystem)
- [Game engines](#game-engines)
- [Hardware support](#hardware-support)
- [Memory management](#memory-management)
- [Network programming](#network-programming)
- [Operating systems](#operating-systems)
- [Operating systems::Unix APIs](#operating-systemsunix-apis)
- [Parser implementations](#parser-implementations)
- [Parsing tools](#parsing-tools)
- [Rendering::Graphics APIs](#renderinggraphics-apis)
- [Rust patterns](#rust-patterns)
- [Science](#science)
- [Template engine](#template-engine)
- [Text processing](#text-processing)
- [Value formatting](#value-formatting)
- [Visualization](#visualization)
- [Web programming](#web-programming)
- [WebAssembly](#webassembly)

## [AOSP rust components](#rust-components-found-in-aosp)

# Crates

## API bindings

### android_logger

<details><summary>
A logging implementation for `log` which hooks to android log output.


</summary>

- https://crates.io/crates/android_logger
- https://github.com/Nercury/android_logger-rs

</details><details><summary>
21 uses

</summary>

- [device/google/cuttlefish/guest/hals/keymint/rust](https://cs.android.com/android/platform/superproject/+/master:device/google/cuttlefish/guest/hals/keymint/rust)
- [hardware/interfaces/security/dice/aidl/default](https://cs.android.com/android/platform/superproject/+/master:hardware/interfaces/security/dice/aidl/default)
- [packages/modules/Bluetooth/system/gd/rust/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/common)
- [packages/modules/Virtualization/authfs](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs)
- [packages/modules/Virtualization/authfs/fd_server](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/fd_server)
- [packages/modules/Virtualization/authfs/service](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/service)
- [packages/modules/Virtualization/authfs/tests/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/tests/common)
- [packages/modules/Virtualization/compos](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos)
- [packages/modules/Virtualization/compos/composd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/composd)
- [packages/modules/Virtualization/compos/verify](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/verify)
- [packages/modules/Virtualization/encryptedstore](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/encryptedstore)
- [packages/modules/Virtualization/rialto](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/rialto)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)
- [packages/modules/Virtualization/vm_payload](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vm_payload)
- [packages/modules/Virtualization/vmbase/example](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vmbase/example)
- [system/core/trusty/keymint](https://cs.android.com/android/platform/superproject/+/master:system/core/trusty/keymint)
- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)
- [system/logging/rust](https://cs.android.com/android/platform/superproject/+/master:system/logging/rust)
- [system/security/diced](https://cs.android.com/android/platform/superproject/+/master:system/security/diced)
- [system/security/keystore2](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2)
- [system/security/keystore2/selinux](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/selinux)

</details>

### flate2

<details><summary>
DEFLATE compression and decompression exposed as Read/BufRead/Write streams.
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip,
and raw deflate streams.


</summary>

- https://crates.io/crates/flate2
- https://docs.rs/flate2
- https://github.com/rust-lang/flate2-rs

</details>

### jni

<details><summary>
Rust bindings to the JNI

</summary>

- https://crates.io/crates/jni
- https://docs.rs/jni
- https://github.com/jni-rs/jni-rs

</details><details><summary>
2 uses

</summary>

- [packages/modules/Uwb/indev_uwb_adaptation](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Uwb/indev_uwb_adaptation)
- [packages/modules/Uwb/service/uci/jni](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Uwb/service/uci/jni)

</details>

### libloading

<details><summary>
Bindings around the platform's dynamic library loading primitives with greatly improved memory safety.

</summary>

- https://crates.io/crates/libloading
- https://docs.rs/libloading/
- https://github.com/nagisa/rust_libloading/

</details>

### openssl

<details><summary>
OpenSSL bindings

</summary>

- https://crates.io/crates/openssl
- https://github.com/sfackler/rust-openssl

</details><details><summary>
6 uses

</summary>

- [packages/modules/Virtualization/authfs](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs)
- [packages/modules/Virtualization/authfs/src/fsverity/metadata](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/src/fsverity/metadata)
- [packages/modules/Virtualization/libs/apkverify](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/apkverify)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [system/keymint/boringssl](https://cs.android.com/android/platform/superproject/+/master:system/keymint/boringssl)
- [system/security/keystore2/tests](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests)

</details>

## Algorithms

### ahash

<details><summary>
A non-cryptographic hash function using AES-NI for high performance

</summary>

- https://crates.io/crates/ahash
- https://docs.rs/ahash
- https://github.com/tkaitchuck/ahash

</details>

### crossbeam-channel

<details><summary>
Multi-producer multi-consumer channels for message passing

</summary>

- https://crates.io/crates/crossbeam-channel
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-channel

</details>

### crossbeam-deque

<details><summary>
Concurrent work-stealing deque

</summary>

- https://crates.io/crates/crossbeam-deque
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-deque

</details>

### crossbeam-utils

<details><summary>
Utilities for concurrent programming

</summary>

- https://crates.io/crates/crossbeam-utils
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-utils

</details>

### fallible-iterator

<details><summary>
Fallible iterator traits

</summary>

- https://crates.io/crates/fallible-iterator
- https://github.com/sfackler/rust-fallible-iterator

</details>

### fxhash

<details><summary>
A fast, non-secure, hashing algorithm derived from an internal hasher used in FireFox and Rustc.

</summary>

- https://crates.io/crates/fxhash
- https://docs.rs/fxhash
- https://github.com/cbreeden/fxhash

</details>

### itertools

<details><summary>
Extra iterator adaptors, iterator methods, free functions, and macros.

</summary>

- https://crates.io/crates/itertools
- https://docs.rs/itertools/
- https://github.com/rust-itertools/itertools

</details>

### num-bigint

<details><summary>
Big integer implementation for Rust

</summary>

- https://crates.io/crates/num-bigint
- https://docs.rs/num-bigint
- https://github.com/rust-num/num-bigint

</details>

### num-integer

<details><summary>
Integer traits and functions

</summary>

- https://crates.io/crates/num-integer
- https://docs.rs/num-integer
- https://github.com/rust-num/num-integer

</details>

### num-traits

<details><summary>
Numeric traits for generic mathematics

</summary>

- https://crates.io/crates/num-traits
- https://docs.rs/num-traits
- https://github.com/rust-num/num-traits

</details>

### oorandom

<details><summary>
A tiny, robust PRNG implementation.

</summary>

- https://crates.io/crates/oorandom
- https://sr.ht/~icefox/oorandom/

</details>

### rand

<details><summary>
Random number generators and other randomness functionality.


</summary>

- https://crates.io/crates/rand
- https://docs.rs/rand
- https://github.com/rust-random/rand
- https://rust-random.github.io/book

</details><details><summary>
5 uses

</summary>

- [packages/modules/Bluetooth/tools/rootcanal/lmp](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/rootcanal/lmp)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [packages/modules/Virtualization/vm](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vm)
- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)
- [system/security/keystore2](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2)

</details>

### rand_chacha

<details><summary>
ChaCha random number generator


</summary>

- https://crates.io/crates/rand_chacha
- https://docs.rs/rand_chacha
- https://github.com/rust-random/rand
- https://rust-random.github.io/book

</details>

### rand_core

<details><summary>
Core random number generator traits and tools for implementation.


</summary>

- https://crates.io/crates/rand_core
- https://docs.rs/rand_core
- https://github.com/rust-random/rand
- https://rust-random.github.io/book

</details>

### rand_xorshift

<details><summary>
Xorshift random number generator


</summary>

- https://crates.io/crates/rand_xorshift
- https://docs.rs/rand_xorshift
- https://github.com/rust-random/rngs
- https://rust-random.github.io/book

</details>

## Asynchronous

### async-trait

<details><summary>
Type erasure for async trait methods

</summary>

- https://crates.io/crates/async-trait
- https://docs.rs/async-trait
- https://github.com/dtolnay/async-trait

</details>

### futures

<details><summary>
An implementation of futures and streams featuring zero allocations,
composability, and iterator-like interfaces.


</summary>

- https://crates.io/crates/futures
- https://github.com/rust-lang/futures-rs
- https://rust-lang.github.io/futures-rs

</details><details><summary>
7 uses

</summary>

- [packages/modules/Bluetooth/system/gd/rust/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/common)
- [packages/modules/Bluetooth/system/gd/rust/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/facade)
- [packages/modules/Bluetooth/system/gd/rust/shim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/shim)
- [packages/modules/Bluetooth/system/gd/rust/stack](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/stack)
- [packages/modules/Bluetooth/system/gd/rust/topshim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim)
- [packages/modules/Bluetooth/system/gd/rust/topshim/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/facade)
- [system/security/keystore2](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2)

</details>

### grpcio

<details><summary>
The rust language implementation of gRPC, base on the gRPC c core library.

</summary>

- https://crates.io/crates/grpcio
- https://docs.rs/grpcio
- https://github.com/tikv/grpc-rs

</details><details><summary>
5 uses

</summary>

- [packages/modules/Bluetooth/system/gd/rust/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/common)
- [packages/modules/Bluetooth/system/gd/rust/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/facade)
- [packages/modules/Bluetooth/system/gd/rust/stack](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/stack)
- [packages/modules/Bluetooth/system/gd/rust/topshim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim)
- [packages/modules/Bluetooth/system/gd/rust/topshim/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/facade)

</details>

### mio

<details><summary>
Lightweight non-blocking IO

</summary>

- https://crates.io/crates/mio
- https://github.com/tokio-rs/mio

</details>

### tokio

<details><summary>
An event-driven, non-blocking I/O platform for writing asynchronous I/O
backed applications.


</summary>

- https://crates.io/crates/tokio
- https://github.com/tokio-rs/tokio
- https://tokio.rs

</details><details><summary>
14 uses

</summary>

- [packages/modules/Bluetooth/system/gd/rust/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/common)
- [packages/modules/Bluetooth/system/gd/rust/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/facade)
- [packages/modules/Bluetooth/system/gd/rust/gddi](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/gddi)
- [packages/modules/Bluetooth/system/gd/rust/shim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/shim)
- [packages/modules/Bluetooth/system/gd/rust/stack](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/stack)
- [packages/modules/Bluetooth/system/gd/rust/topshim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim)
- [packages/modules/Bluetooth/system/gd/rust/topshim/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/facade)
- [packages/modules/Uwb/indev_uwb_adaptation](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Uwb/indev_uwb_adaptation)
- [packages/modules/Uwb/service/uci/jni](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Uwb/service/uci/jni)
- [system/nfc/src/rust](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust)
- [system/nfc/src/rust/rootcanal](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust/rootcanal)
- [system/nfc/src/rust/test](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust/test)
- [system/security/prng_seeder](https://cs.android.com/android/platform/superproject/+/master:system/security/prng_seeder)
- [system/tools/aidl](https://cs.android.com/android/platform/superproject/+/master:system/tools/aidl)

</details>

### tokio-macros

<details><summary>
Tokio's proc macros.


</summary>

- https://crates.io/crates/tokio-macros
- https://github.com/tokio-rs/tokio
- https://tokio.rs

</details>

### tokio-stream

<details><summary>
Utilities to work with `Stream` and `tokio`.


</summary>

- https://crates.io/crates/tokio-stream
- https://github.com/tokio-rs/tokio
- https://tokio.rs

</details>

### tokio-test

<details><summary>
Testing utilities for Tokio- and futures-based code


</summary>

- https://crates.io/crates/tokio-test
- https://docs.rs/tokio-test/0.4.2/tokio_test
- https://github.com/tokio-rs/tokio
- https://tokio.rs

</details>

## Command-line interface

### clap

<details><summary>
A simple to use, efficient, and full-featured Command Line Argument Parser

</summary>

- https://crates.io/crates/clap
- https://github.com/clap-rs/clap

</details><details><summary>
18 uses

</summary>

- [device/google/cuttlefish/host/commands/append_squashfs_overlay](https://cs.android.com/android/platform/superproject/+/master:device/google/cuttlefish/host/commands/append_squashfs_overlay)
- [packages/modules/Bluetooth/system/gd/rust/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/facade)
- [packages/modules/Bluetooth/system/gd/rust/topshim/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/facade)
- [packages/modules/Bluetooth/tools/pdl](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/pdl)
- [packages/modules/Virtualization/apkdmverity](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/apkdmverity)
- [packages/modules/Virtualization/authfs](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs)
- [packages/modules/Virtualization/authfs/fd_server](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/fd_server)
- [packages/modules/Virtualization/authfs/tests/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/tests/common)
- [packages/modules/Virtualization/avmd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/avmd)
- [packages/modules/Virtualization/compos/composd_cmd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/composd_cmd)
- [packages/modules/Virtualization/compos/verify](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/verify)
- [packages/modules/Virtualization/encryptedstore](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/encryptedstore)
- [packages/modules/Virtualization/microdroid/initrd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid/initrd)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)
- [packages/modules/Virtualization/vm](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vm)
- [packages/modules/Virtualization/zipfuse](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/zipfuse)
- [system/security/prng_seeder](https://cs.android.com/android/platform/superproject/+/master:system/security/prng_seeder)
- [system/tools/aidl/scripts/redundancy_check](https://cs.android.com/android/platform/superproject/+/master:system/tools/aidl/scripts/redundancy_check)

</details>

### clap_derive

<details><summary>
Parse command line argument by defining a struct, derive crate.

</summary>

- https://crates.io/crates/clap_derive
- https://github.com/clap-rs/clap/tree/master/clap_derive

</details>

### clap_lex

<details><summary>
Minimal, flexible command line parser

</summary>

- https://crates.io/crates/clap_lex
- https://github.com/clap-rs/clap/tree/master/clap_lex

</details>

### os_str_bytes

<details><summary>
Convert between byte sequences and platform-native strings


</summary>

- https://crates.io/crates/os_str_bytes
- https://github.com/dylni/os_str_bytes

</details>

### shlex

<details><summary>
Split a string into shell words, like Python's shlex.

</summary>

- https://crates.io/crates/shlex
- https://github.com/comex/rust-shlex

</details>

### structopt

<details><summary>
Parse command line argument by defining a struct.

</summary>

- https://crates.io/crates/structopt
- https://docs.rs/structopt
- https://github.com/TeXitoi/structopt

</details>

### structopt-derive

<details><summary>
Parse command line argument by defining a struct, derive crate.

</summary>

- https://crates.io/crates/structopt-derive
- https://docs.rs/structopt-derive
- https://github.com/TeXitoi/structopt

</details>

### textwrap

<details><summary>
Powerful library for word wrapping, indenting, and dedenting strings

</summary>

- https://crates.io/crates/textwrap
- https://docs.rs/textwrap/
- https://github.com/mgeisler/textwrap

</details>

## Compression

### flate2

<details><summary>
DEFLATE compression and decompression exposed as Read/BufRead/Write streams.
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip,
and raw deflate streams.


</summary>

- https://crates.io/crates/flate2
- https://docs.rs/flate2
- https://github.com/rust-lang/flate2-rs

</details>

### libz-sys

<details><summary>
Low-level bindings to the system libz library (also known as zlib).

</summary>

- https://crates.io/crates/libz-sys
- https://github.com/rust-lang/libz-sys

</details>

## Concurrency

### crossbeam-channel

<details><summary>
Multi-producer multi-consumer channels for message passing

</summary>

- https://crates.io/crates/crossbeam-channel
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-channel

</details>

### crossbeam-deque

<details><summary>
Concurrent work-stealing deque

</summary>

- https://crates.io/crates/crossbeam-deque
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-deque

</details>

### crossbeam-epoch

<details><summary>
Epoch-based garbage collection

</summary>

- https://crates.io/crates/crossbeam-epoch
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-epoch

</details>

### crossbeam-queue

<details><summary>
Concurrent queues

</summary>

- https://crates.io/crates/crossbeam-queue
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-queue

</details>

### crossbeam-utils

<details><summary>
Utilities for concurrent programming

</summary>

- https://crates.io/crates/crossbeam-utils
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-utils

</details>

### lock_api

<details><summary>
Wrappers to create fully-featured Mutex and RwLock types. Compatible with no_std.

</summary>

- https://crates.io/crates/lock_api
- https://github.com/Amanieu/parking_lot

</details>

### parking_lot

<details><summary>
More compact and efficient implementations of the standard synchronization primitives.

</summary>

- https://crates.io/crates/parking_lot
- https://github.com/Amanieu/parking_lot

</details>

### parking_lot_core

<details><summary>
An advanced API for creating custom synchronization primitives.

</summary>

- https://crates.io/crates/parking_lot_core
- https://github.com/Amanieu/parking_lot

</details>

### rayon

<details><summary>
Simple work-stealing parallelism for Rust

</summary>

- https://crates.io/crates/rayon
- https://docs.rs/rayon/
- https://github.com/rayon-rs/rayon

</details>

### rayon-core

<details><summary>
Core APIs for Rayon

</summary>

- https://crates.io/crates/rayon-core
- https://docs.rs/rayon/
- https://github.com/rayon-rs/rayon

</details>

## Cryptography

### const-oid

<details><summary>
Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard
as defined in ITU X.660, with support for BER/DER encoding/decoding as well as
heapless no_std (i.e. embedded) support


</summary>

- https://crates.io/crates/const-oid
- https://docs.rs/const-oid
- https://github.com/RustCrypto/formats/tree/master/const-oid

</details>

### coset

<details><summary>
Set of types for supporting COSE

</summary>

- https://crates.io/crates/coset
- https://github.com/google/coset

</details><details><summary>
3 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)
- [system/keymint/wire](https://cs.android.com/android/platform/superproject/+/master:system/keymint/wire)

</details>

### der

<details><summary>
Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules
(DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with
full support for heapless no_std targets


</summary>

- https://crates.io/crates/der
- https://github.com/RustCrypto/formats/tree/master/der

</details><details><summary>
2 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)

</details>

### der_derive

<details><summary>
Custom derive support for the `der` crate's `Choice` and `Sequence` traits

</summary>

- https://crates.io/crates/der_derive
- https://docs.rs/der
- https://github.com/RustCrypto/formats/tree/master/der/derive

</details>

### openssl

<details><summary>
OpenSSL bindings

</summary>

- https://crates.io/crates/openssl
- https://github.com/sfackler/rust-openssl

</details><details><summary>
6 uses

</summary>

- [packages/modules/Virtualization/authfs](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs)
- [packages/modules/Virtualization/authfs/src/fsverity/metadata](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/src/fsverity/metadata)
- [packages/modules/Virtualization/libs/apkverify](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/apkverify)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [system/keymint/boringssl](https://cs.android.com/android/platform/superproject/+/master:system/keymint/boringssl)
- [system/security/keystore2/tests](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests)

</details>

### pkcs1

<details><summary>
Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1:
RSA Cryptography Specifications Version 2.2 (RFC 8017)


</summary>

- https://crates.io/crates/pkcs1
- https://github.com/RustCrypto/formats/tree/master/pkcs1

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### pkcs8

<details><summary>
Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8:
Private-Key Information Syntax Specification (RFC 5208), with additional
support for PKCS#8v2 asymmetric key packages (RFC 5958)


</summary>

- https://crates.io/crates/pkcs8
- https://github.com/RustCrypto/formats/tree/master/pkcs8

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### ppv-lite86

<details><summary>
Implementation of the crypto-simd API for x86

</summary>

- https://crates.io/crates/ppv-lite86
- https://github.com/cryptocorrosion/cryptocorrosion

</details>

### ring

<details><summary>
Safe, fast, small crypto using Rust.

</summary>

- https://briansmith.org/rustdoc/ring/
- https://crates.io/crates/ring
- https://github.com/briansmith/ring

</details>

### sec1

<details><summary>
Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats
including ASN.1 DER-serialized private keys as well as the
Elliptic-Curve-Point-to-Octet-String encoding


</summary>

- https://crates.io/crates/sec1
- https://github.com/RustCrypto/formats/tree/master/sec1

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### spki

<details><summary>
X.509 Subject Public Key Info (RFC5280) describing public keys as well as their
associated AlgorithmIdentifiers (i.e. OIDs)


</summary>

- https://crates.io/crates/spki
- https://github.com/RustCrypto/formats/tree/master/spki

</details><details><summary>
2 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)

</details>

### webpki

<details><summary>
Web PKI X.509 Certificate Verification.

</summary>

- https://briansmith.org/rustdoc/webpki/
- https://crates.io/crates/webpki
- https://github.com/briansmith/webpki

</details>

### x509-cert

<details><summary>
Pure Rust implementation of the X.509 Public Key Infrastructure Certificate
format as described in RFC 5280


</summary>

- https://crates.io/crates/x509-cert
- https://github.com/RustCrypto/formats/tree/master/x509-cert

</details>

### x509-parser

<details><summary>
Parser for the X.509 v3 format (RFC 5280 certificates)

</summary>

- https://crates.io/crates/x509-parser
- https://github.com/rusticata/x509-parser
- https://github.com/rusticata/x509-parser.git

</details>

### zeroize

<details><summary>
Securely clear secrets from memory with a simple trait built on
stable Rust primitives which guarantee memory is zeroed using an
operation will not be 'optimized away' by the compiler.
Uses a portable pure Rust implementation that works everywhere,
even WASM!


</summary>

- https://crates.io/crates/zeroize
- https://github.com/RustCrypto/utils/tree/master/zeroize

</details><details><summary>
2 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/wire](https://cs.android.com/android/platform/superproject/+/master:system/keymint/wire)

</details>

### zeroize_derive

<details><summary>
Custom derive support for zeroize

</summary>

- https://crates.io/crates/zeroize_derive
- https://github.com/RustCrypto/utils/tree/master/zeroize/derive

</details>

## Data structures

### ahash

<details><summary>
A non-cryptographic hash function using AES-NI for high performance

</summary>

- https://crates.io/crates/ahash
- https://docs.rs/ahash
- https://github.com/tkaitchuck/ahash

</details>

### bytes

<details><summary>
Types and traits for working with bytes

</summary>

- https://crates.io/crates/bytes
- https://github.com/tokio-rs/bytes

</details>

### ciborium

<details><summary>
serde implementation of CBOR using ciborium-basic

</summary>

- https://crates.io/crates/ciborium
- https://github.com/enarx/ciborium

</details><details><summary>
6 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/derive](https://cs.android.com/android/platform/superproject/+/master:system/keymint/derive)
- [system/keymint/hal](https://cs.android.com/android/platform/superproject/+/master:system/keymint/hal)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)
- [system/keymint/tests](https://cs.android.com/android/platform/superproject/+/master:system/keymint/tests)
- [system/keymint/wire](https://cs.android.com/android/platform/superproject/+/master:system/keymint/wire)

</details>

### ciborium-io

<details><summary>
Simplified Read/Write traits for no_std usage

</summary>

- https://crates.io/crates/ciborium-io/0.2.0
- https://github.com/enarx/ciborium

</details>

### ciborium-ll

<details><summary>
Low-level CBOR codec primitives

</summary>

- https://crates.io/crates/ciborium-ll/0.2.0
- https://github.com/enarx/ciborium

</details>

### const-oid

<details><summary>
Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard
as defined in ITU X.660, with support for BER/DER encoding/decoding as well as
heapless no_std (i.e. embedded) support


</summary>

- https://crates.io/crates/const-oid
- https://docs.rs/const-oid
- https://github.com/RustCrypto/formats/tree/master/const-oid

</details>

### crossbeam-channel

<details><summary>
Multi-producer multi-consumer channels for message passing

</summary>

- https://crates.io/crates/crossbeam-channel
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-channel

</details>

### crossbeam-deque

<details><summary>
Concurrent work-stealing deque

</summary>

- https://crates.io/crates/crossbeam-deque
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-deque

</details>

### crossbeam-queue

<details><summary>
Concurrent queues

</summary>

- https://crates.io/crates/crossbeam-queue
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-queue

</details>

### crossbeam-utils

<details><summary>
Utilities for concurrent programming

</summary>

- https://crates.io/crates/crossbeam-utils
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-utils

</details>

### der

<details><summary>
Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules
(DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with
full support for heapless no_std targets


</summary>

- https://crates.io/crates/der
- https://github.com/RustCrypto/formats/tree/master/der

</details><details><summary>
2 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)

</details>

### der_derive

<details><summary>
Custom derive support for the `der` crate's `Choice` and `Sequence` traits

</summary>

- https://crates.io/crates/der_derive
- https://docs.rs/der
- https://github.com/RustCrypto/formats/tree/master/der/derive

</details>

### either

<details><summary>
The enum `Either` with variants `Left` and `Right` is a general purpose sum type with two cases.


</summary>

- https://crates.io/crates/either
- https://docs.rs/either/1/
- https://github.com/bluss/either

</details>

### half

<details><summary>
Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types.

</summary>

- https://crates.io/crates/half
- https://github.com/starkat99/half-rs

</details>

### hashbrown

<details><summary>
A Rust port of Google's SwissTable hash map

</summary>

- https://crates.io/crates/hashbrown
- https://github.com/rust-lang/hashbrown

</details>

### indexmap

<details><summary>
A hash table with consistent order and fast iteration.

</summary>

- https://crates.io/crates/indexmap/1.9.1
- https://docs.rs/indexmap/
- https://github.com/bluss/indexmap

</details>

### intrusive-collections

<details><summary>
Intrusive collections for Rust (linked list and red-black tree)

</summary>

- https://crates.io/crates/intrusive-collections
- https://docs.rs/intrusive-collections
- https://github.com/Amanieu/intrusive-rs

</details>

### macaddr

<details><summary>
MAC address types

</summary>

- https://crates.io/crates/macaddr
- https://github.com/svartalf/rust-macaddr

</details><details><summary>
1 uses

</summary>

- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)

</details>

### num-bigint

<details><summary>
Big integer implementation for Rust

</summary>

- https://crates.io/crates/num-bigint
- https://docs.rs/num-bigint
- https://github.com/rust-num/num-bigint

</details>

### pkcs1

<details><summary>
Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1:
RSA Cryptography Specifications Version 2.2 (RFC 8017)


</summary>

- https://crates.io/crates/pkcs1
- https://github.com/RustCrypto/formats/tree/master/pkcs1

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### pkcs8

<details><summary>
Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8:
Private-Key Information Syntax Specification (RFC 5208), with additional
support for PKCS#8v2 asymmetric key packages (RFC 5958)


</summary>

- https://crates.io/crates/pkcs8
- https://github.com/RustCrypto/formats/tree/master/pkcs8

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### sec1

<details><summary>
Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats
including ASN.1 DER-serialized private keys as well as the
Elliptic-Curve-Point-to-Octet-String encoding


</summary>

- https://crates.io/crates/sec1
- https://github.com/RustCrypto/formats/tree/master/sec1

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### semver

<details><summary>
Parser and evaluator for Cargo's flavor of Semantic Versioning

</summary>

- https://crates.io/crates/semver
- https://docs.rs/semver
- https://github.com/dtolnay/semver

</details><details><summary>
2 uses

</summary>

- [packages/modules/Virtualization/libs/vmconfig](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/vmconfig)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)

</details>

### slab

<details><summary>
Pre-allocated storage for a uniform data type

</summary>

- https://crates.io/crates/slab
- https://github.com/tokio-rs/slab

</details>

### smallvec

<details><summary>
'Small vector' optimization: store up to a small number of items on the stack

</summary>

- https://crates.io/crates/smallvec
- https://docs.rs/smallvec/
- https://github.com/servo/rust-smallvec

</details>

### spki

<details><summary>
X.509 Subject Public Key Info (RFC5280) describing public keys as well as their
associated AlgorithmIdentifiers (i.e. OIDs)


</summary>

- https://crates.io/crates/spki
- https://github.com/RustCrypto/formats/tree/master/spki

</details><details><summary>
2 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)

</details>

### tinyvec

<details><summary>
`tinyvec` provides 100% safe vec-like data structures.

</summary>

- https://crates.io/crates/tinyvec
- https://github.com/Lokathor/tinyvec

</details>

### uuid

<details><summary>
A library to generate and parse UUIDs.

</summary>

- https://crates.io/crates/uuid
- https://docs.rs/uuid
- https://github.com/uuid-rs/uuid

</details><details><summary>
4 uses

</summary>

- [packages/modules/Virtualization/apkdmverity](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/apkdmverity)
- [packages/modules/Virtualization/libs/devicemapper](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/devicemapper)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)

</details>

### x509-cert

<details><summary>
Pure Rust implementation of the X.509 Public Key Infrastructure Certificate
format as described in RFC 5280


</summary>

- https://crates.io/crates/x509-cert
- https://github.com/RustCrypto/formats/tree/master/x509-cert

</details>

## Database interfaces

### rusqlite

<details><summary>
Ergonomic wrapper for SQLite

</summary>

- http://docs.rs/rusqlite/
- https://crates.io/crates/rusqlite
- https://github.com/rusqlite/rusqlite

</details><details><summary>
2 uses

</summary>

- [system/security/keystore2](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2)
- [system/security/keystore2/legacykeystore](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/legacykeystore)

</details>

## Date and time

### chrono

<details><summary>
Date and time library for Rust

</summary>

- https://crates.io/crates/chrono
- https://docs.rs/chrono/
- https://github.com/chronotope/chrono

</details><details><summary>
1 uses

</summary>

- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)

</details>

## Development tools

### document-features

<details><summary>
Extract documentation for the feature flags from comments in Cargo.toml

</summary>

- https://crates.io/crates/document-features
- https://github.com/slint-ui/document-features
- https://slint-ui.com

</details>

### paste

<details><summary>
Macros for all your token pasting needs

</summary>

- https://crates.io/crates/paste
- https://github.com/dtolnay/paste

</details>

### remain

<details><summary>
Compile-time checks that an enum, struct, or match is written in sorted order.

</summary>

- https://crates.io/crates/remain
- https://docs.rs/remain
- https://github.com/dtolnay/remain

</details>

## Development tools::Build Utils

### litrs

<details><summary>
Parse and inspect Rust literals (i.e. tokens in the Rust programming language
representing fixed values). Particularly useful for proc macros, but can also
be used outside of a proc-macro context.


</summary>

- https://crates.io/crates/litrs
- https://docs.rs/litrs/
- https://github.com/LukasKalbertodt/litrs/

</details>

### rustversion

<details><summary>
Conditional compilation according to rustc compiler version

</summary>

- https://crates.io/crates/rustversion
- https://docs.rs/rustversion
- https://github.com/dtolnay/rustversion

</details>

## Development tools::Debugging

### env_logger

<details><summary>
A logging implementation for `log` which is configured via an environment
variable.


</summary>

- https://crates.io/crates/env_logger
- https://github.com/rust-cli/env_logger/

</details><details><summary>
5 uses

</summary>

- [device/google/cuttlefish/host/commands/secure_env/rust](https://cs.android.com/android/platform/superproject/+/master:device/google/cuttlefish/host/commands/secure_env/rust)
- [packages/modules/Bluetooth/system/gd/rust/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/common)
- [packages/modules/Virtualization/vm](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vm)
- [system/keymint/tests](https://cs.android.com/android/platform/superproject/+/master:system/keymint/tests)
- [system/logging/rust](https://cs.android.com/android/platform/superproject/+/master:system/logging/rust)

</details>

### gdbstub

<details><summary>
An implementation of the GDB Remote Serial Protocol in Rust

</summary>

- https://crates.io/crates/gdbstub
- https://docs.rs/gdbstub
- https://github.com/daniel5151/gdbstub

</details>

### gdbstub_arch

<details><summary>
Implementations of `gdbstub::arch::Arch` for various architectures.

</summary>

- https://crates.io/crates/gdbstub_arch
- https://docs.rs/gdbstub_arch
- https://github.com/daniel5151/gdbstub

</details>

### log

<details><summary>
A lightweight logging facade for Rust


</summary>

- https://crates.io/crates/log
- https://docs.rs/log
- https://github.com/rust-lang/log

</details>

## Development tools::FFI

### bindgen

<details><summary>
Automatically generates Rust FFI bindings to C and C++ libraries.

</summary>

- https://crates.io/crates/bindgen
- https://docs.rs/bindgen
- https://github.com/rust-lang/rust-bindgen
- https://rust-lang.github.io/rust-bindgen/

</details>

### bindgen-cli

<details><summary>
Automatically generates Rust FFI bindings to C and C++ libraries.

</summary>

- https://crates.io/crates/bindgen-cli
- https://docs.rs/bindgen
- https://github.com/rust-lang/rust-bindgen
- https://rust-lang.github.io/rust-bindgen/

</details>

### os_str_bytes

<details><summary>
Convert between byte sequences and platform-native strings


</summary>

- https://crates.io/crates/os_str_bytes
- https://github.com/dylni/os_str_bytes

</details>

## Development tools::Procedural macro helpers

### clap_derive

<details><summary>
Parse command line argument by defining a struct, derive crate.

</summary>

- https://crates.io/crates/clap_derive
- https://github.com/clap-rs/clap/tree/master/clap_derive

</details>

### litrs

<details><summary>
Parse and inspect Rust literals (i.e. tokens in the Rust programming language
representing fixed values). Particularly useful for proc macros, but can also
be used outside of a proc-macro context.


</summary>

- https://crates.io/crates/litrs
- https://docs.rs/litrs/
- https://github.com/LukasKalbertodt/litrs/

</details>

### proc-macro-error

<details><summary>
Almost drop-in replacement to panics in proc-macros

</summary>

- https://crates.io/crates/proc-macro-error
- https://gitlab.com/CreepySkeleton/proc-macro-error

</details>

### proc-macro-hack

<details><summary>
Procedural macros in expression position

</summary>

- https://crates.io/crates/proc-macro-hack
- https://github.com/dtolnay/proc-macro-hack

</details>

### proc-macro2

<details><summary>
A substitute implementation of the compiler's `proc_macro` API to decouple token-based libraries from the procedural macro use case.

</summary>

- https://crates.io/crates/proc-macro2
- https://docs.rs/proc-macro2
- https://github.com/dtolnay/proc-macro2

</details>

### quote

<details><summary>
Quasi-quoting macro quote!(...)

</summary>

- https://crates.io/crates/quote
- https://docs.rs/quote/
- https://github.com/dtolnay/quote

</details><details><summary>
4 uses

</summary>

- [packages/modules/Bluetooth/system/gd/rust/gddi](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/gddi)
- [packages/modules/Bluetooth/system/gd/rust/topshim/macros](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/macros)
- [packages/modules/Bluetooth/tools/pdl](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/pdl)
- [system/keymint/derive](https://cs.android.com/android/platform/superproject/+/master:system/keymint/derive)

</details>

### syn

<details><summary>
Parser for Rust source code

</summary>

- https://crates.io/crates/syn
- https://docs.rs/syn
- https://github.com/dtolnay/syn

</details><details><summary>
4 uses

</summary>

- [packages/modules/Bluetooth/system/gd/rust/gddi](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/gddi)
- [packages/modules/Bluetooth/system/gd/rust/topshim/macros](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/macros)
- [packages/modules/Bluetooth/tools/pdl](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/pdl)
- [system/keymint/derive](https://cs.android.com/android/platform/superproject/+/master:system/keymint/derive)

</details>

### syn-mid

<details><summary>
Providing the features between "full" and "derive" of syn.


</summary>

- https://crates.io/crates/syn-mid
- https://docs.rs/syn-mid
- https://github.com/taiki-e/syn-mid

</details>

### unicode-ident

<details><summary>
Determine whether characters have the XID_Start or XID_Continue properties according to Unicode Standard Annex #31

</summary>

- https://crates.io/crates/unicode-ident
- https://docs.rs/unicode-ident
- https://github.com/dtolnay/unicode-ident

</details>

## Development tools::Profiling

### bencher

<details><summary>
A port of the libtest (unstable Rust) benchmark runner to Rust stable releases. Supports running benchmarks and filtering based on the name. Benchmark execution works exactly the same way and no more (caveat: black_box is still missing!).

</summary>

- https://crates.io/crates/bencher
- https://docs.rs/bencher/
- https://github.com/bluss/bencher/

</details>

### criterion

<details><summary>
Statistics-driven micro-benchmarking library

</summary>

- https://bheisler.github.io/criterion.rs/book/index.html
- https://crates.io/crates/criterion
- https://github.com/bheisler/criterion.rs

</details>

## Development tools::Testing

### arbitrary

<details><summary>
The trait for generating structured data from unstructured data

</summary>

- https://crates.io/crates/arbitrary
- https://docs.rs/arbitrary/
- https://github.com/rust-fuzz/arbitrary/

</details><details><summary>
2 uses

</summary>

- [system/librustutils](https://cs.android.com/android/platform/superproject/+/master:system/librustutils)
- [system/security/keystore2/src/fuzzers](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/src/fuzzers)

</details>

### derive_arbitrary

<details><summary>
Derives arbitrary traits

</summary>

- https://crates.io/crates/derive_arbitrary
- https://docs.rs/arbitrary/
- https://github.com/rust-fuzz/arbitrary

</details>

### quickcheck

<details><summary>
Automatic property based testing with shrinking.

</summary>

- https://crates.io/crates/quickcheck
- https://docs.rs/quickcheck
- https://github.com/BurntSushi/quickcheck

</details>

### serde_test

<details><summary>
Token De/Serializer for testing De/Serialize implementations

</summary>

- https://crates.io/crates/serde_test
- https://docs.rs/serde_test
- https://github.com/serde-rs/serde
- https://serde.rs

</details>

### static_assertions

<details><summary>
Compile-time assertions to ensure that invariants are met.

</summary>

- https://crates.io/crates/static_assertions
- https://docs.rs/static_assertions/
- https://github.com/nvzqz/static-assertions-rs

</details>

## Embedded development

### aarch64-paging

<details><summary>
A library to manipulate AArch64 VMSA EL1 page tables.

</summary>

- https://crates.io/crates/aarch64-paging
- https://github.com/google/aarch64-paging

</details>

### ciborium

<details><summary>
serde implementation of CBOR using ciborium-basic

</summary>

- https://crates.io/crates/ciborium
- https://github.com/enarx/ciborium

</details><details><summary>
6 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/derive](https://cs.android.com/android/platform/superproject/+/master:system/keymint/derive)
- [system/keymint/hal](https://cs.android.com/android/platform/superproject/+/master:system/keymint/hal)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)
- [system/keymint/tests](https://cs.android.com/android/platform/superproject/+/master:system/keymint/tests)
- [system/keymint/wire](https://cs.android.com/android/platform/superproject/+/master:system/keymint/wire)

</details>

### ciborium-io

<details><summary>
Simplified Read/Write traits for no_std usage

</summary>

- https://crates.io/crates/ciborium-io/0.2.0
- https://github.com/enarx/ciborium

</details>

### ciborium-ll

<details><summary>
Low-level CBOR codec primitives

</summary>

- https://crates.io/crates/ciborium-ll/0.2.0
- https://github.com/enarx/ciborium

</details>

### gdbstub

<details><summary>
An implementation of the GDB Remote Serial Protocol in Rust

</summary>

- https://crates.io/crates/gdbstub
- https://docs.rs/gdbstub
- https://github.com/daniel5151/gdbstub

</details>

### gdbstub_arch

<details><summary>
Implementations of `gdbstub::arch::Arch` for various architectures.

</summary>

- https://crates.io/crates/gdbstub_arch
- https://docs.rs/gdbstub_arch
- https://github.com/daniel5151/gdbstub

</details>

### managed

<details><summary>
An interface for logically owning objects, whether or not heap allocation is available.

</summary>

- https://crates.io/crates/managed
- https://docs.rs/managed/
- https://github.com/m-labs/rust-managed
- https://github.com/m-labs/rust-managed.git

</details>

### oorandom

<details><summary>
A tiny, robust PRNG implementation.

</summary>

- https://crates.io/crates/oorandom
- https://sr.ht/~icefox/oorandom/

</details>

### psci

<details><summary>
Functions and constants for the Arm Power State Coordination Interface (PSCI) 1.1 on aarch64.

</summary>

- https://crates.io/crates/psci
- https://github.com/google/psci

</details><details><summary>
1 uses

</summary>

- [packages/modules/Virtualization/vmbase](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vmbase)

</details>

## Emulators

### gdbstub

<details><summary>
An implementation of the GDB Remote Serial Protocol in Rust

</summary>

- https://crates.io/crates/gdbstub
- https://docs.rs/gdbstub
- https://github.com/daniel5151/gdbstub

</details>

### gdbstub_arch

<details><summary>
Implementations of `gdbstub::arch::Arch` for various architectures.

</summary>

- https://crates.io/crates/gdbstub_arch
- https://docs.rs/gdbstub_arch
- https://github.com/daniel5151/gdbstub

</details>

## Encoding

### base64

<details><summary>
encodes and decodes base64 as bytes or utf8

</summary>

- https://crates.io/crates/base64
- https://docs.rs/base64
- https://github.com/marshallpierce/rust-base64

</details>

### bstr

<details><summary>
A string type that is not required to be valid UTF-8.

</summary>

- https://crates.io/crates/bstr
- https://docs.rs/bstr
- https://github.com/BurntSushi/bstr

</details>

### byteorder

<details><summary>
Library for reading/writing numbers in big-endian and little-endian.

</summary>

- https://crates.io/crates/byteorder
- https://docs.rs/byteorder
- https://github.com/BurntSushi/byteorder

</details>

### ciborium

<details><summary>
serde implementation of CBOR using ciborium-basic

</summary>

- https://crates.io/crates/ciborium
- https://github.com/enarx/ciborium

</details><details><summary>
6 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/derive](https://cs.android.com/android/platform/superproject/+/master:system/keymint/derive)
- [system/keymint/hal](https://cs.android.com/android/platform/superproject/+/master:system/keymint/hal)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)
- [system/keymint/tests](https://cs.android.com/android/platform/superproject/+/master:system/keymint/tests)
- [system/keymint/wire](https://cs.android.com/android/platform/superproject/+/master:system/keymint/wire)

</details>

### ciborium-ll

<details><summary>
Low-level CBOR codec primitives

</summary>

- https://crates.io/crates/ciborium-ll/0.2.0
- https://github.com/enarx/ciborium

</details>

### const-oid

<details><summary>
Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard
as defined in ITU X.660, with support for BER/DER encoding/decoding as well as
heapless no_std (i.e. embedded) support


</summary>

- https://crates.io/crates/const-oid
- https://docs.rs/const-oid
- https://github.com/RustCrypto/formats/tree/master/const-oid

</details>

### csv

<details><summary>
Fast CSV parsing with support for serde.

</summary>

- http://burntsushi.net/rustdoc/csv/
- https://crates.io/crates/csv
- https://github.com/BurntSushi/rust-csv

</details>

### csv-core

<details><summary>
Bare bones CSV parsing with no_std support.

</summary>

- https://crates.io/crates/csv-core
- https://docs.rs/csv-core
- https://github.com/BurntSushi/rust-csv

</details>

### der

<details><summary>
Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules
(DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with
full support for heapless no_std targets


</summary>

- https://crates.io/crates/der
- https://github.com/RustCrypto/formats/tree/master/der

</details><details><summary>
2 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)

</details>

### der_derive

<details><summary>
Custom derive support for the `der` crate's `Choice` and `Sequence` traits

</summary>

- https://crates.io/crates/der_derive
- https://docs.rs/der
- https://github.com/RustCrypto/formats/tree/master/der/derive

</details>

### half

<details><summary>
Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types.

</summary>

- https://crates.io/crates/half
- https://github.com/starkat99/half-rs

</details>

### hex

<details><summary>
Encoding and decoding data into/from hexadecimal representation.

</summary>

- https://crates.io/crates/hex
- https://docs.rs/hex/
- https://github.com/KokaKiwi/rust-hex

</details><details><summary>
13 uses

</summary>

- [device/google/cuttlefish/guest/hals/keymint/rust](https://cs.android.com/android/platform/superproject/+/master:device/google/cuttlefish/guest/hals/keymint/rust)
- [device/google/cuttlefish/host/commands/secure_env/rust](https://cs.android.com/android/platform/superproject/+/master:device/google/cuttlefish/host/commands/secure_env/rust)
- [packages/modules/Virtualization/avmd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/avmd)
- [packages/modules/Virtualization/encryptedstore](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/encryptedstore)
- [packages/modules/Virtualization/libs/apexutil](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/apexutil)
- [packages/modules/Virtualization/libs/apkverify](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/apkverify)
- [packages/modules/Virtualization/libs/devicemapper](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/devicemapper)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/hal](https://cs.android.com/android/platform/superproject/+/master:system/keymint/hal)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)
- [system/keymint/tests](https://cs.android.com/android/platform/superproject/+/master:system/keymint/tests)
- [system/keymint/wire](https://cs.android.com/android/platform/superproject/+/master:system/keymint/wire)

</details>

### os_str_bytes

<details><summary>
Convert between byte sequences and platform-native strings


</summary>

- https://crates.io/crates/os_str_bytes
- https://github.com/dylni/os_str_bytes

</details>

### pkcs1

<details><summary>
Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1:
RSA Cryptography Specifications Version 2.2 (RFC 8017)


</summary>

- https://crates.io/crates/pkcs1
- https://github.com/RustCrypto/formats/tree/master/pkcs1

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### pkcs8

<details><summary>
Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8:
Private-Key Information Syntax Specification (RFC 5208), with additional
support for PKCS#8v2 asymmetric key packages (RFC 5958)


</summary>

- https://crates.io/crates/pkcs8
- https://github.com/RustCrypto/formats/tree/master/pkcs8

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### sec1

<details><summary>
Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats
including ASN.1 DER-serialized private keys as well as the
Elliptic-Curve-Point-to-Octet-String encoding


</summary>

- https://crates.io/crates/sec1
- https://github.com/RustCrypto/formats/tree/master/sec1

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### serde

<details><summary>
A generic serialization/deserialization framework

</summary>

- https://crates.io/crates/serde
- https://docs.rs/serde
- https://github.com/serde-rs/serde
- https://serde.rs

</details><details><summary>
15 uses

</summary>

- [hardware/interfaces/security/dice/aidl/default](https://cs.android.com/android/platform/superproject/+/master:hardware/interfaces/security/dice/aidl/default)
- [packages/modules/Bluetooth/tools/pdl](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/pdl)
- [packages/modules/Virtualization/avmd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/avmd)
- [packages/modules/Virtualization/libs/apkverify](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/apkverify)
- [packages/modules/Virtualization/libs/vmconfig](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/vmconfig)
- [packages/modules/Virtualization/microdroid/payload/config](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid/payload/config)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)
- [packages/modules/Virtualization/vm](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vm)
- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)
- [system/security/diced](https://cs.android.com/android/platform/superproject/+/master:system/security/diced)
- [system/security/keystore2](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2)
- [system/security/keystore2/tests](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests)
- [system/security/keystore2/tests/legacy_blobs](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests/legacy_blobs)
- [system/tools/aidl/scripts/redundancy_check](https://cs.android.com/android/platform/superproject/+/master:system/tools/aidl/scripts/redundancy_check)

</details>

### serde_cbor

<details><summary>
CBOR support for serde.

</summary>

- https://crates.io/crates/serde_cbor
- https://github.com/pyfisch/cbor

</details><details><summary>
4 uses

</summary>

- [packages/modules/Virtualization/avmd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/avmd)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [system/security/diced](https://cs.android.com/android/platform/superproject/+/master:system/security/diced)
- [system/security/keystore2](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2)

</details>

### serde_json

<details><summary>
A JSON serialization file format

</summary>

- https://crates.io/crates/serde_json
- https://docs.serde.rs/serde_json/
- https://github.com/serde-rs/json

</details><details><summary>
8 uses

</summary>

- [packages/modules/Bluetooth/tools/pdl](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/pdl)
- [packages/modules/Virtualization/libs/vmconfig](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/vmconfig)
- [packages/modules/Virtualization/microdroid/payload/config](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid/payload/config)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)
- [packages/modules/Virtualization/vm](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vm)
- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)
- [system/tools/aidl/scripts/redundancy_check](https://cs.android.com/android/platform/superproject/+/master:system/tools/aidl/scripts/redundancy_check)

</details>

### spki

<details><summary>
X.509 Subject Public Key Info (RFC5280) describing public keys as well as their
associated AlgorithmIdentifiers (i.e. OIDs)


</summary>

- https://crates.io/crates/spki
- https://github.com/RustCrypto/formats/tree/master/spki

</details><details><summary>
2 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)

</details>

### unicode-bidi

<details><summary>
Implementation of the Unicode Bidirectional Algorithm

</summary>

- https://crates.io/crates/unicode-bidi
- https://docs.rs/unicode-bidi/
- https://github.com/servo/unicode-bidi

</details>

### url

<details><summary>
URL library for Rust, based on the WHATWG URL Standard

</summary>

- https://crates.io/crates/url
- https://docs.rs/url
- https://github.com/servo/rust-url

</details>

### x509-cert

<details><summary>
Pure Rust implementation of the X.509 Public Key Infrastructure Certificate
format as described in RFC 5280


</summary>

- https://crates.io/crates/x509-cert
- https://github.com/RustCrypto/formats/tree/master/x509-cert

</details>

## External FFI bindings

### android_log-sys

<details><summary>
FFI bindings to Android log Library.


</summary>

- https://crates.io/crates/android_log-sys
- https://docs.rs/android_log-sys
- https://github.com/nercury/android_log-sys-rs

</details>

### bindgen

<details><summary>
Automatically generates Rust FFI bindings to C and C++ libraries.

</summary>

- https://crates.io/crates/bindgen
- https://docs.rs/bindgen
- https://github.com/rust-lang/rust-bindgen
- https://rust-lang.github.io/rust-bindgen/

</details>

### bindgen-cli

<details><summary>
Automatically generates Rust FFI bindings to C and C++ libraries.

</summary>

- https://crates.io/crates/bindgen-cli
- https://docs.rs/bindgen
- https://github.com/rust-lang/rust-bindgen
- https://rust-lang.github.io/rust-bindgen/

</details>

### grpcio-sys

<details><summary>
FFI bindings to gRPC c core library

</summary>

- https://crates.io/crates/grpcio-sys
- https://docs.rs/grpcio-sys
- https://github.com/tikv/grpc-rs

</details>

### jni-sys

<details><summary>
Rust definitions corresponding to jni.h

</summary>

- https://crates.io/crates/jni-sys
- https://docs.rs/jni-sys/0.3.0/jni_sys
- https://github.com/sfackler/rust-jni-sys

</details>

### libc

<details><summary>
Raw FFI bindings to platform libraries like libc.


</summary>

- https://crates.io/crates/libc
- https://docs.rs/libc/
- https://github.com/rust-lang/libc

</details>

### libsqlite3-sys

<details><summary>
Native bindings to the libsqlite3 library

</summary>

- https://crates.io/crates/libsqlite3-sys
- https://github.com/rusqlite/rusqlite

</details>

### libz-sys

<details><summary>
Low-level bindings to the system libz library (also known as zlib).

</summary>

- https://crates.io/crates/libz-sys
- https://github.com/rust-lang/libz-sys

</details>

## Filesystem

### glob

<details><summary>
Support for matching file paths against Unix shell style patterns.


</summary>

- https://crates.io/crates/glob
- https://docs.rs/glob/0.3.1
- https://github.com/rust-lang/glob

</details><details><summary>
1 uses

</summary>

- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)

</details>

### remove_dir_all

<details><summary>
A safe, reliable implementation of remove_dir_all for Windows

</summary>

- https://crates.io/crates/remove_dir_all
- https://github.com/XAMPPRocky/remove_dir_all.git

</details>

### walkdir

<details><summary>
Recursively walk a directory.

</summary>

- https://crates.io/crates/walkdir
- https://docs.rs/walkdir/
- https://github.com/BurntSushi/walkdir

</details>

### which

<details><summary>
A Rust equivalent of Unix command "which". Locate installed executable in cross platforms.

</summary>

- https://crates.io/crates/which
- https://docs.rs/which/
- https://github.com/harryfei/which-rs.git

</details>

## Game engines

### glam

<details><summary>
A simple and fast 3D math library for games and graphics

</summary>

- https://crates.io/crates/glam
- https://github.com/bitshifter/glam-rs

</details>

## Hardware support

### aarch64-paging

<details><summary>
A library to manipulate AArch64 VMSA EL1 page tables.

</summary>

- https://crates.io/crates/aarch64-paging
- https://github.com/google/aarch64-paging

</details>

### num_cpus

<details><summary>
Get the number of CPUs on a machine.

</summary>

- https://crates.io/crates/num_cpus
- https://docs.rs/num_cpus
- https://github.com/seanmonstar/num_cpus

</details><details><summary>
2 uses

</summary>

- [packages/modules/Virtualization/compos/composd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/composd)
- [system/security/keystore2/selinux](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/selinux)

</details>

### psci

<details><summary>
Functions and constants for the Arm Power State Coordination Interface (PSCI) 1.1 on aarch64.

</summary>

- https://crates.io/crates/psci
- https://github.com/google/psci

</details><details><summary>
1 uses

</summary>

- [packages/modules/Virtualization/vmbase](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vmbase)

</details>

### virtio-drivers

<details><summary>
VirtIO guest drivers.

</summary>

- https://crates.io/crates/virtio-drivers
- https://github.com/rcore-os/virtio-drivers

</details>

## Memory management

### crossbeam-epoch

<details><summary>
Epoch-based garbage collection

</summary>

- https://crates.io/crates/crossbeam-epoch
- https://github.com/crossbeam-rs/crossbeam
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-epoch

</details>

### lazy_static

<details><summary>
A macro for declaring lazily evaluated statics in Rust.

</summary>

- https://crates.io/crates/lazy_static
- https://docs.rs/lazy_static
- https://github.com/rust-lang-nursery/lazy-static.rs

</details>

### once_cell

<details><summary>
Single assignment cells and lazy values.

</summary>

- https://crates.io/crates/once_cell
- https://docs.rs/once_cell
- https://github.com/matklad/once_cell

</details><details><summary>
2 uses

</summary>

- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)

</details>

### slab

<details><summary>
Pre-allocated storage for a uniform data type

</summary>

- https://crates.io/crates/slab
- https://github.com/tokio-rs/slab

</details>

### zeroize

<details><summary>
Securely clear secrets from memory with a simple trait built on
stable Rust primitives which guarantee memory is zeroed using an
operation will not be 'optimized away' by the compiler.
Uses a portable pure Rust implementation that works everywhere,
even WASM!


</summary>

- https://crates.io/crates/zeroize
- https://github.com/RustCrypto/utils/tree/master/zeroize

</details><details><summary>
2 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/wire](https://cs.android.com/android/platform/superproject/+/master:system/keymint/wire)

</details>

### zeroize_derive

<details><summary>
Custom derive support for zeroize

</summary>

- https://crates.io/crates/zeroize_derive
- https://github.com/RustCrypto/utils/tree/master/zeroize/derive

</details>

## Network programming

### bytes

<details><summary>
Types and traits for working with bytes

</summary>

- https://crates.io/crates/bytes
- https://github.com/tokio-rs/bytes

</details>

### gdbstub

<details><summary>
An implementation of the GDB Remote Serial Protocol in Rust

</summary>

- https://crates.io/crates/gdbstub
- https://docs.rs/gdbstub
- https://github.com/daniel5151/gdbstub

</details>

### grpcio

<details><summary>
The rust language implementation of gRPC, base on the gRPC c core library.

</summary>

- https://crates.io/crates/grpcio
- https://docs.rs/grpcio
- https://github.com/tikv/grpc-rs

</details><details><summary>
5 uses

</summary>

- [packages/modules/Bluetooth/system/gd/rust/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/common)
- [packages/modules/Bluetooth/system/gd/rust/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/facade)
- [packages/modules/Bluetooth/system/gd/rust/stack](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/stack)
- [packages/modules/Bluetooth/system/gd/rust/topshim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim)
- [packages/modules/Bluetooth/system/gd/rust/topshim/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/facade)

</details>

### grpcio-compiler

<details><summary>
gRPC compiler for grpcio

</summary>

- https://crates.io/crates/grpcio-compiler
- https://docs.rs/grpcio-compiler
- https://github.com/tikv/grpc-rs

</details>

### grpcio-sys

<details><summary>
FFI bindings to gRPC c core library

</summary>

- https://crates.io/crates/grpcio-sys
- https://docs.rs/grpcio-sys
- https://github.com/tikv/grpc-rs

</details>

### macaddr

<details><summary>
MAC address types

</summary>

- https://crates.io/crates/macaddr
- https://github.com/svartalf/rust-macaddr

</details><details><summary>
1 uses

</summary>

- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)

</details>

### octets

<details><summary>
Zero-copy abstraction for parsing and constructing network packets

</summary>

- https://crates.io/crates/octets
- https://github.com/cloudflare/quiche

</details>

### quiche

<details><summary>
🥧 Savoury implementation of the QUIC transport protocol and HTTP/3

</summary>

- https://crates.io/crates/quiche
- https://github.com/cloudflare/quiche

</details>

### tokio

<details><summary>
An event-driven, non-blocking I/O platform for writing asynchronous I/O
backed applications.


</summary>

- https://crates.io/crates/tokio
- https://github.com/tokio-rs/tokio
- https://tokio.rs

</details><details><summary>
14 uses

</summary>

- [packages/modules/Bluetooth/system/gd/rust/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/common)
- [packages/modules/Bluetooth/system/gd/rust/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/facade)
- [packages/modules/Bluetooth/system/gd/rust/gddi](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/gddi)
- [packages/modules/Bluetooth/system/gd/rust/shim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/shim)
- [packages/modules/Bluetooth/system/gd/rust/stack](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/stack)
- [packages/modules/Bluetooth/system/gd/rust/topshim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim)
- [packages/modules/Bluetooth/system/gd/rust/topshim/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/facade)
- [packages/modules/Uwb/indev_uwb_adaptation](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Uwb/indev_uwb_adaptation)
- [packages/modules/Uwb/service/uci/jni](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Uwb/service/uci/jni)
- [system/nfc/src/rust](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust)
- [system/nfc/src/rust/rootcanal](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust/rootcanal)
- [system/nfc/src/rust/test](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust/test)
- [system/security/prng_seeder](https://cs.android.com/android/platform/superproject/+/master:system/security/prng_seeder)
- [system/tools/aidl](https://cs.android.com/android/platform/superproject/+/master:system/tools/aidl)

</details>

## Operating systems

### getrandom

<details><summary>
A small cross-platform library for retrieving random data from system source

</summary>

- https://crates.io/crates/getrandom
- https://docs.rs/getrandom
- https://github.com/rust-random/getrandom

</details>

### libc

<details><summary>
Raw FFI bindings to platform libraries like libc.


</summary>

- https://crates.io/crates/libc
- https://docs.rs/libc/
- https://github.com/rust-lang/libc

</details>

### os_str_bytes

<details><summary>
Convert between byte sequences and platform-native strings


</summary>

- https://crates.io/crates/os_str_bytes
- https://github.com/dylni/os_str_bytes

</details>

### shared_child

<details><summary>
a library for using child processes from multiple threads

</summary>

- https://crates.io/crates/shared_child
- https://docs.rs/shared_child
- https://github.com/oconnor663/shared_child.rs

</details><details><summary>
4 uses

</summary>

- [packages/modules/Virtualization/authfs/service](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/service)
- [packages/modules/Virtualization/compos/composd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/composd)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)
- [packages/modules/Virtualization/vmclient](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vmclient)

</details>

### which

<details><summary>
A Rust equivalent of Unix command "which". Locate installed executable in cross platforms.

</summary>

- https://crates.io/crates/which
- https://docs.rs/which/
- https://github.com/harryfei/which-rs.git

</details>

### zeroize

<details><summary>
Securely clear secrets from memory with a simple trait built on
stable Rust primitives which guarantee memory is zeroed using an
operation will not be 'optimized away' by the compiler.
Uses a portable pure Rust implementation that works everywhere,
even WASM!


</summary>

- https://crates.io/crates/zeroize
- https://github.com/RustCrypto/utils/tree/master/zeroize

</details><details><summary>
2 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/wire](https://cs.android.com/android/platform/superproject/+/master:system/keymint/wire)

</details>

### zeroize_derive

<details><summary>
Custom derive support for zeroize

</summary>

- https://crates.io/crates/zeroize_derive
- https://github.com/RustCrypto/utils/tree/master/zeroize/derive

</details>

## Operating systems::Unix APIs

### command-fds

<details><summary>
A library for passing arbitrary file descriptors when spawning child processes.

</summary>

- https://crates.io/crates/command-fds
- https://github.com/google/command-fds/

</details>

### nix

<details><summary>
Rust friendly bindings to *nix APIs

</summary>

- https://crates.io/crates/nix
- https://github.com/nix-rust/nix

</details><details><summary>
28 uses

</summary>

- [packages/modules/Bluetooth/system/gd/rust/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/common)
- [packages/modules/Bluetooth/system/gd/rust/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/facade)
- [packages/modules/Bluetooth/system/gd/rust/shim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/shim)
- [packages/modules/Bluetooth/system/gd/rust/topshim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim)
- [packages/modules/Bluetooth/system/gd/rust/topshim/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/facade)
- [packages/modules/Virtualization/apkdmverity](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/apkdmverity)
- [packages/modules/Virtualization/authfs](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs)
- [packages/modules/Virtualization/authfs/fd_server](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/fd_server)
- [packages/modules/Virtualization/authfs/service](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/service)
- [packages/modules/Virtualization/compos](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos)
- [packages/modules/Virtualization/compos/composd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/composd)
- [packages/modules/Virtualization/encryptedstore](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/encryptedstore)
- [packages/modules/Virtualization/libs/capabilities](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/capabilities)
- [packages/modules/Virtualization/libs/devicemapper](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/devicemapper)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [packages/modules/Virtualization/rialto](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/rialto)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)
- [packages/modules/Virtualization/vmbase/example](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vmbase/example)
- [packages/modules/Virtualization/vmclient](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vmclient)
- [packages/modules/Virtualization/zipfuse](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/zipfuse)
- [system/core/trusty/libtrusty-rs](https://cs.android.com/android/platform/superproject/+/master:system/core/trusty/libtrusty-rs)
- [system/security/diced](https://cs.android.com/android/platform/superproject/+/master:system/security/diced)
- [system/security/keystore2](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2)
- [system/security/keystore2/selinux](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/selinux)
- [system/security/keystore2/src/crypto](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/src/crypto)
- [system/security/keystore2/tests](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests)
- [system/security/keystore2/tests/legacy_blobs](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests/legacy_blobs)
- [system/security/prng_seeder](https://cs.android.com/android/platform/superproject/+/master:system/security/prng_seeder)

</details>

## Parser implementations

### const-oid

<details><summary>
Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard
as defined in ITU X.660, with support for BER/DER encoding/decoding as well as
heapless no_std (i.e. embedded) support


</summary>

- https://crates.io/crates/const-oid
- https://docs.rs/const-oid
- https://github.com/RustCrypto/formats/tree/master/const-oid

</details>

### csv

<details><summary>
Fast CSV parsing with support for serde.

</summary>

- http://burntsushi.net/rustdoc/csv/
- https://crates.io/crates/csv
- https://github.com/BurntSushi/rust-csv

</details>

### csv-core

<details><summary>
Bare bones CSV parsing with no_std support.

</summary>

- https://crates.io/crates/csv-core
- https://docs.rs/csv-core
- https://github.com/BurntSushi/rust-csv

</details>

### der

<details><summary>
Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules
(DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with
full support for heapless no_std targets


</summary>

- https://crates.io/crates/der
- https://github.com/RustCrypto/formats/tree/master/der

</details><details><summary>
2 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)

</details>

### der-parser

<details><summary>
Parser/encoder for ASN.1 BER/DER data

</summary>

- https://crates.io/crates/der-parser
- https://github.com/rusticata/der-parser
- https://github.com/rusticata/der-parser.git

</details>

### der_derive

<details><summary>
Custom derive support for the `der` crate's `Choice` and `Sequence` traits

</summary>

- https://crates.io/crates/der_derive
- https://docs.rs/der
- https://github.com/RustCrypto/formats/tree/master/der/derive

</details>

### litrs

<details><summary>
Parse and inspect Rust literals (i.e. tokens in the Rust programming language
representing fixed values). Particularly useful for proc macros, but can also
be used outside of a proc-macro context.


</summary>

- https://crates.io/crates/litrs
- https://docs.rs/litrs/
- https://github.com/LukasKalbertodt/litrs/

</details>

### pkcs1

<details><summary>
Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1:
RSA Cryptography Specifications Version 2.2 (RFC 8017)


</summary>

- https://crates.io/crates/pkcs1
- https://github.com/RustCrypto/formats/tree/master/pkcs1

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### pkcs8

<details><summary>
Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8:
Private-Key Information Syntax Specification (RFC 5208), with additional
support for PKCS#8v2 asymmetric key packages (RFC 5958)


</summary>

- https://crates.io/crates/pkcs8
- https://github.com/RustCrypto/formats/tree/master/pkcs8

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### sec1

<details><summary>
Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats
including ASN.1 DER-serialized private keys as well as the
Elliptic-Curve-Point-to-Octet-String encoding


</summary>

- https://crates.io/crates/sec1
- https://github.com/RustCrypto/formats/tree/master/sec1

</details><details><summary>
1 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)

</details>

### serde_json

<details><summary>
A JSON serialization file format

</summary>

- https://crates.io/crates/serde_json
- https://docs.serde.rs/serde_json/
- https://github.com/serde-rs/json

</details><details><summary>
8 uses

</summary>

- [packages/modules/Bluetooth/tools/pdl](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/pdl)
- [packages/modules/Virtualization/libs/vmconfig](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/vmconfig)
- [packages/modules/Virtualization/microdroid/payload/config](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid/payload/config)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)
- [packages/modules/Virtualization/vm](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vm)
- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)
- [system/tools/aidl/scripts/redundancy_check](https://cs.android.com/android/platform/superproject/+/master:system/tools/aidl/scripts/redundancy_check)

</details>

### shlex

<details><summary>
Split a string into shell words, like Python's shlex.

</summary>

- https://crates.io/crates/shlex
- https://github.com/comex/rust-shlex

</details>

### syn

<details><summary>
Parser for Rust source code

</summary>

- https://crates.io/crates/syn
- https://docs.rs/syn
- https://github.com/dtolnay/syn

</details><details><summary>
4 uses

</summary>

- [packages/modules/Bluetooth/system/gd/rust/gddi](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/gddi)
- [packages/modules/Bluetooth/system/gd/rust/topshim/macros](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/macros)
- [packages/modules/Bluetooth/tools/pdl](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/pdl)
- [system/keymint/derive](https://cs.android.com/android/platform/superproject/+/master:system/keymint/derive)

</details>

### url

<details><summary>
URL library for Rust, based on the WHATWG URL Standard

</summary>

- https://crates.io/crates/url
- https://docs.rs/url
- https://github.com/servo/rust-url

</details>

### uuid

<details><summary>
A library to generate and parse UUIDs.

</summary>

- https://crates.io/crates/uuid
- https://docs.rs/uuid
- https://github.com/uuid-rs/uuid

</details><details><summary>
4 uses

</summary>

- [packages/modules/Virtualization/apkdmverity](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/apkdmverity)
- [packages/modules/Virtualization/libs/devicemapper](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/devicemapper)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)

</details>

### x509-parser

<details><summary>
Parser for the X.509 v3 format (RFC 5280 certificates)

</summary>

- https://crates.io/crates/x509-parser
- https://github.com/rusticata/x509-parser
- https://github.com/rusticata/x509-parser.git

</details>

## Parsing tools

### byteorder

<details><summary>
Library for reading/writing numbers in big-endian and little-endian.

</summary>

- https://crates.io/crates/byteorder
- https://docs.rs/byteorder
- https://github.com/BurntSushi/byteorder

</details>

### ciborium

<details><summary>
serde implementation of CBOR using ciborium-basic

</summary>

- https://crates.io/crates/ciborium
- https://github.com/enarx/ciborium

</details><details><summary>
6 uses

</summary>

- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)
- [system/keymint/derive](https://cs.android.com/android/platform/superproject/+/master:system/keymint/derive)
- [system/keymint/hal](https://cs.android.com/android/platform/superproject/+/master:system/keymint/hal)
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)
- [system/keymint/tests](https://cs.android.com/android/platform/superproject/+/master:system/keymint/tests)
- [system/keymint/wire](https://cs.android.com/android/platform/superproject/+/master:system/keymint/wire)

</details>

### ciborium-ll

<details><summary>
Low-level CBOR codec primitives

</summary>

- https://crates.io/crates/ciborium-ll/0.2.0
- https://github.com/enarx/ciborium

</details>

### combine

<details><summary>
Fast parser combinators on arbitrary streams with zero-copy support.

</summary>

- https://crates.io/crates/combine
- https://docs.rs/combine
- https://github.com/Marwes/combine

</details>

### minimal-lexical

<details><summary>
Fast float parsing conversion routines.

</summary>

- https://crates.io/crates/minimal-lexical
- https://docs.rs/minimal-lexical
- https://github.com/Alexhuszagh/minimal-lexical

</details>

### nom

<details><summary>
A byte-oriented, zero-copy, parser combinators library

</summary>

- https://crates.io/crates/nom
- https://docs.rs/nom
- https://github.com/Geal/nom

</details>

### pest

<details><summary>
The Elegant Parser

</summary>

- https://crates.io/crates/pest
- https://docs.rs/pest
- https://github.com/pest-parser/pest
- https://pest.rs/

</details><details><summary>
1 uses

</summary>

- [packages/modules/Bluetooth/tools/pdl](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/pdl)

</details>

### pest_derive

<details><summary>
pest's derive macro

</summary>

- https://crates.io/crates/pest_derive
- https://docs.rs/pest
- https://github.com/pest-parser/pest
- https://pest.rs/

</details>

### pest_generator

<details><summary>
pest code generator

</summary>

- https://crates.io/crates/pest_generator
- https://docs.rs/pest
- https://github.com/pest-parser/pest
- https://pest.rs/

</details>

### pest_meta

<details><summary>
pest meta language parser and validator

</summary>

- https://crates.io/crates/pest_meta
- https://docs.rs/pest
- https://github.com/pest-parser/pest
- https://pest.rs/

</details>

### rusticata-macros

<details><summary>
Helper macros for Rusticata

</summary>

- https://crates.io/crates/rusticata-macros
- https://github.com/rusticata/rusticata-macros
- https://github.com/rusticata/rusticata-macros.git

</details>

### xml-rs

<details><summary>
An XML library in pure Rust

</summary>

- http://docs.rs/xml-rs/
- https://crates.io/crates/xml-rs
- https://github.com/netvl/xml-rs

</details>

## Rendering::Graphics APIs

### vulkano

<details><summary>
Safe wrapper for the Vulkan graphics API

</summary>

- https://crates.io/crates/vulkano
- https://docs.rs/vulkano
- https://github.com/vulkano-rs/vulkano
- https://vulkano.rs

</details>

## Rust patterns

### anyhow

<details><summary>
Flexible concrete Error type built on std::error::Error

</summary>

- https://crates.io/crates/anyhow
- https://docs.rs/anyhow
- https://github.com/dtolnay/anyhow

</details><details><summary>
43 uses

</summary>

- [hardware/interfaces/security/dice/aidl/default](https://cs.android.com/android/platform/superproject/+/master:hardware/interfaces/security/dice/aidl/default)
- [hardware/interfaces/security/dice/aidl/vts/functional](https://cs.android.com/android/platform/superproject/+/master:hardware/interfaces/security/dice/aidl/vts/functional)
- [packages/modules/Virtualization/apkdmverity](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/apkdmverity)
- [packages/modules/Virtualization/authfs](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs)
- [packages/modules/Virtualization/authfs/fd_server](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/fd_server)
- [packages/modules/Virtualization/authfs/service](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/service)
- [packages/modules/Virtualization/authfs/tests/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/tests/common)
- [packages/modules/Virtualization/avmd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/avmd)
- [packages/modules/Virtualization/compos](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos)
- [packages/modules/Virtualization/compos/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/common)
- [packages/modules/Virtualization/compos/composd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/composd)
- [packages/modules/Virtualization/compos/composd/native](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/composd/native)
- [packages/modules/Virtualization/compos/composd_cmd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/composd_cmd)
- [packages/modules/Virtualization/compos/verify](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/verify)
- [packages/modules/Virtualization/compos/verify/native](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/verify/native)
- [packages/modules/Virtualization/encryptedstore](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/encryptedstore)
- [packages/modules/Virtualization/libs/apkverify](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/apkverify)
- [packages/modules/Virtualization/libs/capabilities](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/capabilities)
- [packages/modules/Virtualization/libs/devicemapper](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/devicemapper)
- [packages/modules/Virtualization/libs/nested_virt](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/nested_virt)
- [packages/modules/Virtualization/libs/vbmeta](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/vbmeta)
- [packages/modules/Virtualization/libs/vmconfig](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/vmconfig)
- [packages/modules/Virtualization/microdroid/initrd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid/initrd)
- [packages/modules/Virtualization/microdroid/payload/metadata](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid/payload/metadata)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [packages/modules/Virtualization/pvmfw/avb](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/pvmfw/avb)
- [packages/modules/Virtualization/rialto](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/rialto)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)
- [packages/modules/Virtualization/vm](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vm)
- [packages/modules/Virtualization/vm_payload](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vm_payload)
- [packages/modules/Virtualization/vmbase/example](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vmbase/example)
- [packages/modules/Virtualization/zipfuse](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/zipfuse)
- [system/extras/profcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd)
- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)
- [system/librustutils](https://cs.android.com/android/platform/superproject/+/master:system/librustutils)
- [system/security/diced](https://cs.android.com/android/platform/superproject/+/master:system/security/diced)
- [system/security/keystore2](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2)
- [system/security/keystore2/legacykeystore](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/legacykeystore)
- [system/security/keystore2/selinux](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/selinux)
- [system/security/keystore2/tests](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests)
- [system/security/keystore2/tests/legacy_blobs](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests/legacy_blobs)
- [system/security/prng_seeder](https://cs.android.com/android/platform/superproject/+/master:system/security/prng_seeder)
- [system/tools/aidl/scripts/redundancy_check](https://cs.android.com/android/platform/superproject/+/master:system/tools/aidl/scripts/redundancy_check)

</details>

### bencher

<details><summary>
A port of the libtest (unstable Rust) benchmark runner to Rust stable releases. Supports running benchmarks and filtering based on the name. Benchmark execution works exactly the same way and no more (caveat: black_box is still missing!).

</summary>

- https://crates.io/crates/bencher
- https://docs.rs/bencher/
- https://github.com/bluss/bencher/

</details>

### enumn

<details><summary>
Convert number to enum

</summary>

- https://crates.io/crates/enumn
- https://docs.rs/enumn
- https://github.com/dtolnay/enumn

</details>

### itertools

<details><summary>
Extra iterator adaptors, iterator methods, free functions, and macros.

</summary>

- https://crates.io/crates/itertools
- https://docs.rs/itertools/
- https://github.com/rust-itertools/itertools

</details>

### lazy_static

<details><summary>
A macro for declaring lazily evaluated statics in Rust.

</summary>

- https://crates.io/crates/lazy_static
- https://docs.rs/lazy_static
- https://github.com/rust-lang-nursery/lazy-static.rs

</details>

### merge

<details><summary>
Merge multiple values into one

</summary>

- https://crates.io/crates/merge
- https://git.sr.ht/~ireas/merge-rs

</details>

### merge_derive

<details><summary>
Derive macro for the merge::Merge trait

</summary>

- https://crates.io/crates/merge_derive
- https://git.sr.ht/~ireas/merge-rs/tree/master/merge_derive

</details>

### once_cell

<details><summary>
Single assignment cells and lazy values.

</summary>

- https://crates.io/crates/once_cell
- https://docs.rs/once_cell
- https://github.com/matklad/once_cell

</details><details><summary>
2 uses

</summary>

- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)

</details>

### os_str_bytes

<details><summary>
Convert between byte sequences and platform-native strings


</summary>

- https://crates.io/crates/os_str_bytes
- https://github.com/dylni/os_str_bytes

</details>

### peeking_take_while

<details><summary>
Like `Iterator::take_while`, but calls the predicate on a peeked value. This allows you to use `Iterator::by_ref` and `Iterator::take_while` together, and still get the first value for which the `take_while` predicate returned false after dropping the `by_ref`.

</summary>

- https://crates.io/crates/peeking_take_while
- https://github.com/fitzgen/peeking_take_while

</details>

### pin-project

<details><summary>
A crate for safe and ergonomic pin-projection.


</summary>

- https://crates.io/crates/pin-project
- https://github.com/taiki-e/pin-project

</details>

### pin-project-internal

<details><summary>
Implementation detail of the `pin-project` crate.


</summary>

- https://crates.io/crates/pin-project-internal
- https://github.com/taiki-e/pin-project

</details>

### pin-project-lite

<details><summary>
A lightweight version of pin-project written with declarative macros.


</summary>

- https://crates.io/crates/pin-project-lite
- https://github.com/taiki-e/pin-project-lite

</details>

### scopeguard

<details><summary>
A RAII scope guard that will run a given closure when it goes out of scope,
even if the code between panics (assuming unwinding panic).

Defines the macros `defer!`, `defer_on_unwind!`, `defer_on_success!` as
shorthands for guards with one of the implemented strategies.


</summary>

- https://crates.io/crates/scopeguard
- https://docs.rs/scopeguard/
- https://github.com/bluss/scopeguard

</details><details><summary>
6 uses

</summary>

- [packages/modules/Virtualization/apkdmverity](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/apkdmverity)
- [packages/modules/Virtualization/compos](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos)
- [packages/modules/Virtualization/libs/capabilities](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/capabilities)
- [packages/modules/Virtualization/libs/devicemapper](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/devicemapper)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [packages/modules/Virtualization/zipfuse](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/zipfuse)

</details>

### static_assertions

<details><summary>
Compile-time assertions to ensure that invariants are met.

</summary>

- https://crates.io/crates/static_assertions
- https://docs.rs/static_assertions/
- https://github.com/nvzqz/static-assertions-rs

</details>

### thiserror

<details><summary>
derive(Error)

</summary>

- https://crates.io/crates/thiserror
- https://docs.rs/thiserror
- https://github.com/dtolnay/thiserror

</details><details><summary>
26 uses

</summary>

- [packages/modules/Bluetooth/system/gd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd)
- [packages/modules/Bluetooth/system/gd/rust/stack](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/stack)
- [packages/modules/Bluetooth/tools/pdl](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/pdl)
- [packages/modules/Bluetooth/tools/rootcanal/lmp](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/rootcanal/lmp)
- [packages/modules/Uwb/indev_uwb_adaptation](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Uwb/indev_uwb_adaptation)
- [packages/modules/Uwb/service/uci/jni](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Uwb/service/uci/jni)
- [packages/modules/Virtualization/authfs](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs)
- [packages/modules/Virtualization/libs/apexutil](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/apexutil)
- [packages/modules/Virtualization/libs/statslog_virtualization](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/statslog_virtualization)
- [packages/modules/Virtualization/libs/vbmeta](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/vbmeta)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [packages/modules/Virtualization/vmclient](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vmclient)
- [system/core/debuggerd/rust/tombstoned_client](https://cs.android.com/android/platform/superproject/+/master:system/core/debuggerd/rust/tombstoned_client)
- [system/librustutils](https://cs.android.com/android/platform/superproject/+/master:system/librustutils)
- [system/nfc/src](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src)
- [system/nfc/src/rust](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust)
- [system/nfc/src/rust/rootcanal](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust/rootcanal)
- [system/nfc/src/rust/test](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust/test)
- [system/security/diced](https://cs.android.com/android/platform/superproject/+/master:system/security/diced)
- [system/security/diced/open_dice_cbor](https://cs.android.com/android/platform/superproject/+/master:system/security/diced/open_dice_cbor)
- [system/security/keystore2](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2)
- [system/security/keystore2/legacykeystore](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/legacykeystore)
- [system/security/keystore2/selinux](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/selinux)
- [system/security/keystore2/src/crypto](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/src/crypto)
- [system/security/keystore2/tests](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests)
- [system/security/keystore2/tests/legacy_blobs](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests/legacy_blobs)

</details>

## Science

### num-bigint

<details><summary>
Big integer implementation for Rust

</summary>

- https://crates.io/crates/num-bigint
- https://docs.rs/num-bigint
- https://github.com/rust-num/num-bigint

</details>

### num-derive

<details><summary>
Numeric syntax extensions

</summary>

- https://crates.io/crates/num-derive
- https://docs.rs/num-derive
- https://github.com/rust-num/num-derive

</details>

### num-integer

<details><summary>
Integer traits and functions

</summary>

- https://crates.io/crates/num-integer
- https://docs.rs/num-integer
- https://github.com/rust-num/num-integer

</details>

### num-traits

<details><summary>
Numeric traits for generic mathematics

</summary>

- https://crates.io/crates/num-traits
- https://docs.rs/num-traits
- https://github.com/rust-num/num-traits

</details>

## Template engine

### tinytemplate

<details><summary>
Simple, lightweight template engine

</summary>

- https://crates.io/crates/tinytemplate
- https://github.com/bheisler/TinyTemplate

</details>

## Text processing

### aho-corasick

<details><summary>
Fast multiple substring searching.

</summary>

- https://crates.io/crates/aho-corasick
- https://github.com/BurntSushi/aho-corasick

</details>

### bstr

<details><summary>
A string type that is not required to be valid UTF-8.

</summary>

- https://crates.io/crates/bstr
- https://docs.rs/bstr
- https://github.com/BurntSushi/bstr

</details>

### regex

<details><summary>
An implementation of regular expressions for Rust. This implementation uses
finite automata and guarantees linear time matching on all inputs.


</summary>

- https://crates.io/crates/regex
- https://docs.rs/regex
- https://github.com/rust-lang/regex

</details><details><summary>
4 uses

</summary>

- [packages/modules/Virtualization/compos](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos)
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)
- [system/keymint/hal](https://cs.android.com/android/platform/superproject/+/master:system/keymint/hal)
- [system/tools/aidl/scripts/redundancy_check](https://cs.android.com/android/platform/superproject/+/master:system/tools/aidl/scripts/redundancy_check)

</details>

### regex-automata

<details><summary>
Automata construction and matching using regular expressions.

</summary>

- https://crates.io/crates/regex-automata
- https://docs.rs/regex-automata
- https://github.com/BurntSushi/regex-automata

</details>

### textwrap

<details><summary>
Powerful library for word wrapping, indenting, and dedenting strings

</summary>

- https://crates.io/crates/textwrap
- https://docs.rs/textwrap/
- https://github.com/mgeisler/textwrap

</details>

### unicode-bidi

<details><summary>
Implementation of the Unicode Bidirectional Algorithm

</summary>

- https://crates.io/crates/unicode-bidi
- https://docs.rs/unicode-bidi/
- https://github.com/servo/unicode-bidi

</details>

## Value formatting

### itoa

<details><summary>
Fast integer primitive to string conversion

</summary>

- https://crates.io/crates/itoa
- https://docs.rs/itoa
- https://github.com/dtolnay/itoa

</details>

### ryu

<details><summary>
Fast floating point to string conversion

</summary>

- https://crates.io/crates/ryu
- https://docs.rs/ryu
- https://github.com/dtolnay/ryu

</details>

## Visualization

### criterion-plot

<details><summary>
Criterion's plotting library

</summary>

- https://crates.io/crates/criterion-plot
- https://github.com/bheisler/criterion.rs

</details>

### plotters

<details><summary>
A Rust drawing library focus on data plotting for both WASM and native applications

</summary>

- https://crates.io/crates/plotters
- https://github.com/plotters-rs/plotters
- https://plotters-rs.github.io/

</details>

## Web programming

### url

<details><summary>
URL library for Rust, based on the WHATWG URL Standard

</summary>

- https://crates.io/crates/url
- https://docs.rs/url
- https://github.com/servo/rust-url

</details>

## WebAssembly

### plotters

<details><summary>
A Rust drawing library focus on data plotting for both WASM and native applications

</summary>

- https://crates.io/crates/plotters
- https://github.com/plotters-rs/plotters
- https://plotters-rs.github.io/

</details>

### uuid

<details><summary>
A library to generate and parse UUIDs.

</summary>

- https://crates.io/crates/uuid
- https://docs.rs/uuid
- https://github.com/uuid-rs/uuid

</details><details><summary>
4 uses

</summary>

- [packages/modules/Virtualization/apkdmverity](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/apkdmverity)
- [packages/modules/Virtualization/libs/devicemapper](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/devicemapper)
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)
- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)

</details>



# rust components found in AOSP

- [device/google/cuttlefish/guest/hals/keymint/rust](https://cs.android.com/android/platform/superproject/+/master:device/google/cuttlefish/guest/hals/keymint/rust)([android_logger](#android_logger), [hex](#hex))
- [device/google/cuttlefish/host/commands/append_squashfs_overlay](https://cs.android.com/android/platform/superproject/+/master:device/google/cuttlefish/host/commands/append_squashfs_overlay)([clap](#clap))
- [device/google/cuttlefish/host/commands/secure_env/rust](https://cs.android.com/android/platform/superproject/+/master:device/google/cuttlefish/host/commands/secure_env/rust)([env_logger](#env_logger), [hex](#hex))
- [hardware/interfaces/security/dice/aidl/default](https://cs.android.com/android/platform/superproject/+/master:hardware/interfaces/security/dice/aidl/default)([anyhow](#anyhow), [android_logger](#android_logger), [serde](#serde))
- [hardware/interfaces/security/dice/aidl/vts/functional](https://cs.android.com/android/platform/superproject/+/master:hardware/interfaces/security/dice/aidl/vts/functional)([anyhow](#anyhow))
- [hardware/interfaces/security/keymint/aidl](https://cs.android.com/android/platform/superproject/+/master:hardware/interfaces/security/keymint/aidl)
- [packages/modules/Bluetooth/system/gd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd)([thiserror](#thiserror))
- [packages/modules/Bluetooth/system/gd/rust/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/common)([futures](#futures), [android_logger](#android_logger), [grpcio](#grpcio), [env_logger](#env_logger), [tokio](#tokio), [nix](#nix))
- [packages/modules/Bluetooth/system/gd/rust/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/facade)([futures](#futures), [grpcio](#grpcio), [protobuf](#protobuf), [clap](#clap), [tokio](#tokio), [nix](#nix))
- [packages/modules/Bluetooth/system/gd/rust/gddi](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/gddi)([quote](#quote), [syn](#syn), [tokio](#tokio))
- [packages/modules/Bluetooth/system/gd/rust/shim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/shim)([futures](#futures), [tokio](#tokio), [nix](#nix))
- [packages/modules/Bluetooth/system/gd/rust/stack](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/stack)([futures](#futures), [grpcio](#grpcio), [thiserror](#thiserror), [protobuf](#protobuf), [tokio](#tokio))
- [packages/modules/Bluetooth/system/gd/rust/topshim](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim)([futures](#futures), [grpcio](#grpcio), [tokio](#tokio), [nix](#nix))
- [packages/modules/Bluetooth/system/gd/rust/topshim/facade](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/facade)([futures](#futures), [grpcio](#grpcio), [tokio](#tokio), [clap](#clap), [nix](#nix))
- [packages/modules/Bluetooth/system/gd/rust/topshim/macros](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/system/gd/rust/topshim/macros)([quote](#quote), [syn](#syn))
- [packages/modules/Bluetooth/tools/pdl](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/pdl)([quote](#quote), [syn](#syn), [pest](#pest), [thiserror](#thiserror), [clap](#clap), [serde](#serde), [serde_json](#serde_json), [tempfile](#tempfile))
- [packages/modules/Bluetooth/tools/rootcanal/lmp](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Bluetooth/tools/rootcanal/lmp)([rand](#rand), [thiserror](#thiserror))
- [packages/modules/DnsResolver](https://cs.android.com/android/platform/superproject/+/master:packages/modules/DnsResolver)
- [packages/modules/Uwb/indev_uwb_adaptation](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Uwb/indev_uwb_adaptation)([thiserror](#thiserror), [tokio](#tokio), [jni](#jni))
- [packages/modules/Uwb/service/uci/jni](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Uwb/service/uci/jni)([thiserror](#thiserror), [tokio](#tokio), [jni](#jni))
- [packages/modules/Virtualization/apkdmverity](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/apkdmverity)([anyhow](#anyhow), [uuid](#uuid), [clap](#clap), [scopeguard](#scopeguard), [tempfile](#tempfile), [nix](#nix))
- [packages/modules/Virtualization/authfs](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs)([anyhow](#anyhow), [android_logger](#android_logger), [thiserror](#thiserror), [clap](#clap), [protobuf](#protobuf), [nix](#nix), [openssl](#openssl))
- [packages/modules/Virtualization/authfs/fd_server](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/fd_server)([anyhow](#anyhow), [android_logger](#android_logger), [clap](#clap), [nix](#nix))
- [packages/modules/Virtualization/authfs/service](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/service)([anyhow](#anyhow), [android_logger](#android_logger), [shared_child](#shared_child), [nix](#nix))
- [packages/modules/Virtualization/authfs/src/fsverity/metadata](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/src/fsverity/metadata)([openssl](#openssl))
- [packages/modules/Virtualization/authfs/tests/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/authfs/tests/common)([anyhow](#anyhow), [android_logger](#android_logger), [clap](#clap))
- [packages/modules/Virtualization/avmd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/avmd)([anyhow](#anyhow), [tempfile](#tempfile), [serde_cbor](#serde_cbor), [clap](#clap), [serde](#serde), [hex](#hex))
- [packages/modules/Virtualization/compos](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos)([anyhow](#anyhow), [android_logger](#android_logger), [regex](#regex), [protobuf](#protobuf), [scopeguard](#scopeguard), [nix](#nix))
- [packages/modules/Virtualization/compos/common](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/common)([anyhow](#anyhow))
- [packages/modules/Virtualization/compos/composd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/composd)([anyhow](#anyhow), [android_logger](#android_logger), [num_cpus](#num_cpus), [shared_child](#shared_child), [nix](#nix))
- [packages/modules/Virtualization/compos/composd/native](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/composd/native)([anyhow](#anyhow))
- [packages/modules/Virtualization/compos/composd_cmd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/composd_cmd)([anyhow](#anyhow), [clap](#clap))
- [packages/modules/Virtualization/compos/verify](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/verify)([anyhow](#anyhow), [android_logger](#android_logger), [clap](#clap))
- [packages/modules/Virtualization/compos/verify/native](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/compos/verify/native)([anyhow](#anyhow))
- [packages/modules/Virtualization/encryptedstore](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/encryptedstore)([anyhow](#anyhow), [android_logger](#android_logger), [clap](#clap), [nix](#nix), [hex](#hex))
- [packages/modules/Virtualization/libs/apexutil](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/apexutil)([thiserror](#thiserror), [zip](#zip), [hex](#hex))
- [packages/modules/Virtualization/libs/apkverify](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/apkverify)([anyhow](#anyhow), [openssl](#openssl), [serde](#serde), [zip](#zip), [hex](#hex))
- [packages/modules/Virtualization/libs/capabilities](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/capabilities)([anyhow](#anyhow), [scopeguard](#scopeguard), [nix](#nix))
- [packages/modules/Virtualization/libs/devicemapper](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/devicemapper)([anyhow](#anyhow), [uuid](#uuid), [scopeguard](#scopeguard), [tempfile](#tempfile), [nix](#nix), [hex](#hex))
- [packages/modules/Virtualization/libs/dice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/dice)
- [packages/modules/Virtualization/libs/fdtpci](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/fdtpci)
- [packages/modules/Virtualization/libs/libfdt](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/libfdt)
- [packages/modules/Virtualization/libs/nested_virt](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/nested_virt)([anyhow](#anyhow))
- [packages/modules/Virtualization/libs/statslog_virtualization](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/statslog_virtualization)([thiserror](#thiserror))
- [packages/modules/Virtualization/libs/vbmeta](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/vbmeta)([anyhow](#anyhow), [tempfile](#tempfile), [thiserror](#thiserror))
- [packages/modules/Virtualization/libs/vmconfig](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/libs/vmconfig)([anyhow](#anyhow), [serde](#serde), [semver](#semver), [serde_json](#serde_json))
- [packages/modules/Virtualization/microdroid/initrd](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid/initrd)([anyhow](#anyhow), [clap](#clap))
- [packages/modules/Virtualization/microdroid/payload/config](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid/payload/config)([serde_json](#serde_json), [serde](#serde))
- [packages/modules/Virtualization/microdroid/payload/metadata](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid/payload/metadata)([anyhow](#anyhow), [protobuf](#protobuf))
- [packages/modules/Virtualization/microdroid_manager](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/microdroid_manager)([anyhow](#anyhow), [serde](#serde), [serde_json](#serde_json), [nix](#nix), [vsock](#vsock), [scopeguard](#scopeguard), [kernlog](#kernlog), [hex](#hex), [openssl](#openssl), [rand](#rand), [protobuf](#protobuf), [once_cell](#once_cell), [glob](#glob), [uuid](#uuid), [serde_cbor](#serde_cbor), [thiserror](#thiserror), [tempfile](#tempfile))
- [packages/modules/Virtualization/pvmfw](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/pvmfw)
- [packages/modules/Virtualization/pvmfw/avb](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/pvmfw/avb)([anyhow](#anyhow))
- [packages/modules/Virtualization/rialto](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/rialto)([anyhow](#anyhow), [android_logger](#android_logger), [nix](#nix))
- [packages/modules/Virtualization/virtualizationservice](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/virtualizationservice)([anyhow](#anyhow), [serde](#serde), [serde_json](#serde_json), [nix](#nix), [zip](#zip), [vsock](#vsock), [android_logger](#android_logger), [shared_child](#shared_child), [semver](#semver), [once_cell](#once_cell), [regex](#regex), [clap](#clap), [tempfile](#tempfile))
- [packages/modules/Virtualization/vm](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vm)([anyhow](#anyhow), [rand](#rand), [serde](#serde), [zip](#zip), [env_logger](#env_logger), [clap](#clap), [serde_json](#serde_json))
- [packages/modules/Virtualization/vm_payload](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vm_payload)([anyhow](#anyhow), [vsock](#vsock), [android_logger](#android_logger))
- [packages/modules/Virtualization/vmbase](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vmbase)([psci](#psci))
- [packages/modules/Virtualization/vmbase/example](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vmbase/example)([anyhow](#anyhow), [android_logger](#android_logger), [nix](#nix))
- [packages/modules/Virtualization/vmclient](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/vmclient)([thiserror](#thiserror), [shared_child](#shared_child), [nix](#nix))
- [packages/modules/Virtualization/zipfuse](https://cs.android.com/android/platform/superproject/+/master:packages/modules/Virtualization/zipfuse)([anyhow](#anyhow), [nix](#nix), [clap](#clap), [scopeguard](#scopeguard), [tempfile](#tempfile), [zip](#zip))
- [system/core/debuggerd/rust/tombstoned_client](https://cs.android.com/android/platform/superproject/+/master:system/core/debuggerd/rust/tombstoned_client)([thiserror](#thiserror))
- [system/core/libstats/pull_rust](https://cs.android.com/android/platform/superproject/+/master:system/core/libstats/pull_rust)
- [system/core/trusty/keymint](https://cs.android.com/android/platform/superproject/+/master:system/core/trusty/keymint)([android_logger](#android_logger))
- [system/core/trusty/libtrusty-rs](https://cs.android.com/android/platform/superproject/+/master:system/core/trusty/libtrusty-rs)([nix](#nix))
- [system/extras/profcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd)([anyhow](#anyhow))
- [system/extras/profcollectd/libprofcollectd](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd)([anyhow](#anyhow), [rand](#rand), [uuid](#uuid), [android_logger](#android_logger), [macaddr](#macaddr), [serde_json](#serde_json), [chrono](#chrono), [serde](#serde), [zip](#zip))
- [system/extras/profcollectd/libprofcollectd/bindings/libflags](https://cs.android.com/android/platform/superproject/+/master:system/extras/profcollectd/libprofcollectd/bindings/libflags)
- [system/keymint/boringssl](https://cs.android.com/android/platform/superproject/+/master:system/keymint/boringssl)([openssl](#openssl))
- [system/keymint/common](https://cs.android.com/android/platform/superproject/+/master:system/keymint/common)([pkcs1](#pkcs1), [coset](#coset), [spki](#spki), [pkcs8](#pkcs8), [der](#der), [ciborium](#ciborium), [zeroize](#zeroize), [sec1](#sec1), [hex](#hex))
- [system/keymint/derive](https://cs.android.com/android/platform/superproject/+/master:system/keymint/derive)([quote](#quote), [syn](#syn), [ciborium](#ciborium))
- [system/keymint/hal](https://cs.android.com/android/platform/superproject/+/master:system/keymint/hal)([regex](#regex), [ciborium](#ciborium), [hex](#hex))
- [system/keymint/ta](https://cs.android.com/android/platform/superproject/+/master:system/keymint/ta)([coset](#coset), [spki](#spki), [flagset](#flagset), [der](#der), [ciborium](#ciborium), [hex](#hex))
- [system/keymint/tests](https://cs.android.com/android/platform/superproject/+/master:system/keymint/tests)([env_logger](#env_logger), [ciborium](#ciborium), [hex](#hex))
- [system/keymint/wire](https://cs.android.com/android/platform/superproject/+/master:system/keymint/wire)([coset](#coset), [ciborium](#ciborium), [zeroize](#zeroize), [hex](#hex))
- [system/librustutils](https://cs.android.com/android/platform/superproject/+/master:system/librustutils)([anyhow](#anyhow), [arbitrary](#arbitrary), [thiserror](#thiserror))
- [system/logging/rust](https://cs.android.com/android/platform/superproject/+/master:system/logging/rust)([android_logger](#android_logger), [env_logger](#env_logger))
- [system/nfc/src](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src)([thiserror](#thiserror))
- [system/nfc/src/rust](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust)([thiserror](#thiserror), [tokio](#tokio))
- [system/nfc/src/rust/rootcanal](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust/rootcanal)([thiserror](#thiserror), [tokio](#tokio))
- [system/nfc/src/rust/test](https://cs.android.com/android/platform/superproject/+/master:system/nfc/src/rust/test)([thiserror](#thiserror), [tokio](#tokio))
- [system/security/diced](https://cs.android.com/android/platform/superproject/+/master:system/security/diced)([anyhow](#anyhow), [android_logger](#android_logger), [serde_cbor](#serde_cbor), [thiserror](#thiserror), [serde](#serde), [nix](#nix))
- [system/security/diced/open_dice_cbor](https://cs.android.com/android/platform/superproject/+/master:system/security/diced/open_dice_cbor)([thiserror](#thiserror))
- [system/security/keystore2](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2)([futures](#futures), [anyhow](#anyhow), [serde](#serde), [nix](#nix), [rusqlite](#rusqlite), [android_logger](#android_logger), [rand](#rand), [serde_cbor](#serde_cbor), [thiserror](#thiserror))
- [system/security/keystore2/aaid](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/aaid)
- [system/security/keystore2/aidl](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/aidl)
- [system/security/keystore2/apc_compat](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/apc_compat)
- [system/security/keystore2/legacykeystore](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/legacykeystore)([anyhow](#anyhow), [rusqlite](#rusqlite), [thiserror](#thiserror))
- [system/security/keystore2/selinux](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/selinux)([anyhow](#anyhow), [android_logger](#android_logger), [thiserror](#thiserror), [num_cpus](#num_cpus), [nix](#nix))
- [system/security/keystore2/src/crypto](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/src/crypto)([nix](#nix), [thiserror](#thiserror))
- [system/security/keystore2/src/fuzzers](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/src/fuzzers)([arbitrary](#arbitrary))
- [system/security/keystore2/src/km_compat](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/src/km_compat)
- [system/security/keystore2/src/vintf](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/src/vintf)
- [system/security/keystore2/tests](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests)([anyhow](#anyhow), [thiserror](#thiserror), [serde](#serde), [nix](#nix), [openssl](#openssl))
- [system/security/keystore2/tests/legacy_blobs](https://cs.android.com/android/platform/superproject/+/master:system/security/keystore2/tests/legacy_blobs)([anyhow](#anyhow), [thiserror](#thiserror), [nix](#nix), [serde](#serde))
- [system/security/prng_seeder](https://cs.android.com/android/platform/superproject/+/master:system/security/prng_seeder)([anyhow](#anyhow), [clap](#clap), [tokio](#tokio), [nix](#nix))
- [system/tools/aidl](https://cs.android.com/android/platform/superproject/+/master:system/tools/aidl)([tokio](#tokio))
- [system/tools/aidl/scripts/redundancy_check](https://cs.android.com/android/platform/superproject/+/master:system/tools/aidl/scripts/redundancy_check)([anyhow](#anyhow), [regex](#regex), [clap](#clap), [serde](#serde), [serde_json](#serde_json))
