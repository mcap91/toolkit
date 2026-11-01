---
name: unitask
title: UniTask
url: https://github.com/Cysharp/UniTask
source_url: https://www.instagram.com/reel/DeuQdK6THpz/
source: instagram
category: framework
summary: Cysharp's allocation-free async/await library for Unity — a struct-based UniTask<T> (vs. the heap-allocating Task<T>) that makes Unity's AsyncOperations, Coroutines, and MonoBehaviour/uGUI events awaitable, runs on Unity's PlayerLoop without threads (works on WebGL/wasm), and adds async LINQ (Channel, AsyncReactiveProperty) plus a TaskTracker window for leak detection; commonly used to replace coroutines for timers and sequencing (e.g. day/night cycles); requires Unity 2018.3+ for C# 7.0 task-like builders; 11.3k stars, 1.0k forks; MIT.
tags:
  - unity
  - async-await
  - coroutines
  - csharp
  - performance
  - game-development
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
---

## What it does

UniTask provides an efficient, allocation-free async/await integration for Unity, built around a struct-based `UniTask`/`UniTask<T>` type instead of the heap-allocating `System.Threading.Tasks.Task<T>`. It makes Unity's native asynchronous objects — `AsyncOperation`, `ResourceRequest`, `UnityWebRequestAsyncOperation`, and coroutines — directly awaitable, and exposes MonoBehaviour lifecycle/uGUI events as awaitable or async-enumerable streams via `AsyncTriggers`. Because it runs on Unity's PlayerLoop rather than real OS threads or `SynchronizationContext`, it works on platforms coroutines already support, including WebGL and wasm. It's commonly adopted as a coroutine replacement for game-logic sequencing and timers — e.g. driving day/night cycles or periodic crop-growth timers in async methods instead of `IEnumerator` coroutines.

## Mechanical details

Requires Unity 2018.3+ (C# 7.0's task-like custom async method builder feature); officially supported from Unity 2018.4.13f1 onward. Includes Async LINQ operators (`SelectAwait`, etc.) and `Channel`/`AsyncReactiveProperty` primitives for async data streams, plus a TaskTracker editor window to catch leaked/un-awaited tasks. 11.3k GitHub stars, 1.0k forks. Published by Cysharp, Inc.

## Security

MIT licensed. Local async-scheduling library with no network calls or telemetry.

## Sources

- [GitHub: Cysharp/UniTask](https://github.com/Cysharp/UniTask) — README, feature list, license
- [Instagram reel](https://www.instagram.com/reel/DeuQdK6THpz/) — named the tool as one of eight repos used to build a Claude-assisted farm game (catalog source; no link given in the reel itself)