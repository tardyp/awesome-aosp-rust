# Summary

# Asynchronous

## futures

An implementation of futures and streams featuring zero allocations, composability, and iterator-like interfaces.

- https://crates.io/crates/futures
- https://rust-lang.github.io/futures-rs
- https://github.com/rust-lang/futures-rs

## tokio

An event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications.

- https://crates.io/crates/tokio
- https://tokio.rs
- https://github.com/tokio-rs/tokio

## tokio-macros

Tokio\'s proc macros.

- https://crates.io/crates/tokio-macros
- https://tokio.rs
- https://github.com/tokio-rs/tokio

## mio

Lightweight non-blocking IO

- https://crates.io/crates/mio
- https://github.com/tokio-rs/mio
- https://github.com/tokio-rs/mio

## async-trait

Type erasure for async trait methods

- https://crates.io/crates/async-trait
- https://docs.rs/async-trait
- https://github.com/dtolnay/async-trait

## tokio-stream

Utilities to work with `Stream` and `tokio`.

- https://crates.io/crates/tokio-stream
- https://tokio.rs
- https://github.com/tokio-rs/tokio

## grpcio

The rust language implementation of gRPC, base on the gRPC c core library.

- https://crates.io/crates/grpcio
- https://github.com/tikv/grpc-rs
- https://docs.rs/grpcio
- https://github.com/tikv/grpc-rs

## tokio-test

Testing utilities for Tokio- and futures-based code

- https://crates.io/crates/tokio-test
- https://tokio.rs
- https://docs.rs/tokio-test/0.4.2/tokio_test
- https://github.com/tokio-rs/tokio

# Development tools::Debugging

## gdbstub

An implementation of the GDB Remote Serial Protocol in Rust

- https://crates.io/crates/gdbstub
- https://github.com/daniel5151/gdbstub
- https://docs.rs/gdbstub
- https://github.com/daniel5151/gdbstub

## gdbstub_arch

Implementations of `gdbstub::arch::Arch` for various architectures.

- https://crates.io/crates/gdbstub_arch
- https://github.com/daniel5151/gdbstub
- https://docs.rs/gdbstub_arch
- https://github.com/daniel5151/gdbstub

## env_logger

A logging implementation for `log` which is configured via an environment variable.

- https://crates.io/crates/env_logger
- https://github.com/rust-cli/env_logger/

## log

A lightweight logging facade for Rust

- https://crates.io/crates/log
- https://docs.rs/log
- https://github.com/rust-lang/log

# Cryptography

## sec1

Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys (also described in RFC5915) as well as the Elliptic-Curve-Point-to-Octet-String and Octet-String-to-Elliptic Curve-Point encoding algorithms.

- https://crates.io/crates/sec1
- https://github.com/RustCrypto/formats/tree/master/sec1

## coset

Set of types for supporting COSE

- https://crates.io/crates/coset
- https://github.com/google/coset

## zeroize_derive

Custom derive support for zeroize

- https://crates.io/crates/zeroize_derive
- https://github.com/RustCrypto/utils/tree/master/zeroize/derive

## x509-cert

Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280.

- https://crates.io/crates/x509-cert
- https://github.com/RustCrypto/formats/tree/master/x509-cert

## der_derive

Custom derive support for the `der` crate\'s `Choice` and `Sequence` traits

- https://crates.io/crates/der_derive
- https://docs.rs/der
- https://github.com/RustCrypto/formats/tree/master/der/derive

## ring

Safe, fast, small crypto using Rust.

- https://crates.io/crates/ring
- https://briansmith.org/rustdoc/ring/
- https://github.com/briansmith/ring

## zeroize

Securely zero memory while avoiding compiler optimizations.

- https://crates.io/crates/zeroize
- https://github.com/RustCrypto/utils/tree/master/zeroize

## pkcs8

Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208).

- https://crates.io/crates/pkcs8
- https://github.com/RustCrypto/formats/tree/master/pkcs8

## pkcs1

Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017).

- https://crates.io/crates/pkcs1
- https://github.com/RustCrypto/formats/tree/master/pkcs1

## x509-parser

Parser for the X.509 v3 format (RFC 5280 certificates)

- https://crates.io/crates/x509-parser
- https://github.com/rusticata/x509-parser
- https://github.com/rusticata/x509-parser.git

## openssl

OpenSSL bindings

- https://crates.io/crates/openssl
- https://github.com/sfackler/rust-openssl
- https://github.com/sfackler/rust-openssl

## ppv-lite86

Implementation of the crypto-simd API for x86

- https://crates.io/crates/ppv-lite86
- https://github.com/cryptocorrosion/cryptocorrosion

## const-oid

Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard as defined in ITU X.660, with support for BER/DER encoding/decoding as well as heapless no_std (i.e. embedded) support

- https://crates.io/crates/const-oid
- https://docs.rs/const-oid
- https://github.com/RustCrypto/formats/tree/master/const-oid

## webpki

Web PKI X.509 Certificate Verification.

- https://crates.io/crates/webpki
- https://briansmith.org/rustdoc/webpki/
- https://github.com/briansmith/webpki

## spki

X.509 Subject Public Key Info types describing public keys as well as their associated AlgorithmIdentifiers (i.e. OIDs).

- https://crates.io/crates/spki
- https://github.com/RustCrypto/formats/tree/master/spki

## der

Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690.

- https://crates.io/crates/der
- https://github.com/RustCrypto/formats/tree/master/der

# Data structures

## crossbeam-queue

Concurrent queues

- https://crates.io/crates/crossbeam-queue
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-queue
- https://github.com/crossbeam-rs/crossbeam

## der_derive

Custom derive support for the `der` crate\'s `Choice` and `Sequence` traits

- https://crates.io/crates/der_derive
- https://docs.rs/der
- https://github.com/RustCrypto/formats/tree/master/der/derive

## indexmap

A hash table with consistent order and fast iteration.

- https://crates.io/crates/indexmap/1.9.1
- https://docs.rs/indexmap/
- https://github.com/bluss/indexmap

## uuid

A library to generate and parse UUIDs.

- https://crates.io/crates/uuid
- https://github.com/uuid-rs/uuid
- https://docs.rs/uuid
- https://github.com/uuid-rs/uuid

## smallvec

\'Small vector\' optimization: store up to a small number of items on the stack

- https://crates.io/crates/smallvec
- https://docs.rs/smallvec/
- https://github.com/servo/rust-smallvec

