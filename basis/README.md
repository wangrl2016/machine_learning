## Deep Learning with Python

### Preface

### 1. What is Deep Learning?

#### 1.1 Artificial Intelligence, Machine Learning, and Deep Learning
#### 1.2 Before Deep Learning: A Brief History of Machine
#### 1.3 Why Deep Learning? Why Now?

### 2. The Mathematical Building Blocks of Neural Networks

#### 2.1 A First Look at a Neural Network
#### 2.2 Data Representations For Neural Networks
#### 2.3 The Gears of Neural Networks: Tensor Operations
#### 2.4 The Engine of Neural Networks: Gradient-Based
#### 2.5 Looking Back at Our First Example

### 3. Introduction to Keras and TensorFlow

#### 3.1 What's TensorFlow?
#### 3.2 What's Keras?
#### 3.3 Keras and TensorFlow: A Brief History
#### 3.4 Setting up a Deep Learning Workspace
#### 3.5 First Steps with TensorFlow
#### 3.6 Anatomy of a Neural Network: Understanding core Keras APIs

### 4. Getting Started with Neural Networks: Classification and Regression

#### 4.1 Classifying Movie Reviews: A Binary Classification Example
#### 4.2 Classifying News-wires: A Multiclass Classification Example
#### 4.3 Predicting HousePrices: A Regression Example

### 5. Fundamentals of Machine Learning

#### 5.1 Generalization: The Goal of Machine Learning
#### 5.2 Evaluating Machine Learning Models
#### 5.3 Improving Model Fit
#### 5.4 Improving Generalization

### 6. The Universal Workflow of Machine Learning

#### 6.1 Define the Task
#### 6.2 Develop a Model
#### 6.3 Deploy the Model

### 7. Working with Keras: A Deep Dive

#### 7.1 A Spectrum of Workflows
#### 7.2 Different Ways to build Keras Models
#### 7.3 Using Built-in Training and Evaluation Loops
#### 7.4 Writing Your Own Training and Evaluation Loops

### 8. Introduction to Deep Learning for Computer Vision

#### 8.1 Introduction to Convnets
#### 8.2 Training a Convnet from Scratch on a Small Dataset
#### 8.3 Leveraging a Pretrained Model

### 9. Advanced Deep Learning for Computer Vision

#### 9.1 Three Essential Computer Vision Tasks
#### 9.2 An Image Segmentation Example
#### 9.3 Modern Convnet Architecture Patterns
#### 9.4 Interpreting What Convnets Learn

### 10. Deep Learning for Timeseries

#### 10.1 Different kinds of Timeseries Tasks
#### 10.2 A Temperature-Forcasting Example
#### 10.3 Understanding Recurrent Neural Networks
#### 10.4 Advanced Use of Recurrent Neural Networks

### 11. Deep Learning for Text

#### 11.1 Netural Language Processing: The Bird's Eye View
#### 11.2 Preparing Text Data
#### 11.3 Two Approaches for Representing Groups of Words: Sets and Sequences
#### 11.4 The Transformer Architecture
#### 11.5 Beyond Text Classification: Sequence-to-sequence

### 12. Generative Deep Learning

#### 12.1 Text Generation
#### 12.2 DeepDream
#### 12.3 Neural Style Transfer
#### 12.4 Generating Images with Variational Autoencoders
#### 12.5 Introduction to Generative Adversarial Networks

### 13. Best Practices for the Real World

#### 13.1 Getting the Most out of Your Models
#### 13.2 Scaling-up Model Training

### Conclusions

#### 14.1 Key concepts in Review
#### 14.2 The Limitations of Deep Learning
#### 14.3 Setting the Course Toward Greater Generality in AI
#### 14.4 Implementating Intelligence: The Missing Ingredients
#### 14.5 The Future of Deep Learning
#### 14.6 Staying Up to Date in a Fast-moving Field
#### 14.7 Final Words

## Guide of TensorFlow

- [ ] Tensor

Tensors are multidimensional arrays with a uniform type (called a `dtype`). If you're
familiar with `NumPy`, tensors are (kind of) like `np.arrays`.

All tensors are immutable like Python numbers and strings: you can never update the contents
of the tensor, only create a new one.

