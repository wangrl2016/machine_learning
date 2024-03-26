# machine_learning
Machine learning from the ground up

As machine learning becomes popular, more and more people want to switch to the machine learning
industry in order to stay at the forefront of the times and obtain higher prospects or income.

But getting started with machine learning is not as simple as traditional programming. It
involves a lot of mathematical knowledge and engineering practices. This tutorial is designed to
break down these boundaries and is intended for those with only a high school background.

Before writing the simplest neural network, you need to be proficient in writing Python code, as
well as a lot of mathematical background, especially derivatives and matrices.

This tutorial is mainly divided into three parts: the first part is prerequisites, mainly solving
programming and mathematical problems; the second part is the basics of machine learning, writing
neural networks from scratch, training simple data, and comprehensively understanding the
TensorFlow library; the third part is to follow the industry cutting-edge, such as learning
large language models and reading relevant papers.

If your English is not good, it is recommended that you start by learning English first, because
many materials come from the English-speaking world. If some people pay attention to this tutorial,
I will consider opening a YouTube channel to explain it.

There's a lot more to say, but if you want to learn, just follow the tutorial and get started. This
will be a difficult journey, and you will gain a lot. Perhaps you will find that machine learning is
not that mysterious after all. Then I wish you success.

## Prerequisite

### [Python](python)

Python is a programming language that lets you work quickly and integrate systems more effectively.
Mainly divided into three parts for learning:

(1) The Python tutorial