## crossbeam-deque

Concurrent work-stealing deque

- https://crates.io/crates/crossbeam-deque
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-deque
- https://github.com/crossbeam-rs/crossbeam

## spki

X.509 Subject Public Key Info types describing public keys as well as their associated AlgorithmIdentifiers (i.e. OIDs).

- https://crates.io/crates/spki
- https://github.com/RustCrypto/formats/tree/master/spki

## intrusive-collections

Intrusive collections for Rust (linked list and red-black tree)

- https://crates.io/crates/intrusive-collections
- https://docs.rs/intrusive-collections
- https://github.com/Amanieu/intrusive-rs

## x509-cert

Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280.

- https://crates.io/crates/x509-cert
- https://github.com/RustCrypto/formats/tree/master/x509-cert

## ciborium-ll

Low-level CBOR codec primitives

- https://crates.io/crates/ciborium-ll/0.2.0
- https://github.com/enarx/ciborium
- https://github.com/enarx/ciborium

## bytes

Types and traits for working with bytes

- https://crates.io/crates/bytes
- https://github.com/tokio-rs/bytes

## ciborium-io

Simplified Read/Write traits for no_std usage

- https://crates.io/crates/ciborium-io/0.2.0
- https://github.com/enarx/ciborium
- https://github.com/enarx/ciborium

## half

Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types.

- https://crates.io/crates/half
- https://github.com/starkat99/half-rs

## semver

Parser and evaluator for Cargo\'s flavor of Semantic Versioning

- https://crates.io/crates/semver
- https://docs.rs/semver
- https://github.com/dtolnay/semver

## ciborium

serde implementation of CBOR using ciborium-basic

- https://crates.io/crates/ciborium
- https://github.com/enarx/ciborium
- https://github.com/enarx/ciborium

## ahash

A non-cryptographic hash function using AES-NI for high performance

- https://crates.io/crates/ahash
- https://docs.rs/ahash
- https://github.com/tkaitchuck/ahash

## num-bigint

Big integer implementation for Rust

- https://crates.io/crates/num-bigint
- https://github.com/rust-num/num-bigint
- https://docs.rs/num-bigint
- https://github.com/rust-num/num-bigint

## crossbeam-utils

Utilities for concurrent programming

- https://crates.io/crates/crossbeam-utils
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-utils
- https://github.com/crossbeam-rs/crossbeam

## either

The enum `Either` with variants `Left` and `Right` is a general purpose sum type with two cases.

- https://crates.io/crates/either
- https://docs.rs/either/1/
- https://github.com/bluss/either

## macaddr

MAC address types

- https://crates.io/crates/macaddr
- https://github.com/svartalf/rust-macaddr

## der

Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690.

- https://crates.io/crates/der
- https://github.com/RustCrypto/formats/tree/master/der

## tinyvec

`tinyvec` provides 100% safe vec-like data structures.

- https://crates.io/crates/tinyvec
- https://github.com/Lokathor/tinyvec

## sec1

Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys (also described in RFC5915) as well as the Elliptic-Curve-Point-to-Octet-String and Octet-String-to-Elliptic Curve-Point encoding algorithms.

- https://crates.io/crates/sec1
- https://github.com/RustCrypto/formats/tree/master/sec1

## pkcs8

Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208).

- https://crates.io/crates/pkcs8
- https://github.com/RustCrypto/formats/tree/master/pkcs8

## pkcs1

Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017).

- https://crates.io/crates/pkcs1
- https://github.com/RustCrypto/formats/tree/master/pkcs1

## slab

Pre-allocated storage for a uniform data type

- https://crates.io/crates/slab
- https://github.com/tokio-rs/slab

## const-oid

Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard as defined in ITU X.660, with support for BER/DER encoding/decoding as well as heapless no_std (i.e. embedded) support

- https://crates.io/crates/const-oid
- https://docs.rs/const-oid
- https://github.com/RustCrypto/formats/tree/master/const-oid

## hashbrown

A Rust port of Google\'s SwissTable hash map

- https://crates.io/crates/hashbrown
- https://github.com/rust-lang/hashbrown

## crossbeam-channel

Multi-producer multi-consumer channels for message passing

- https://crates.io/crates/crossbeam-channel
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-channel
- https://github.com/crossbeam-rs/crossbeam

# Encoding

## serde

A generic serialization/deserialization framework

- https://crates.io/crates/serde
- https://serde.rs
- https://docs.rs/serde
- https://github.com/serde-rs/serde

## der_derive

Custom derive support for the `der` crate\'s `Choice` and `Sequence` traits

- https://crates.io/crates/der_derive
- https://docs.rs/der
- https://github.com/RustCrypto/formats/tree/master/der/derive

## unicode-bidi

Implementation of the Unicode Bidirectional Algorithm

- https://crates.io/crates/unicode-bidi
- https://docs.rs/unicode-bidi/
- https://github.com/servo/unicode-bidi

## serde_cbor

CBOR support for serde.

- https://crates.io/crates/serde_cbor
- https://github.com/pyfisch/cbor

## spki

X.509 Subject Public Key Info types describing public keys as well as their associated AlgorithmIdentifiers (i.e. OIDs).

- https://crates.io/crates/spki
- https://github.com/RustCrypto/formats/tree/master/spki

## url

URL library for Rust, based on the WHATWG URL Standard

- https://crates.io/crates/url
- https://docs.rs/url
- https://github.com/servo/rust-url

## x509-cert

Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280.

- https://crates.io/crates/x509-cert
- https://github.com/RustCrypto/formats/tree/master/x509-cert

## ciborium-ll

Low-level CBOR codec primitives

- https://crates.io/crates/ciborium-ll/0.2.0
- https://github.com/enarx/ciborium
- https://github.com/enarx/ciborium

## csv-core

Bare bones CSV parsing with no_std support.

- https://crates.io/crates/csv-core
- https://github.com/BurntSushi/rust-csv
- https://docs.rs/csv-core
- https://github.com/BurntSushi/rust-csv

## bstr

A string type that is not required to be valid UTF-8.

- https://crates.io/crates/bstr
- https://github.com/BurntSushi/bstr
- https://docs.rs/bstr
- https://github.com/BurntSushi/bstr

## half

Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types.

- https://crates.io/crates/half
- https://github.com/starkat99/half-rs

## ciborium

