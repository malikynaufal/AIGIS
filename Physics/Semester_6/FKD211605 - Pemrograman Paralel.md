---
code: FKD211605
name: Pemrograman Paralel
SKS: 3
semester: 6
department: Informatika/Fisika
tags: [parallel-computing, HPC, GPU, CUDA, openmp, MPI]
created: 2026-07-27
---

# FKD211605 — Pemrograman Paralel

## Course Overview

High-performance computing for physics — parallel algorithms and architectures enabling simulation of large systems that would be impossible on a single core. This course covers multi-core CPU parallelism, GPU computing, and distributed computing, essential for modern physics research.

**Contact Hours:** 3 SKS (1 hour lecture + 2 hours lab per week)
**Prerequisites:** Pemrograman Lanjutan, Analisis Numerik
**Co-requisites:** Simulasi Fisika

---

## 📋 Topics & Outline

### Unit 1: Parallel Computing Foundations (Weeks 1–4)

- **Why parallel computing?** Amdahl's law, GPU revolution, big data in physics

- **Parallel architectures:**
 - Shared memory (multi-core CPU)
 - Distributed memory (cluster computing)
 - **GPU computing:** many simple cores for data parallelism

- **Concurrency vs. parallelism:** threads, processes, tasks

- **Python parallelism:**
 - `multiprocessing` module (separate processes)
 - `threading` (limited by GIL — Global Interpreter Lock)
 - `concurrent.futures` for task parallelism

- **Performance metrics:** speedup, efficiency, scalability

$$ ext{Speedup} = \frac{T_{ext{serial}}}{T_{ext{parallel}}}

$ $

$$ ext{Efficiency} = \frac{ext{Speedup}}{N_{ext{processors}}}

$ $