Tensors have shapes. Some vocabulary:
* Shape: The length (number of elements) of each of the axes of a tensor.
* Rank: Number of tensor axes. A scalar has rank 0, a vector has rank 1, a matrix is rank 2.
* Axis or Dimension: A particular dimension of a tensor.
* Size: The total number of items in the tensor, the product of the shape vector's elements.

## TensorFlow Python API

- [x] tf.version

## Understanding Deep Learning

### 1. Introduction

Machine learning methods can coarsely be divided into three areas: supervised, unsupervised,
and reinforcement learning. At the time of writing, the cutting-edge methods in all three
areas rely on deep learning.

[ai_relationship.drawio](https://drive.google.com/file/d/1bpxuH7hIpAxgqb82dSW5jmk419Xx5gLp/view?usp=sharing)

#### 1.1 Supervised Learning

This vector forms the model input. The model maps the input to an output vector which is then
"translated" back to a meaningful real-world prediction.

Deep neural networks can process inputs that are very large, of variable length, and contain
various kinds of internal structures. They can output single real numbers (regression),
multiple numbers (multivariate regression), or probabilities over two or more classes
(binary and multiclass classification, respectively).

#### 1.2 Unsupervised Learning

Constructing a model from input data without corresponding output labels in termed
unsupervised learning; the absence of output labels means there can be no "supervision".
Rather than learning a mapping from input to output, the goal is to describe or
understand the structure of the data.

#### 1.3 Reinforcement Learning


#### 1.4 Ethics
#### 1.5 Structure of Book
#### 1.6 Other Books
#### 1.7 How to Read This Book

### 2. Supervised Learning

#### 2.1 Supervised Learning Overview
#### 2.2 Linear Regression Example
#### 2.3 Summary

### 3. Shallow Neural Networks

#### 3.1 Neural Network Example
#### 3.2 Universal Approximation Theorem
#### 3.3 Multivariate Inputs and Outputs
#### 3.4 Shallow Neural Networks: General Case
#### 3.5 Terminology
#### 3.6 Summary

### 4. Deep Neural Networks

#### 4.1 Composing Neural Networks
#### 4.2 From Composing Networks to Deep Networks
#### 4.3 Deep Neural Networks
#### 4.4 Matrix Notation
#### 4.5 Shallow vs. Deep Neural Networks
#### 4.6 Summary

### 5. Loss Functions

#### 5.1 Maximum Likelihood
#### 5.2 Recipe for Constructing Loss Functions
#### 5.3 Example 1: Univariate Regression
#### 5.4 Example 2: Binary Classification
#### 5.5 Example 3: Multiclass Classification
#### 5.6 Multiple Outputs
#### 5.7 Cross-entropy Loss
#### 5.8 Summary

### 6. Fitting Models

#### 6.1 Gradient Descent
#### 6.2 Stochastic Gradient Descent
#### 6.3 Momentum
#### 6.4 Adam
#### 6.5 Training Algorithm Hyperparameters
#### 6.6 Summary

### 7. Graidents and Initialization

#### 7.1 Problem Definitions
#### 7.2 Computing Derivatives
#### 7.3 Toy Example
#### 7.4 Backpropagation Algorithm
#### 7.5 Parameter Initialization
#### 7.6 Example Training Code
#### 7.7 Summary

### 8. Measuring Performance

#### 8.1 Training a Simple Model
#### 8.2 Sources of Error
#### 8.3 Reducing Error
#### 8.4 Double Descent
#### 8.5 Choosing Hyperparameters
#### 8.6 Summary

### 9. Regularization

#### 9.1 Explicit Regularization
#### 9.2 Implicit Regularization
#### 9.3 Heuristics to Improve Performance
#### 9.4 Summary

### 10. Convolutional Networks

#### 10.1 Invariance and Equivariance
#### 10.2 Convolutional Networks for 1D inputs
#### 10.3 Convolutional Networks for 2D inputs
#### 10.4 Downsampling and Unsampling
#### 10.5 Applications
#### 10.6 Summary

### 11. Residual Networks

#### 11.1 Sequential Processing
#### 11.2 Residual Connecting and Residual Blocks