serde implementation of CBOR using ciborium-basic

- https://crates.io/crates/ciborium
- https://github.com/enarx/ciborium
- https://github.com/enarx/ciborium

## base64

encodes and decodes base64 as bytes or utf8

- https://crates.io/crates/base64
- https://docs.rs/base64
- https://github.com/marshallpierce/rust-base64

## serde_json

A JSON serialization file format

- https://crates.io/crates/serde_json
- https://docs.serde.rs/serde_json/
- https://github.com/serde-rs/json

## der

Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690.

- https://crates.io/crates/der
- https://github.com/RustCrypto/formats/tree/master/der

## sec1

Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys (also described in RFC5915) as well as the Elliptic-Curve-Point-to-Octet-String and Octet-String-to-Elliptic Curve-Point encoding algorithms.

- https://crates.io/crates/sec1
- https://github.com/RustCrypto/formats/tree/master/sec1

## os_str_bytes

()

- https://crates.io/crates/os_str_bytes
- https://github.com/dylni/os_str_bytes

## byteorder

Library for reading/writing numbers in big-endian and little-endian.

- https://crates.io/crates/byteorder
- https://github.com/BurntSushi/byteorder
- https://docs.rs/byteorder
- https://github.com/BurntSushi/byteorder

## hex

Encoding and decoding data into/from hexadecimal representation.

- https://crates.io/crates/hex
- https://docs.rs/hex/
- https://github.com/KokaKiwi/rust-hex

## csv

Fast CSV parsing with support for serde.

- https://crates.io/crates/csv
- https://github.com/BurntSushi/rust-csv
- http://burntsushi.net/rustdoc/csv/
- https://github.com/BurntSushi/rust-csv

## pkcs8

Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208).

- https://crates.io/crates/pkcs8
- https://github.com/RustCrypto/formats/tree/master/pkcs8

## pkcs1

Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017).

- https://crates.io/crates/pkcs1
- https://github.com/RustCrypto/formats/tree/master/pkcs1

## const-oid

Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard as defined in ITU X.660, with support for BER/DER encoding/decoding as well as heapless no_std (i.e. embedded) support

- https://crates.io/crates/const-oid
- https://docs.rs/const-oid
- https://github.com/RustCrypto/formats/tree/master/const-oid

# Parser implementations

## sec1

Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys (also described in RFC5915) as well as the Elliptic-Curve-Point-to-Octet-String and Octet-String-to-Elliptic Curve-Point encoding algorithms.

- https://crates.io/crates/sec1
- https://github.com/RustCrypto/formats/tree/master/sec1

## der_derive

Custom derive support for the `der` crate\'s `Choice` and `Sequence` traits

- https://crates.io/crates/der_derive
- https://docs.rs/der
- https://github.com/RustCrypto/formats/tree/master/der/derive

## csv-core

Bare bones CSV parsing with no_std support.

- https://crates.io/crates/csv-core
- https://github.com/BurntSushi/rust-csv
- https://docs.rs/csv-core
- https://github.com/BurntSushi/rust-csv

## litrs

Parse and inspect Rust literals (i.e. tokens in the Rust programming language representing fixed values). Particularly useful for proc macros, but can also be used outside of a proc-macro context.

- https://crates.io/crates/litrs
- https://docs.rs/litrs/
- https://github.com/LukasKalbertodt/litrs/

## csv

Fast CSV parsing with support for serde.

- https://crates.io/crates/csv
- https://github.com/BurntSushi/rust-csv
- http://burntsushi.net/rustdoc/csv/
- https://github.com/BurntSushi/rust-csv

## x509-parser

Parser for the X.509 v3 format (RFC 5280 certificates)

- https://crates.io/crates/x509-parser
- https://github.com/rusticata/x509-parser
- https://github.com/rusticata/x509-parser.git

## pkcs8

Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208).

- https://crates.io/crates/pkcs8
- https://github.com/RustCrypto/formats/tree/master/pkcs8

## pkcs1

Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017).

- https://crates.io/crates/pkcs1
- https://github.com/RustCrypto/formats/tree/master/pkcs1

## der-parser

Parser/encoder for ASN.1 BER/DER data

- https://crates.io/crates/der-parser
- https://github.com/rusticata/der-parser
- https://github.com/rusticata/der-parser.git

## syn

Parser for Rust source code

- https://crates.io/crates/syn
- https://docs.rs/syn
- https://github.com/dtolnay/syn

## shlex

Split a string into shell words, like Python\'s shlex.

- https://crates.io/crates/shlex
- https://github.com/comex/rust-shlex

## serde_json

A JSON serialization file format

- https://crates.io/crates/serde_json
- https://docs.serde.rs/serde_json/
- https://github.com/serde-rs/json

## uuid

A library to generate and parse UUIDs.

- https://crates.io/crates/uuid
- https://github.com/uuid-rs/uuid
- https://docs.rs/uuid
- https://github.com/uuid-rs/uuid

## const-oid

Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard as defined in ITU X.660, with support for BER/DER encoding/decoding as well as heapless no_std (i.e. embedded) support

- https://crates.io/crates/const-oid
- https://docs.rs/const-oid
- https://github.com/RustCrypto/formats/tree/master/const-oid

## url

URL library for Rust, based on the WHATWG URL Standard

- https://crates.io/crates/url
- https://docs.rs/url
- https://github.com/servo/rust-url

## der

Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690.

- https://crates.io/crates/der
- https://github.com/RustCrypto/formats/tree/master/der

# Concurrency

## crossbeam-queue

Concurrent queues

- https://crates.io/crates/crossbeam-queue
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-queue
- https://github.com/crossbeam-rs/crossbeam

## parking_lot_core

An advanced API for creating custom synchronization primitives.

- https://crates.io/crates/parking_lot_core
- https://github.com/Amanieu/parking_lot

## rayon-core

Core APIs for Rayon

- https://crates.io/crates/rayon-core
- https://docs.rs/rayon/
- https://github.com/rayon-rs/rayon

## crossbeam-epoch

Epoch-based garbage collection

- https://crates.io/crates/crossbeam-epoch
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-epoch
- https://github.com/crossbeam-rs/crossbeam

## parking_lot

More compact and efficient implementations of the standard synchronization primitives.

- https://crates.io/crates/parking_lot
- https://github.com/Amanieu/parking_lot

## lock_api

Wrappers to create fully-featured Mutex and RwLock types. Compatible with no_std.