$$ ext{Amdahl's law: } ext{Speedup}_{\max} = \frac{1}{(1 - p) + \frac{p}{N}}

$ $

Unit 2: Shared-Memory Parallelism (Weeks 5–9)

- **OpenMP:** compiler directives for loop parallelization
 ```c
 #pragma omp parallel for reduction(+:sum)
 for (int i = 0; i < N; i++) {
 sum += a[i] * b[i];
 }
 ```

- **Critical sections** and race conditions

- **Load balancing:** distributing work evenly across threads

- **NumPy vectorization** — Python's "implicit parallelism"

- **Scientific Python parallelism:**
 - `joblib` for embarrassingly parallel loops
 - `dask` for larger-than-memory computation
 - `scipy` for optimized BLAS/LAPACK routines (multi-threaded by default)

### Unit 3: GPU Computing with CUDA (Weeks 10–13)

- **GPU architecture:** SMs, threads, warps, memory hierarchy

- **CUDA programming model:**
 ```python
 from numba import cuda
 @cuda.jit
 def vec_add(a, b, c, N):
 i = cuda.grid(1)
 if i < N:
 c[i] = a[i] + b[i]

 threadsperblock = 256
 blockspergrid = (N + 255) // 256
 vec_add[blockspergrid, threadsperblock](a, b, c, N)
 ```

- **Memory management:** global, shared, constant, register memory

- **Memory coalescing** — efficient global memory access patterns

- **GPUs in physics:**
 - N-body gravitational simulation on GPU
 - Monte Carlo methods with millions of particles
 - MD force calculations (LAMMPS-GPU)

- **OpenCL** overview (cross-platform alternative to CUDA)

### Unit 4: Distributed Computing and Applications (Weeks 14–16)

- **MPI (Message Passing Interface):** for cluster computing
 - `mpi4py` in Python:
 ```python
 from mpi4py import MPI
 comm = MPI.COMM_WORLD
 rank = comm.Get_rank()
 size = comm.Get_size()
 data = scatter_data(root=0) # Send chunks to each process
 local_result = compute_local(data)
 result = comm.reduce(local_result, op=MPI.SUM, root=0)
 ```

- **MPI collectives:** reduce, gather, scatter, broadcast, barrier

- **Scaling study:** weak scaling vs. strong scaling

- **Cloud computing for physics:** AWS, Google Colab (T4/A100 GPUs)

- **Final project:** parallelize a physics simulation, benchmark, and present

---

## 🔬 Key Algorithms

$$## Unit 2: Shared-Memory Parallelism (Weeks 5–9)

- **OpenMP:** compiler directives for loop parallelization
 ```c
 #pragma omp parallel for reduction(+:sum)
 for (int i = 0; i < N; i++) {
 sum += a[i] * b[i];
 }
 ```

- **Critical sections** and race conditions

- **Load balancing:** distributing work evenly across threads

- **NumPy vectorization** — Python's "implicit parallelism"

- **Scientific Python parallelism:**
 - `joblib` for embarrassingly parallel loops
 - `dask` for larger-than-memory computation
 - `scipy` for optimized BLAS/LAPACK routines (multi-threaded by default)

### Unit 3: GPU Computing with CUDA (Weeks 10–13)

- **GPU architecture:** SMs, threads, warps, memory hierarchy

- **CUDA programming model:**
 ```python
 from numba import cuda
 @cuda.jit
 def vec_add(a, b, c, N):
 i = cuda.grid(1)
 if i < N:
 c[i] = a[i] + b[i]

 threadsperblock = 256
 blockspergrid = (N + 255) // 256
 vec_add[blockspergrid, threadsperblock](a, b, c, N)
 ```

- **Memory management:** global, shared, constant, register memory

- **Memory coalescing** — efficient global memory access patterns

- **GPUs in physics:**
 - N-body gravitational simulation on GPU
 - Monte Carlo methods with millions of particles
 - MD force calculations (LAMMPS-GPU)

- **OpenCL** overview (cross-platform alternative to CUDA)

### Unit 4: Distributed Computing and Applications (Weeks 14–16)

- **MPI (Message Passing Interface):** for cluster computing
 - `mpi4py` in Python:
 ```python
 from mpi4py import MPI
 comm = MPI.COMM_WORLD
 rank = comm.Get_rank()
 size = comm.Get_size()
 data = scatter_data(root=0) # Send chunks to each process
 local_result = compute_local(data)
 result = comm.reduce(local_result, op=MPI.SUM, root=0)
 ```

- **MPI collectives:** reduce, gather, scatter, broadcast, barrier

- **Scaling study:** weak scaling vs. strong scaling

- **Cloud computing for physics:** AWS, Google Colab (T4/A100 GPUs)

- **Final project:** parallelize a physics simulation, benchmark, and present

---

## 🔬 Key Algorithms ext{Amdahl's law: } ext{Speedup}_{\max} = \frac{1}{(1-p) + \frac{p}{N}}$ $

# ## Unit 2: Shared-Memory Parallelism (Weeks 5–9)

- **OpenMP:** compiler directives for loop parallelization
 ```c
 #pragma omp parallel for reduction(+:sum)
 for (int i = 0; i < N; i++) {
 sum += a[i] * b[i];
 }
 ```

- **Critical sections** and race conditions

- **Load balancing:** distributing work evenly across threads

- **NumPy vectorization** — Python's "implicit parallelism"

- **Scientific Python parallelism:**
 - `joblib` for embarrassingly parallel loops
 - `dask` for larger-than-memory computation
 - `scipy` for optimized BLAS/LAPACK routines (multi-threaded by default)

### Unit 3: GPU Computing with CUDA (Weeks 10–13)

- **GPU architecture:** SMs, threads, warps, memory hierarchy

- **CUDA programming model:**
 ```python
 from numba import cuda
 @cuda.jit
 def vec_add(a, b, c, N):
 i = cuda.grid(1)
 if i < N:
 c[i] = a[i] + b[i]

 threadsperblock = 256
 blockspergrid = (N + 255) // 256
 vec_add[blockspergrid, threadsperblock](a, b, c, N)
 ```

- **Memory management:** global, shared, constant, register memory

- **Memory coalescing** — efficient global memory access patterns

- **GPUs in physics:**
 - N-body gravitational simulation on GPU
 - Monte Carlo methods with millions of particles
 - MD force calculations (LAMMPS-GPU)

- **OpenCL** overview (cross-platform alternative to CUDA)

### Unit 4: Distributed Computing and Applications (Weeks 14–16)

- **MPI (Message Passing Interface):** for cluster computing
 - `mpi4py` in Python:
 ```python
 from mpi4py import MPI
 comm = MPI.COMM_WORLD
 rank = comm.Get_rank()
 size = comm.Get_size()
 data = scatter_data(root=0) # Send chunks to each process
 local_result = compute_local(data)
 result = comm.reduce(local_result, op=MPI.SUM, root=0)
 ```

- **MPI collectives:** reduce, gather, scatter, broadcast, barrier

- **Scaling study:** weak scaling vs. strong scaling

- **Cloud computing for physics:** AWS, Google Colab (T4/A100 GPUs)

- **Final project:** parallelize a physics simulation, benchmark, and present

---

## 🔬 Key Algorithms ext{Amdahl's law: } ext{Speedup}_{\max} = \frac{1}{(1-p) + \frac{p}{N}}

$$ ext{MapReduce: Split} o ext{Map} o ext{Shuffle} o ext{Reduce}

$ $

$$ ext{Parallel sum: Tree reduction, work efficiency} = O\!\left(\frac{N}{p} + \log p
ight)

$ $

$$ ext{GPU kernel: 1 thread per data point, blocks of} \sim 256 ext{ threads}

$$

---

## 🎯 Learning Outcomes

Upon completion, students will be able to:
1. Identify parallelism opportunities in physics codes
2. Write parallel Python code using multiprocessing and joblib
3. Implement GPU kernels using Numba/CUDA
4. Use MPI for distributed computing across cluster nodes
5. Profile and optimize parallel code for performance
6. Apply parallel computing to real physics problems (N-body, MC, MD)

---

## 📚 References

1. Kirk, D.B. & Hwu, W.W. (2017). *Programming Massively Parallel Processors*, 4th ed. Morgan Kaufmann.
2. Pacheco, P. (2011). *An Introduction to Parallel Programming*. Jones & Bartlett.
3. Downey, A.B. (2014). *The Little Book of Semaphores*. (Free)
4. Numba CUDA documentation: https://numba.pydata.org/numba-doc/dev/cuda/
5. mpi4py documentation: https://mpi4py.readthedocs.io/
