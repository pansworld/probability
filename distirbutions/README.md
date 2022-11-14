# Study in Distributions
A probability distribution of a random variable X is the set of probabilities assigned to each possible value of X.

## Probability Distribution Function vs. Cumulative Distribution Function

#### Probability Distribution Fuction (PDF)
1. The probability density function $f(x)$ is the probability that $X$ takes on values between two adjacent realizations of the random variable.
2. Focuses on one specific value

#### Cumulative Distribution Function (CDF)
1. Monotonically non-decreasing function (Function that may be flat in some ranges and increasing in others but never decreasing)
2. such that $\lim_{x\to-\infty} f(x) = 0$ and $\lim_{x\to\infty} f(x) = 1$
3. Defined as $F(x) = P(X \le x)$
4. Focuses on a sum or integral of values

## Discrete vs. Continuous
Distributions are based on two types of random variables.

**Discrete Random Variables**
Variables that take distinct values. 
```
Variable that captures the outcome of a dice roll (1 through 6).
```

**Continuous Random Variables**
Variables that take any value within a range. 
```
Variable that captures the amount of rainfall.
```

#### Discrete Distributions
Have the following properties:
1. The CDF is described as
$$F(x)=P(X \le x) = \sum_{x_i \le x} P(X=x_i)$$
2. They are described by a **Probability Mass Function**
$$f(x_j) = P(X = x_j)$$
$$0 \le f(x_j) \le 1$$
$$\sum_{j}f(x_j)=1$$


#### Continuous Distributions
1. The CDF is described as
$$F(x)=\int_{-\infty}^{x}f(y)dy$$
2. They are described by a **Probability Density Function**
$$f(x) = dF/dx$$
$$\int_{-\infty}^{\infty}f(x)dx=1$$
$$f(x) \ge 0$$

## General Properties of Distributions
#### Moment of distributions

#### Expectation and mean

#### Variance

#### Standard Deviation

#### Characteristic function (Fourier transform)


## Common Distribution Types
#### Bernoulli (Discrete)

#### Poisson (Discrete)

#### Uniform (Continuous)

#### Normal or Gaussian (Continuous)

#### Student's T-Distribution (Continuous)

#### Chi-Squared (Continuous)

## Resources
1. [Probabilities and Statistics refresher](https://stanford.edu/~shervine/teaching/cs-229/refresher-probabilities-statistics)
2. [Statistics cheatsheet](https://stanford.edu/~shervine/teaching/cme-106/cheatsheet-statistics)