- https://crates.io/crates/lock_api
- https://github.com/Amanieu/parking_lot

## crossbeam-utils

Utilities for concurrent programming

- https://crates.io/crates/crossbeam-utils
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-utils
- https://github.com/crossbeam-rs/crossbeam

## crossbeam-deque

Concurrent work-stealing deque

- https://crates.io/crates/crossbeam-deque
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-deque
- https://github.com/crossbeam-rs/crossbeam

## rayon

Simple work-stealing parallelism for Rust

- https://crates.io/crates/rayon
- https://docs.rs/rayon/
- https://github.com/rayon-rs/rayon

## crossbeam-channel

Multi-producer multi-consumer channels for message passing

- https://crates.io/crates/crossbeam-channel
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-channel
- https://github.com/crossbeam-rs/crossbeam

# Rust patterns

## peeking_take_while

Like `Iterator::take_while`, but calls the predicate on a peeked value. This allows you to use `Iterator::by_ref` and `Iterator::take_while` together, and still get the first value for which the `take_while` predicate returned false after dropping the `by_ref`.

- https://crates.io/crates/peeking_take_while
- https://github.com/fitzgen/peeking_take_while

## once_cell

Single assignment cells and lazy values.

- https://crates.io/crates/once_cell
- https://docs.rs/once_cell
- https://github.com/matklad/once_cell

## lazy_static

A macro for declaring lazily evaluated statics in Rust.

- https://crates.io/crates/lazy_static
- https://docs.rs/lazy_static
- https://github.com/rust-lang-nursery/lazy-static.rs

## anyhow

Flexible concrete Error type built on std::error::Error

- https://crates.io/crates/anyhow
- https://docs.rs/anyhow
- https://github.com/dtolnay/anyhow

## os_str_bytes

()

- https://crates.io/crates/os_str_bytes
- https://github.com/dylni/os_str_bytes

## merge

Merge multiple values into one

- https://crates.io/crates/merge
- https://git.sr.ht/~ireas/merge-rs

## pin-project-lite

A lightweight version of pin-project written with declarative macros.

- https://crates.io/crates/pin-project-lite
- https://github.com/taiki-e/pin-project-lite

## enumn

Convert number to enum

- https://crates.io/crates/enumn
- https://docs.rs/enumn
- https://github.com/dtolnay/enumn

## static_assertions

Compile-time assertions to ensure that invariants are met.

- https://crates.io/crates/static_assertions
- https://github.com/nvzqz/static-assertions-rs
- https://docs.rs/static_assertions/
- https://github.com/nvzqz/static-assertions-rs

## scopeguard

A RAII scope guard that will run a given closure when it goes out of scope, even if the code between panics (assuming unwinding panic).  Defines the macros `defer!`, `defer_on_unwind!`, `defer_on_success!` as shorthands for guards with one of the implemented strategies.

- https://crates.io/crates/scopeguard
- https://docs.rs/scopeguard/
- https://github.com/bluss/scopeguard

## merge_derive

Derive macro for the merge::Merge trait

- https://crates.io/crates/merge_derive
- https://git.sr.ht/~ireas/merge-rs/tree/master/merge_derive

## thiserror

derive(Error)

- https://crates.io/crates/thiserror
- https://docs.rs/thiserror
- https://github.com/dtolnay/thiserror

## bencher

A port of the libtest (unstable Rust) benchmark runner to Rust stable releases. Supports running benchmarks and filtering based on the name. Benchmark execution works exactly the same way and no more (caveat: black_box is still missing!).

- https://crates.io/crates/bencher
- https://docs.rs/bencher/
- https://github.com/bluss/bencher/

## itertools

Extra iterator adaptors, iterator methods, free functions, and macros.

- https://crates.io/crates/itertools
- https://docs.rs/itertools/
- https://github.com/rust-itertools/itertools

## pin-project

A crate for safe and ergonomic pin-projection.

- https://crates.io/crates/pin-project
- https://github.com/taiki-e/pin-project

## pin-project-internal

Implementation detail of the `pin-project` crate.

- https://crates.io/crates/pin-project-internal
- https://github.com/taiki-e/pin-project

# Embedded development

## oorandom

A tiny, robust PRNG implementation.

- https://crates.io/crates/oorandom
- https://sr.ht/~icefox/oorandom/

## ciborium

serde implementation of CBOR using ciborium-basic

- https://crates.io/crates/ciborium
- https://github.com/enarx/ciborium
- https://github.com/enarx/ciborium

## ciborium-ll

Low-level CBOR codec primitives

- https://crates.io/crates/ciborium-ll/0.2.0
- https://github.com/enarx/ciborium
- https://github.com/enarx/ciborium

## aarch64-paging

A library to manipulate AArch64 VMSA EL1 page tables.

- https://crates.io/crates/aarch64-paging
- https://github.com/google/aarch64-paging

## psci

Functions and constants for the Arm Power State Coordination Interface (PSCI) 1.1 on aarch64.

- https://crates.io/crates/psci
- https://github.com/google/psci

## ciborium-io

Simplified Read/Write traits for no_std usage

- https://crates.io/crates/ciborium-io/0.2.0
- https://github.com/enarx/ciborium
- https://github.com/enarx/ciborium

## gdbstub

An implementation of the GDB Remote Serial Protocol in Rust

- https://crates.io/crates/gdbstub
- https://github.com/daniel5151/gdbstub
- https://docs.rs/gdbstub
- https://github.com/daniel5151/gdbstub

## gdbstub_arch

Implementations of `gdbstub::arch::Arch` for various architectures.

- https://crates.io/crates/gdbstub_arch
- https://github.com/daniel5151/gdbstub
- https://docs.rs/gdbstub_arch
- https://github.com/daniel5151/gdbstub

## managed

An interface for logically owning objects, whether or not heap allocation is available.

- https://crates.io/crates/managed
- https://github.com/m-labs/rust-managed
- https://docs.rs/managed/
- https://github.com/m-labs/rust-managed.git

# Emulators

## gdbstub

An implementation of the GDB Remote Serial Protocol in Rust

- https://crates.io/crates/gdbstub
- https://github.com/daniel5151/gdbstub
- https://docs.rs/gdbstub
- https://github.com/daniel5151/gdbstub

## gdbstub_arch

Implementations of `gdbstub::arch::Arch` for various architectures.