This tutorial refers to the official tutorial [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
which will allow you to write Python code quickly. Practice makes perfect and requires
continuous practice in subsequent studies.

- [x] Whetting Your Appetite
- [x] Using the Python Interpreter
- [x] An Informal Introduction to Python
- [x] More Control Flow Tools
- [x] Data Structures
- [x] Modules and Packages
- [x] Import and Output
- [x] Classes
- [x] Errors and Exceptions

(2) Python Standard Library

Only select common and important content for introduction. For comprehensive information, please
refer to the official website [The Python Standard Library](https://docs.python.org/3/library/index.html).

- [x] Brief Tour of the Standard Library (I)
- [x] Brief Tour of the Standard Library (II)
- [x] `turtle` — Turtle graphics
- [x] `logging` - Logging facility for Python

(3) Third-party library

Mainly select libraries related to machine learning for introduction to consolidate the Python
tutorials learned previously. Reference book: [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)

- [x] [NumPy](https://numpy.org/): The fundamental package for scientific computing with Python
- [x] [Pandas](https://pandas.pydata.org/): Data analysis and manipulation tool
- [ ] [SciPy ](https://scipy.org): An open-source software for mathematics, science, and engineering.
- [ ] [Matplotlib](https://matplotlib.org/): Visualization with Python

There are many ways to get started with Python, and you can even learn other languages first,
such as C language and Java language, these languages have a lot in common. You can choose
what you like during the learning process. Here are some learning materials for reference
and consolidation.

* [The Python Coding Book](https://thepythoncodingbook.com/)
* [C Primer Plus](https://www.oreilly.com/library/view/c-primer-plus/9780133432398/)
* [Introduction to Programming in Python](https://introcs.cs.princeton.edu/python/home/)

To check if you have mastered Python, here are a few small tests to complete.

- [ ] Text: Load height-weight-gender database
- [ ] Sound: Handwritten WAV decoder according to protocol

### Computer Science

If you don't know anything about computer basics, then you'd better need to supplement the
basics, including computer systems and algorithms, before proceeding to more in-depth study.

(4) Computer Systems: A Programmer's Perspective, 3rd Edition

- [ ] A Tour of Computer Systems
- [ ] Representing and Manipulating Information
- [ ] Machine-Level Representation of Programs
- [ ] Processor Architecture
- [ ] Optimizing Program Performance
- [ ] The Memory Hierarchy
- [ ] Linking
- [ ] Exceptional Control Flow
- [ ] Virtual Memory
- [ ] System-Level I/O
- [ ] Network Programming
- [ ] Concurrent Programming

(5) Introduction to Algorithms, 4th Edition

- [ ] The Role of Algorithms in Computing
- [ ] Getting Started
- [ ] Characterizing running Times
- [ ] Divide-and-Conquer
- [ ] Probabilistic Analysis and Randomized Algorithms
- [ ] Heapsort
- [ ] Quicksort
- [ ] Sorting in Linear Time
- [ ] Medians and Order Statistics
- [ ] Elementary Data Structures
- [ ] Hash Tables
- [ ] Binary Search Trees
- [ ] Red-Black Trees
- [ ] Dynamic Programming
- [ ] Greedy Algorithms
- [ ] Amortized Analysis
- [ ] Augmenting Data Structures
- [ ] B-Trees
- [ ] Data Structures for Disjoint Sets
- [ ] Elementary Graph Algorithms
- [ ] Minimum Spanning Trees
- [ ] Single-Source Shortest Paths
- [ ] All-Pairs Shortest Paths
- [ ] Maximum Flow
- [ ] Matchings in Bipartite Graphs
- [ ] Parallel Algorithms
- [ ] Online Algorithms
- [ ] Matrix Operations
- [ ] Linear Programming
- [ ] Polynomials and the FFT
- [ ] Number-Theoretic Algorithms
- [ ] String Matching
- [ ] Machine-Learning Algorithms
- [ ] NP-Completeness
- [ ] Approximation Algorithms

The difficulty of (4) and (5) is beyond imagination, so it is best to watch the official
video and check more information, focusing on understanding the relevant concepts.

### [Math](math)

Machine learning involves a large amount of mathematical knowledge, among which calculus,
linear algebra, and probability theory are particularly important. The following is divided
into four parts:

(1) Precalculus

Precalculus uses the textbook provided by [OpenStax](https://openstax.org/)，which provides a
comprehensive exploration of mathematical principles and meets scope and sequence requirements
for a typical precalculus course. The text proceeds from functions through trigonometry and
ends with an introduction to calculus.

- [ ] Functions
- [ ] Linear Functions
- [ ] Polynomial and Rational Functions
- [ ] Exponential and Logarithmic Functions
- [ ] Trigonometric Functions
- [ ] Periodic Functions
- [ ] Trigonometric Identities and Equations
- [ ] Further Applications of Trigonometry
- [ ] Systems of Equations and Inequalities
- [ ] Analytic Geometry
- [ ] Sequences, Probability and Counting Theory
- [ ] Introduction to Calculus 

(2) Calculus

Calculus uses the textbook provided by [OpenStax](https://openstax.org/), which contains three
volumes in total. It guides students through the core concepts of calculus and helps them
understand how those concepts apply to their lives and the world around them.

Calculus I

- [ ] Functions and Graphs
- [ ] Limits
- [ ] Derivatives
- [ ] Applications of Derivatives
- [ ] Integration
- [ ] Application of Integration

Calculus II

- [ ] Techniques of Integration
- [ ] Introduction to Differential Equations
- [ ] Sequences and Series
- [ ] Power Series
- [ ] Parametric Equations and Polar

Calculus III

- [ ] Vectors in Space
- [ ] Vector-Valued Functions
- [ ] Differentiation of Functions of Several Variables
- [ ] Multiple Integration
- [ ] Vector Calculus
- [ ] Second-Order Differential Equations

(3) Introduction to Linear Algebra, 6th Edition

- [ ] Vectors and Matrices
- [ ] Solving Linear Equations Ax = b
- [ ] The Four Fundamental Subspaces
- [ ] Orthogonality
- [ ] Determinants
- [ ] Eigenvalues and Eigenvectors
- [ ] The Singular Value Decomposition
- [ ] Linear Transformations
- [ ] Linear Algebra in Optimization
- [ ] Learning from Data

(4) Introductory Statistics

- [ ] Sampling and Data
- [ ] Descriptive Statistics
- [ ] Probability Topics
- [ ] Discrete Random Variables
- [ ] Continuous Random Variables
- [ ] The Normal Distribution
- [ ] The Central Limit Theorem
- [ ] Confidence Intervals
- [ ] Hypothesis Testing with One Sample
- [ ] Hypothesis Testing with Two Samples
- [ ] The Chi-Square Distribution
- [ ] Linear Regression and Correlation
- [ ] F Distribution and One-Way ANOVA 

## Basic of Machine Learning

It is mainly written with reference to the [TensorFlow](https://www.tensorflow.org/)
official website and the book [Deep Learning with Python](https://github.com/fchollet/deep-learning-with-python-notebooks),
which comprehensively covers the basic content of machine learning.

(1) Introduction to Deep Learning

An efficient and high-intensity bootcamp designed to teach you the fundamentals of deep
learning as quickly as possible!

- [ ] What is Deep Learning 
- [ ] Tensor
- [ ] Tensor Slicing
- [ ] Variable
- [ ] TensorFlow Function
- [ ] Simple Function Implementation
- [ ] The Mathematical Building Blocks of Neural Networks
- [ ] Simple Neutral Network
- [ ] Automatic Differentiation
- [ ] Advanced Autodiff
- [ ] Binary Classification with DNN
- [ ] Graph
- [ ] Modules, Layers, and Models

(2) TensorFlow Python API

TensorFlow has APIs available in several languages both for constructing and executing a
TensorFlow graph. Because the official [API Documentation](https://www.tensorflow.org/api_docs/)
is constantly updated, there will be differences between this tutorial and the official API.

- [ ] tf
- [ ] tf.audio
- [ ] tf.autodiff
- [ ] tf.autograph
- [ ] tf.bitwise
- [ ] tf.compat
- [ ] tf.config
- [ ] tf.data
- [ ] tf.debugging
- [ ] tf.distribute
- [ ] tf.dtypes
- [ ] tf.errors
- [ ] tf.experimental
- [ ] tf.feature_column
- [ ] tf.image
- [ ] tf.io
- [ ] tf.keras
- [ ] tf.linalg
- [ ] tf.lite
- [ ] tf.lookup
- [ ] tf.math
- [ ] tf.mlir
- [ ] tf.nest
- [ ] tf.nn
- [ ] tf.profiler
- [ ] tf.queue
- [ ] tf.ragged
- [ ] tf.random
- [ ] tf.raw_ops
- [ ] tf.saved_model
- [ ] tf.sets
- [ ] tf.signal
- [ ] tf.sparse
- [x] tf.strings
- [ ] tf.summary
- [ ] tf.sysconfig
- [ ] tf.test
- [ ] tf.tpu
- [ ] tf.train
- [ ] tf.types
- [x] tf.version
- [ ] tf.xla

(3) Understanding Deep Learning

- [ ] Introduction
- [ ] Supervised Learning
- [ ] Shallow Neural Networks
- [ ] Deep Neural Networks
- [ ] Loss Functions
- [ ] Training Models
- [ ] Gradients and Initialization
- [ ] Measuring Performance
- [ ] Regularization
- [ ] Convolutional Networks
- [ ] Residual Networks
- [ ] transformers
- [ ] Graph Neural Networks
- [ ] Unsupervised Learning
- [ ] Generative Adversarial Networks
- [ ] Normalizing Flows
- [ ] Variational Autoencoders
- [ ] Diffusion Models
- [ ] Deep Reinforcement Learning
- [ ] Why Does Deep Learning Work?
- [ ] Deep Learning and Ethics

## Cutting Edge

- [ ] Deep Residual Learning for Image Recognition (12/10/2015)

- [ ] Attention Is All You Need (6/12/2017)

