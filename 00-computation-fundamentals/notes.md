# From Source Code to Execution

When I write Python, C++, or any other programming language, the CPU does not understand what I wrote. It understands machine instructions.

So somewhere between my source code and the CPU, there has to be a translation layer.

This is more important for AI/ML than it first appears. When I later work with NumPy, PyTorch, GPUs, multiprocessing, or model training, I am constantly moving between different execution layers. If I understand what is actually running where, performance and memory behavior stop feeling mysterious.

## Compilation vs Runtime Execution

With languages such as C and C++, the traditional model is straightforward: the compiler takes my source code and produces native machine code for a target platform.

That gives me very fast execution because the CPU can execute the generated instructions directly. The tradeoff is that the program is tied to the target architecture, and when I change the source code, I generally need to compile it again.

Python follows a different model, although saying simply "Python is interpreted" hides an important detail.

In CPython, my `.py` source is first compiled into bytecode, and that bytecode is executed by the Python runtime. Other runtimes, such as modern JavaScript engines, may interpret, JIT-compile, or optimize code dynamically. Rust, on the other hand, is primarily an ahead-of-time compiled language and should not be grouped with Python as an interpreted language.

The useful idea is not memorizing whether a language is "compiled" or "interpreted." The useful question is:

> **What does my code become, and who executes that representation?**

That question becomes extremely useful once I start working with performance-sensitive AI/ML systems.

## Why Python Can Feel Slow but NumPy Does Not

A Python loop doing millions of arithmetic operations can be much slower than equivalent native code.

For example:

```python
total = 0

for i in range(10_000_000):
    total += i
```

Here, Python itself is repeatedly managing the loop, objects, dynamic types, and bytecode execution.

But when I write:

```python
import numpy as np

x = np.arange(10_000_000)
y = x * 2
```

the important computation is not happening as ten million individual Python operations.

NumPy exposes a Python interface, but the heavy numerical work is implemented in optimized native code. The same idea appears throughout AI/ML libraries. PyTorch gives me a Python API, but tensor operations can execute inside highly optimized C/C++ and CUDA kernels, including on a GPU.

So I should not make the mistake of thinking:

> "Python is slow, therefore PyTorch is slow."

The better mental model is:

> **Python can be the interface while the expensive computation happens somewhere else.**

This distinction becomes fundamental when I start optimizing ML code.

## Stack and Heap: Where Data Lives

I used to think of the stack as "small data" and the heap as "large data." That is a useful beginner shortcut, but it is not the real distinction.

The better way to think about them is **lifetime and allocation**.

When a function is called, the program needs execution state for that call: local variables, parameters, return information, and other bookkeeping. This is associated with the call stack. When the function returns, that stack frame is naturally removed.

That is why excessive recursion can cause a stack overflow: I keep creating new call frames without allowing the previous ones to disappear.

The heap is different. It is used for dynamically allocated data whose lifetime does not simply follow one function call. Objects can live beyond the function that created them, and references or pointers can be used to access them.

Different languages manage this differently. In C and C++, I may explicitly allocate and free memory. In Python, memory management is handled by the runtime.

The important idea is not "stack is small, heap is big."

It is:

> **Who allocates this data, how long does it need to live, and who is responsible for managing that lifetime?**

That way of thinking becomes useful later when I deal with tensors, large datasets, GPU memory, and memory leaks.

## Process vs Thread

If I launch a Python program, the operating system creates a **process** for it.

A process gets its own protected virtual address space and operating-system resources. This isolation matters because I do not want one program accidentally writing into another program's memory.

Threads exist inside processes.

If a process has multiple threads, those threads generally share the process's memory, including its heap, while each thread maintains its own execution state and stack.

This creates an important tradeoff:

* **Processes** give stronger isolation but require more coordination to communicate.
* **Threads** can communicate through shared memory much more easily, but that shared memory introduces synchronization problems.

For example, if two threads both modify the same variable, their operations can interleave in an unexpected order.

That is a **race condition**.

```text
Thread A: read value -> modify -> write
Thread B:       read value -> modify -> write
```

If both threads read the same old value before either writes the new one, one update can overwrite the other.

So concurrency is not simply "make more threads and go faster." Once memory is shared, I also have to think about ownership, synchronization, and correctness.

## The GIL and Why 8 Cores Do Not Automatically Mean 8 Python Threads

Traditional CPython has a Global Interpreter Lock, commonly called the **GIL**.

In a GIL-enabled CPython interpreter, only one thread at a time can execute Python bytecode within that interpreter. This means creating eight Python threads does not mean eight threads can simultaneously execute Python bytecode across eight CPU cores.

That matters particularly for **CPU-bound Python code**.

If my workload spends most of its time doing Python-level computation, adding more threads may not produce the parallel speedup I expect. There is also overhead from switching between threads and coordinating their work.

But the GIL does not make threads useless.

For **I/O-bound work**, such as waiting for network responses, files, or other external resources, threads can still be useful because the program spends much of its time waiting rather than executing Python bytecode.

Also, native libraries can release the GIL while performing work outside the Python interpreter. This is one reason Python applications can still make effective use of multiple CPU cores through libraries implemented in native code.

Modern CPython also has free-threaded builds that can operate without the traditional GIL, so "Python has a GIL" should not be treated as an absolute rule for every current Python configuration.

## Concurrency Is Not the Same as Parallelism

These two terms are easy to mix up.

**Concurrency** means multiple tasks can make progress during overlapping periods. They do not necessarily execute at exactly the same instant.

**Parallelism** means multiple tasks are actually executing simultaneously using multiple processing resources.

A single CPU core can support concurrency by rapidly switching between tasks. Multiple CPU cores can provide actual parallel execution.

This distinction becomes useful when choosing between threads, processes, asynchronous programming, native code, and GPUs.

## The Mental Model I Want to Keep

Whenever I look at a program, especially an AI/ML program, I want to ask four questions:

1. **Where is my code actually executing?**
2. **Where is my data currently stored?**
3. **Who owns and manages that data?**
4. **What happens when multiple workers try to use it?**

These questions connect concepts that otherwise look unrelated.

Compilation explains how my code becomes executable instructions. The Python runtime explains why Python behaves differently from native code. Stack and heap explain memory lifetime. Processes and threads explain how work is separated or shared. Race conditions explain what can go wrong when that sharing is uncontrolled. The GIL explains one important limitation of traditional CPython threading.

And in AI/ML, these ideas eventually come together in a very practical way: **where the computation runs, where the data lives, and how the data moves can matter just as much as the algorithm itself.**