- https://crates.io/crates/gdbstub_arch
- https://github.com/daniel5151/gdbstub
- https://docs.rs/gdbstub_arch
- https://github.com/daniel5151/gdbstub

# Memory management

## once_cell

Single assignment cells and lazy values.

- https://crates.io/crates/once_cell
- https://docs.rs/once_cell
- https://github.com/matklad/once_cell

## lazy_static

A macro for declaring lazily evaluated statics in Rust.

- https://crates.io/crates/lazy_static
- https://docs.rs/lazy_static
- https://github.com/rust-lang-nursery/lazy-static.rs

## zeroize_derive

Custom derive support for zeroize

- https://crates.io/crates/zeroize_derive
- https://github.com/RustCrypto/utils/tree/master/zeroize/derive

## zeroize

Securely zero memory while avoiding compiler optimizations.

- https://crates.io/crates/zeroize
- https://github.com/RustCrypto/utils/tree/master/zeroize

## slab

Pre-allocated storage for a uniform data type

- https://crates.io/crates/slab
- https://github.com/tokio-rs/slab

## crossbeam-epoch

Epoch-based garbage collection

- https://crates.io/crates/crossbeam-epoch
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-epoch
- https://github.com/crossbeam-rs/crossbeam

# Network programming

## octets

Zero-copy abstraction for parsing and constructing network packets

- https://crates.io/crates/octets
- https://github.com/cloudflare/quiche

## tokio

An event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications.

- https://crates.io/crates/tokio
- https://tokio.rs
- https://github.com/tokio-rs/tokio

## grpcio-sys

FFI bindings to gRPC c core library

- https://crates.io/crates/grpcio-sys
- https://github.com/tikv/grpc-rs
- https://docs.rs/grpcio-sys
- https://github.com/tikv/grpc-rs

## grpcio-compiler

gRPC compiler for grpcio

- https://crates.io/crates/grpcio-compiler
- https://github.com/tikv/grpc-rs
- https://docs.rs/grpcio-compiler
- https://github.com/tikv/grpc-rs

## bytes

Types and traits for working with bytes

- https://crates.io/crates/bytes
- https://github.com/tokio-rs/bytes

## grpcio

The rust language implementation of gRPC, base on the gRPC c core library.

- https://crates.io/crates/grpcio
- https://github.com/tikv/grpc-rs
- https://docs.rs/grpcio
- https://github.com/tikv/grpc-rs

## gdbstub

An implementation of the GDB Remote Serial Protocol in Rust

- https://crates.io/crates/gdbstub
- https://github.com/daniel5151/gdbstub
- https://docs.rs/gdbstub
- https://github.com/daniel5151/gdbstub

## quiche

\ud83e\udd67 Savoury implementation of the QUIC transport protocol and HTTP/3

- https://crates.io/crates/quiche
- https://github.com/cloudflare/quiche

## macaddr

MAC address types

- https://crates.io/crates/macaddr
- https://github.com/svartalf/rust-macaddr

# External FFI bindings

## jni-sys

Rust definitions corresponding to jni.h

- https://crates.io/crates/jni-sys
- https://docs.rs/jni-sys/0.3.0/jni_sys
- https://github.com/sfackler/rust-jni-sys

## bindgen-cli

Automatically generates Rust FFI bindings to C and C++ libraries.

- https://crates.io/crates/bindgen-cli
- https://rust-lang.github.io/rust-bindgen/
- https://docs.rs/bindgen
- https://github.com/rust-lang/rust-bindgen

## android_log-sys

FFI bindings to Android log Library.

- https://crates.io/crates/android_log-sys
- https://docs.rs/android_log-sys
- https://github.com/nercury/android_log-sys-rs

## grpcio-sys

FFI bindings to gRPC c core library

- https://crates.io/crates/grpcio-sys
- https://github.com/tikv/grpc-rs
- https://docs.rs/grpcio-sys
- https://github.com/tikv/grpc-rs

## libc

Raw FFI bindings to platform libraries like libc.

- https://crates.io/crates/libc
- https://github.com/rust-lang/libc
- https://docs.rs/libc/
- https://github.com/rust-lang/libc

## bindgen

Automatically generates Rust FFI bindings to C and C++ libraries.

- https://crates.io/crates/bindgen
- https://rust-lang.github.io/rust-bindgen/
- https://docs.rs/bindgen
- https://github.com/rust-lang/rust-bindgen

## libsqlite3-sys

Native bindings to the libsqlite3 library

- https://crates.io/crates/libsqlite3-sys
- https://github.com/rusqlite/rusqlite

## libz-sys

Low-level bindings to the system libz library (also known as zlib).

- https://crates.io/crates/libz-sys
- https://github.com/rust-lang/libz-sys

# Text processing

## aho-corasick

Fast multiple substring searching.

- https://crates.io/crates/aho-corasick
- https://github.com/BurntSushi/aho-corasick
- https://github.com/BurntSushi/aho-corasick

## unicode-bidi

Implementation of the Unicode Bidirectional Algorithm

- https://crates.io/crates/unicode-bidi
- https://docs.rs/unicode-bidi/
- https://github.com/servo/unicode-bidi

## bstr

A string type that is not required to be valid UTF-8.

- https://crates.io/crates/bstr
- https://github.com/BurntSushi/bstr
- https://docs.rs/bstr
- https://github.com/BurntSushi/bstr

## regex-automata

Automata construction and matching using regular expressions.

- https://crates.io/crates/regex-automata
- https://github.com/BurntSushi/regex-automata
- https://docs.rs/regex-automata
- https://github.com/BurntSushi/regex-automata

## regex

An implementation of regular expressions for Rust. This implementation uses finite automata and guarantees linear time matching on all inputs.

- https://crates.io/crates/regex
- https://github.com/rust-lang/regex
- https://docs.rs/regex
- https://github.com/rust-lang/regex

## textwrap

Library for word wrapping, indenting, and dedenting strings. Has optional support for Unicode and emojis as well as machine hyphenation.

- https://crates.io/crates/textwrap
- https://docs.rs/textwrap/
- https://github.com/mgeisler/textwrap

# Algorithms

## rand_chacha

ChaCha random number generator

- https://crates.io/crates/rand_chacha
- https://rust-random.github.io/book
- https://docs.rs/rand_chacha
- https://github.com/rust-random/rand

## oorandom

A tiny, robust PRNG implementation.

