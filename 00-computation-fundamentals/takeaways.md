# What This Changes in My ML Code

* Think about **where code actually executes**, not just the language I wrote it in.
* Avoid unnecessary Python-level loops for heavy computation; rely on optimized native/vectorized operations.
* Treat **data movement and memory location** as part of performance, especially with CPUs and GPUs.
* Choose threads, processes, or async execution based on whether the workload is **CPU-bound or I/O-bound**.
* When debugging performance, ask: **Where is the computation? Where is the data? What is moving?**