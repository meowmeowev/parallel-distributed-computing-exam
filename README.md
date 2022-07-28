# Parallel Distributed Computing Final Exam
## LEVEL 1, ESSAY SECTION
#### Number 1. Differentiate between SIMD and MIMD? Explain

A single instruction is executed in multiple processors and processes multiple data. Those instructions can be performed sequentially, taking advantage of pipelining, or in parallel using multiple processors. An example is a moving game character, imagine a block of the box to move to the finish line. There is only 1 instruction and that is to move upward, downward, and sideward but it processes in multiple processors. While Multiple autonomous processors perform operations on different pieces of data, either independently or as part of shared memory space. This means that several different instructions can be executed at the same time, using different data streams. An example of this system is Intel Xeon Phi, descended from Larrabee microarchitecture. These processors have multiple processing cores (up to 61 as of 2015) that can execute different instructions on different data. Most parallel computers, as of 2013, are MIMD systems.

---
Number 2. Performance Metric of Parallel System.

— Runtime —

The serial runtime of a program is the time elapsed between the beginning and the end of its execution on a sequential computer. The parallel runtime is the time that elapses from the moment a parallel computation starts to the moment the last processing element finishes execution.

— Total Parallel Overhead —

The overheads incurred by a parallel program are encapsulated into a single expression referred to as the overhead function. We define an overhead function or total overhead of a parallel system as the total time collectively spent by all the processing elements over and above that required by the fastest known sequential algorithm for solving the same problem on a single processing element.

— Speedup —

When evaluating a parallel system, we are often interested in knowing how much performance gain is achieved by parallelizing a given application over a sequential implementation. Speedup is a measure that captures the relative benefit of solving a problem in parallel. 

— Efficiency —

Only an ideal parallel system containing p processing elements can deliver a speedup equal to p. In practice, ideal behavior is not achieved because while executing a parallel algorithm, the processing elements cannot devote 100% of their time to the computations of the algorithm. Efficiency is a measure of the fraction of time for which a processing element is usefully employed; it is defined as the ratio of speedup to the number of processing elements.

— Cost —

We define the cost of solving a problem on a parallel system as the product of parallel runtime and the number of processing elements used. The cost reflects the sum of the time that each processing element spends solving the problem. Efficiency can also be expressed as the ratio of the execution time of the fastest known sequential algorithm for solving a problem to the cost of solving the same problem on p processing elements.

---
Number 3. How does the performance of metrics of parallel systems affect each other? Explain.

Performance metrics apply to initial design phases as well as to procurement, tuning, and capacity planning analyses. Performance evaluation as a discipline has repeatedly proved to be critical for the design and successful use of parallel systems. At the early stage of design, performance models can be used to protect the system’s scalability and evaluate design alternatives. At the production stage, performance evaluation methodologies can be used to detect bottlenecks and subsequently suggest ways to alleviate them.

---
Number 4. Explain what pipelining is.

In Parallel Computing, pipelining does break a task into steps performed by different processor units, with inputs streaming through, much like an assembly line.

In networking, it is the method of sending multiple data units without waiting for an acknowledgment for the first frame sent. Pipelining ensures better utilization of network resources and also increases the speed of delivery, particularly in situations where a large number of data units make up a message to be sent.

---
## LEVEL 2, ESSAY SECTION
How does parallel programming/computing work? What do you think will be the advantage of utilizing a parallel approach?

Parallel Computing breaks all the problems into smaller parts that can be solved concurrently. Each part of the problem is further broken down into a series of instructions. And in each instruction, will execute simultaneously on different processors which makes a better solution. The advantage of utilizing a parallel approach is; that it saves more time because it processes more data and instructions, solves larger and more complex problems, provides concurrency, takes advantage of non-local resources, and makes better use of underlying parallel hardware.