- https://crates.io/crates/oorandom
- https://sr.ht/~icefox/oorandom/

## rand

Random number generators and other randomness functionality.

- https://crates.io/crates/rand
- https://rust-random.github.io/book
- https://docs.rs/rand
- https://github.com/rust-random/rand

## ahash

A non-cryptographic hash function using AES-NI for high performance

- https://crates.io/crates/ahash
- https://docs.rs/ahash
- https://github.com/tkaitchuck/ahash

## num-integer

Integer traits and functions

- https://crates.io/crates/num-integer
- https://github.com/rust-num/num-integer
- https://docs.rs/num-integer
- https://github.com/rust-num/num-integer

## rand_xorshift

Xorshift random number generator

- https://crates.io/crates/rand_xorshift
- https://rust-random.github.io/book
- https://docs.rs/rand_xorshift
- https://github.com/rust-random/rngs

## rand_core

Core random number generator traits and tools for implementation.

- https://crates.io/crates/rand_core
- https://rust-random.github.io/book
- https://docs.rs/rand_core
- https://github.com/rust-random/rand

## num-bigint

Big integer implementation for Rust

- https://crates.io/crates/num-bigint
- https://github.com/rust-num/num-bigint
- https://docs.rs/num-bigint
- https://github.com/rust-num/num-bigint

## fallible-iterator

Fallible iterator traits

- https://crates.io/crates/fallible-iterator
- https://github.com/sfackler/rust-fallible-iterator

## crossbeam-utils

Utilities for concurrent programming

- https://crates.io/crates/crossbeam-utils
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-utils
- https://github.com/crossbeam-rs/crossbeam

## crossbeam-deque

Concurrent work-stealing deque

- https://crates.io/crates/crossbeam-deque
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-deque
- https://github.com/crossbeam-rs/crossbeam

## itertools

Extra iterator adaptors, iterator methods, free functions, and macros.

- https://crates.io/crates/itertools
- https://docs.rs/itertools/
- https://github.com/rust-itertools/itertools

## num-traits

Numeric traits for generic mathematics

- https://crates.io/crates/num-traits
- https://github.com/rust-num/num-traits
- https://docs.rs/num-traits
- https://github.com/rust-num/num-traits

## fxhash

A fast, non-secure, hashing algorithm derived from an internal hasher used in FireFox and Rustc.

- https://crates.io/crates/fxhash
- https://docs.rs/fxhash
- https://github.com/cbreeden/fxhash

## crossbeam-channel

Multi-producer multi-consumer channels for message passing

- https://crates.io/crates/crossbeam-channel
- https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-channel
- https://github.com/crossbeam-rs/crossbeam

# Parsing tools

## pest

The Elegant Parser

- https://crates.io/crates/pest
- https://pest.rs/
- https://docs.rs/pest
- https://github.com/pest-parser/pest

## minimal-lexical

Fast float parsing conversion routines.

- https://crates.io/crates/minimal-lexical
- https://docs.rs/minimal-lexical
- https://github.com/Alexhuszagh/minimal-lexical

## pest_meta

pest meta language parser and validator

- https://crates.io/crates/pest_meta
- https://pest.rs/
- https://docs.rs/pest
- https://github.com/pest-parser/pest

## pest_generator

pest code generator

- https://crates.io/crates/pest_generator
- https://pest.rs/
- https://docs.rs/pest
- https://github.com/pest-parser/pest

## byteorder

Library for reading/writing numbers in big-endian and little-endian.

- https://crates.io/crates/byteorder
- https://github.com/BurntSushi/byteorder
- https://docs.rs/byteorder
- https://github.com/BurntSushi/byteorder

## ciborium-ll

Low-level CBOR codec primitives

- https://crates.io/crates/ciborium-ll/0.2.0
- https://github.com/enarx/ciborium
- https://github.com/enarx/ciborium

## nom

A byte-oriented, zero-copy, parser combinators library

- https://crates.io/crates/nom
- https://docs.rs/nom
- https://github.com/Geal/nom

## combine

Fast parser combinators on arbitrary streams with zero-copy support.

- https://crates.io/crates/combine
- https://docs.rs/combine
- https://github.com/Marwes/combine

## rusticata-macros

Helper macros for Rusticata

- https://crates.io/crates/rusticata-macros
- https://github.com/rusticata/rusticata-macros
- https://github.com/rusticata/rusticata-macros.git

## xml-rs

An XML library in pure Rust

- https://crates.io/crates/xml-rs
- http://docs.rs/xml-rs/
- https://github.com/netvl/xml-rs

## ciborium

serde implementation of CBOR using ciborium-basic

- https://crates.io/crates/ciborium
- https://github.com/enarx/ciborium
- https://github.com/enarx/ciborium

## pest_derive

pest\'s derive macro

- https://crates.io/crates/pest_derive
- https://pest.rs/
- https://docs.rs/pest
- https://github.com/pest-parser/pest

# Development tools::Testing

## serde_test

Token De/Serializer for testing De/Serialize implementations

- https://crates.io/crates/serde_test
- https://serde.rs
- https://docs.rs/serde_test
- https://github.com/serde-rs/serde

## static_assertions

Compile-time assertions to ensure that invariants are met.

- https://crates.io/crates/static_assertions
- https://github.com/nvzqz/static-assertions-rs
- https://docs.rs/static_assertions/
- https://github.com/nvzqz/static-assertions-rs

## derive_arbitrary

Derives arbitrary traits

- https://crates.io/crates/derive_arbitrary
- https://docs.rs/arbitrary/
- https://github.com/rust-fuzz/arbitrary

## quickcheck

Automatic property based testing with shrinking.

- https://crates.io/crates/quickcheck
- https://github.com/BurntSushi/quickcheck
- https://docs.rs/quickcheck
- https://github.com/BurntSushi/quickcheck

## arbitrary

The trait for generating structured data from unstructured data

- https://crates.io/crates/arbitrary
- https://docs.rs/arbitrary/
- https://github.com/rust-fuzz/arbitrary/

# Value formatting

## itoa

Fast integer primitive to string conversion

- https://crates.io/crates/itoa
- https://docs.rs/itoa
- https://github.com/dtolnay/itoa

## ryu

Fast floating point to string conversion

- https://crates.io/crates/ryu
- https://docs.rs/ryu
- https://github.com/dtolnay/ryu

# API bindings

## libloading

Bindings around the platform\'s dynamic library loading primitives with greatly improved memory safety.

- https://crates.io/crates/libloading
- https://docs.rs/libloading/
- https://github.com/nagisa/rust_libloading/

## openssl

OpenSSL bindings

- https://crates.io/crates/openssl
- https://github.com/sfackler/rust-openssl
- https://github.com/sfackler/rust-openssl

## flate2

DEFLATE compression and decompression exposed as Read/BufRead/Write streams. Supports miniz_oxide, miniz.c, and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.

- https://crates.io/crates/flate2
- https://github.com/rust-lang/flate2-rs
- https://docs.rs/flate2
- https://github.com/rust-lang/flate2-rs

## jni

Rust bindings to the JNI

- https://crates.io/crates/jni
- https://docs.rs/jni
- https://github.com/jni-rs/jni-rs

## android_logger

A logging implementation for `log` which hooks to android log output.

- https://crates.io/crates/android_logger
- https://github.com/Nercury/android_logger-rs

# Filesystem

## remove_dir_all

Reliable and fast directory removal functions.

- https://crates.io/crates/remove_dir_all
- https://github.com/XAMPPRocky/remove_dir_all.git

## which

A Rust equivalent of Unix command \

- https://crates.io/crates/which
- https://docs.rs/which/
- https://github.com/harryfei/which-rs.git

## glob

Support for matching file paths against Unix shell style patterns.

- https://crates.io/crates/glob
- https://github.com/rust-lang/glob
- https://docs.rs/glob/0.3.1
- https://github.com/rust-lang/glob

## walkdir

Recursively walk a directory.

- https://crates.io/crates/walkdir
- https://github.com/BurntSushi/walkdir
- https://docs.rs/walkdir/
- https://github.com/BurntSushi/walkdir

# Operating systems

## shared_child

a library for using child processes from multiple threads

- https://crates.io/crates/shared_child
- https://docs.rs/shared_child
- https://github.com/oconnor663/shared_child.rs

## getrandom

A small cross-platform library for retrieving random data from system source

- https://crates.io/crates/getrandom
- https://docs.rs/getrandom
- https://github.com/rust-random/getrandom

## os_str_bytes

()

- https://crates.io/crates/os_str_bytes
- https://github.com/dylni/os_str_bytes

## zeroize_derive

Custom derive support for zeroize

- https://crates.io/crates/zeroize_derive
- https://github.com/RustCrypto/utils/tree/master/zeroize/derive

## which

A Rust equivalent of Unix command \

- https://crates.io/crates/which
- https://docs.rs/which/
- https://github.com/harryfei/which-rs.git

## zeroize

Securely zero memory while avoiding compiler optimizations.

- https://crates.io/crates/zeroize
- https://github.com/RustCrypto/utils/tree/master/zeroize

## libc

Raw FFI bindings to platform libraries like libc.

- https://crates.io/crates/libc
- https://github.com/rust-lang/libc
- https://docs.rs/libc/
- https://github.com/rust-lang/libc

# Development tools::Procedural macro helpers

## unicode-ident

Determine whether characters have the XID_Start or XID_Continue properties according to Unicode Standard Annex #31

- https://crates.io/crates/unicode-ident
- https://docs.rs/unicode-ident
- https://github.com/dtolnay/unicode-ident

## proc-macro2

A substitute implementation of the compiler\'s `proc_macro` API to decouple token-based libraries from the procedural macro use case.

- https://crates.io/crates/proc-macro2
- https://docs.rs/proc-macro2
- https://github.com/dtolnay/proc-macro2

## clap_derive

Parse command line argument by defining a struct, derive crate.

- https://crates.io/crates/clap_derive
- https://github.com/clap-rs/clap/tree/master/clap_derive

## litrs

Parse and inspect Rust literals (i.e. tokens in the Rust programming language representing fixed values). Particularly useful for proc macros, but can also be used outside of a proc-macro context.

- https://crates.io/crates/litrs
- https://docs.rs/litrs/
- https://github.com/LukasKalbertodt/litrs/

## proc-macro-error

Almost drop-in replacement to panics in proc-macros

- https://crates.io/crates/proc-macro-error
- https://gitlab.com/CreepySkeleton/proc-macro-error

## proc-macro-hack

Procedural macros in expression position

- https://crates.io/crates/proc-macro-hack
- https://github.com/dtolnay/proc-macro-hack

## syn

Parser for Rust source code

- https://crates.io/crates/syn
- https://docs.rs/syn
- https://github.com/dtolnay/syn

## syn-mid

Providing the features between \

- https://crates.io/crates/syn-mid
- https://docs.rs/syn-mid
- https://github.com/taiki-e/syn-mid

## quote

Quasi-quoting macro quote!(...)

- https://crates.io/crates/quote
- https://docs.rs/quote/
- https://github.com/dtolnay/quote

# Command-line interface

## os_str_bytes

()

- https://crates.io/crates/os_str_bytes
- https://github.com/dylni/os_str_bytes

## clap_derive

Parse command line argument by defining a struct, derive crate.

- https://crates.io/crates/clap_derive
- https://github.com/clap-rs/clap/tree/master/clap_derive

## clap_lex

Minimal, flexible command line parser.

- https://crates.io/crates/clap_lex
- https://github.com/clap-rs/clap/tree/master/clap_lex

## structopt-derive

Parse command line argument by defining a struct, derive crate.

- https://crates.io/crates/structopt-derive
- https://docs.rs/structopt-derive
- https://github.com/TeXitoi/structopt

## clap

A simple to use, efficient, and full-featured Command Line Argument Parser

- https://crates.io/crates/clap
- https://github.com/clap-rs/clap

## shlex

Split a string into shell words, like Python\'s shlex.

- https://crates.io/crates/shlex
- https://github.com/comex/rust-shlex

## textwrap

Library for word wrapping, indenting, and dedenting strings. Has optional support for Unicode and emojis as well as machine hyphenation.

- https://crates.io/crates/textwrap
- https://docs.rs/textwrap/
- https://github.com/mgeisler/textwrap

## structopt

Parse command line argument by defining a struct.

- https://crates.io/crates/structopt
- https://docs.rs/structopt
- https://github.com/TeXitoi/structopt

# Hardware support

## num_cpus

Get the number of CPUs on a machine.

- https://crates.io/crates/num_cpus
- https://docs.rs/num_cpus
- https://github.com/seanmonstar/num_cpus

## psci

Functions and constants for the Arm Power State Coordination Interface (PSCI) 1.1 on aarch64.

- https://crates.io/crates/psci
- https://github.com/google/psci

## aarch64-paging

A library to manipulate AArch64 VMSA EL1 page tables.

- https://crates.io/crates/aarch64-paging
- https://github.com/google/aarch64-paging

## virtio-drivers

VirtIO guest drivers.

- https://crates.io/crates/virtio-drivers
- https://github.com/rcore-os/virtio-drivers

# Web programming

## url

URL library for Rust, based on the WHATWG URL Standard

- https://crates.io/crates/url
- https://docs.rs/url
- https://github.com/servo/rust-url

# Rendering::Graphics APIs

## vulkano

Safe wrapper for the Vulkan graphics API

- https://crates.io/crates/vulkano
- https://vulkano.rs
- https://docs.rs/vulkano
- https://github.com/vulkano-rs/vulkano

# Development tools

## document-features

Extract documentation for the feature flags from comments in Cargo.toml

- https://crates.io/crates/document-features
- https://slint-ui.com
- https://github.com/slint-ui/document-features

## paste

Macros for all your token pasting needs

- https://crates.io/crates/paste
- https://github.com/dtolnay/paste

## remain

Compile-time checks that an enum, struct, or match is written in sorted order.

- https://crates.io/crates/remain
- https://docs.rs/remain
- https://github.com/dtolnay/remain

# Science

## num-traits

Numeric traits for generic mathematics

- https://crates.io/crates/num-traits
- https://github.com/rust-num/num-traits
- https://docs.rs/num-traits
- https://github.com/rust-num/num-traits

## num-derive

Numeric syntax extensions

- https://crates.io/crates/num-derive
- https://github.com/rust-num/num-derive
- https://docs.rs/num-derive
- https://github.com/rust-num/num-derive

## num-bigint

Big integer implementation for Rust

- https://crates.io/crates/num-bigint
- https://github.com/rust-num/num-bigint
- https://docs.rs/num-bigint
- https://github.com/rust-num/num-bigint

## num-integer

Integer traits and functions

- https://crates.io/crates/num-integer
- https://github.com/rust-num/num-integer
- https://docs.rs/num-integer
- https://github.com/rust-num/num-integer

# Operating systems::Unix APIs

## nix

Rust friendly bindings to *nix APIs

- https://crates.io/crates/nix
- https://github.com/nix-rust/nix

## command-fds

A library for passing arbitrary file descriptors when spawning child processes.

- https://crates.io/crates/command-fds
- https://github.com/google/command-fds/

# Development tools::Build Utils

## litrs

Parse and inspect Rust literals (i.e. tokens in the Rust programming language representing fixed values). Particularly useful for proc macros, but can also be used outside of a proc-macro context.

- https://crates.io/crates/litrs
- https://docs.rs/litrs/
- https://github.com/LukasKalbertodt/litrs/

## rustversion

Conditional compilation according to rustc compiler version

- https://crates.io/crates/rustversion
- https://docs.rs/rustversion
- https://github.com/dtolnay/rustversion

# Compression

## flate2

DEFLATE compression and decompression exposed as Read/BufRead/Write streams. Supports miniz_oxide, miniz.c, and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.

- https://crates.io/crates/flate2
- https://github.com/rust-lang/flate2-rs
- https://docs.rs/flate2
- https://github.com/rust-lang/flate2-rs

## libz-sys

Low-level bindings to the system libz library (also known as zlib).

- https://crates.io/crates/libz-sys
- https://github.com/rust-lang/libz-sys

# Development tools::Profiling

## bencher

A port of the libtest (unstable Rust) benchmark runner to Rust stable releases. Supports running benchmarks and filtering based on the name. Benchmark execution works exactly the same way and no more (caveat: black_box is still missing!).

- https://crates.io/crates/bencher
- https://docs.rs/bencher/
- https://github.com/bluss/bencher/

## criterion

Statistics-driven micro-benchmarking library

- https://crates.io/crates/criterion
- https://bheisler.github.io/criterion.rs/book/index.html
- https://github.com/bheisler/criterion.rs

# Development tools::FFI

## bindgen-cli

Automatically generates Rust FFI bindings to C and C++ libraries.

- https://crates.io/crates/bindgen-cli
- https://rust-lang.github.io/rust-bindgen/
- https://docs.rs/bindgen
- https://github.com/rust-lang/rust-bindgen

## os_str_bytes

()

- https://crates.io/crates/os_str_bytes
- https://github.com/dylni/os_str_bytes

## bindgen

Automatically generates Rust FFI bindings to C and C++ libraries.

- https://crates.io/crates/bindgen
- https://rust-lang.github.io/rust-bindgen/
- https://docs.rs/bindgen
- https://github.com/rust-lang/rust-bindgen

# Visualization

## criterion-plot

Criterion\'s plotting library

- https://crates.io/crates/criterion-plot
- https://github.com/bheisler/criterion.rs

## plotters

A Rust drawing library focus on data plotting for both WASM and native applications

- https://crates.io/crates/plotters
- https://plotters-rs.github.io/
- https://github.com/plotters-rs/plotters

# WebAssembly

## uuid

A library to generate and parse UUIDs.

- https://crates.io/crates/uuid
- https://github.com/uuid-rs/uuid
- https://docs.rs/uuid
- https://github.com/uuid-rs/uuid

## plotters

A Rust drawing library focus on data plotting for both WASM and native applications

- https://crates.io/crates/plotters
- https://plotters-rs.github.io/
- https://github.com/plotters-rs/plotters

# Database interfaces

## rusqlite

Ergonomic wrapper for SQLite

- https://crates.io/crates/rusqlite
- http://docs.rs/rusqlite/
- https://github.com/rusqlite/rusqlite

# Date and time

## chrono

Date and time library for Rust

- https://crates.io/crates/chrono
- https://github.com/chronotope/chrono
- https://docs.rs/chrono/
- https://github.com/chronotope/chrono

# Game engines

## glam

A simple and fast 3D math library for games and graphics

- https://crates.io/crates/glam
- https://github.com/bitshifter/glam-rs

# Template engine

## tinytemplate

Simple, lightweight template engine

- https://crates.io/crates/tinytemplate
- https://github.com/bheisler/TinyTemplate

