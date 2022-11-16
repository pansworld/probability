# Study in Distributions
A probability distribution of a random variable X is the set of probabilities assigned to each possible value of X.

## Probability Distribution Function vs. Cumulative Distribution Function

### Probability Distribution Fuction (PDF)
1. The probability density function $f(x)$ is the probability that $X$ takes on values between two adjacent realizations of the random variable.
2. Focuses on one specific value

### Cumulative Distribution Function (CDF)
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

### Discrete Distributions
Have the following properties:
1. The CDF is described as
$$F(x)=P(X \le x) = \sum_{x_i \le x} P(X=x_i)$$
2. They are described by a **Probability Mass Function**
$$f(x_j) = P(X = x_j)$$
$$0 \le f(x_j) \le 1$$
$$\sum_{j}f(x_j)=1$$


### Continuous Distributions
1. The CDF is described as
$$F(x)=\int_{-\infty}^{x}f(y)dy$$
2. They are described by a **Probability Density Function**
$$f(x) = dF/dx$$
$$\int_{-\infty}^{\infty}f(x)dx=1$$
$$f(x) \ge 0$$

## General Properties of Distributions
### Moment of distributions
A “moment” refers to how probability mass is distributed. Moments quantify three parameters of distributions: location (where is the mean), shape (what is the geometry: bimodal, asymmetric, heavy tailed etc.), and scale (what is the spread or variance). The **$k^{th}$ central moment** about the mean $\mu_x$ for a random variable X can be written as:

$$
E[(X - \mu_x)^k] = \sum_{i=1}^{n} (x_i - \mu_x)^k f(x_i)
$$

$$
E[(X - \mu_x)^k] = \int_{-\infty}^{\infty} (x - \mu_x)^k f(x) dx
$$

A **raw moment** is the $k^{th}$ moment for a random variable X whose mean $\mu_x = 0$ 

$$
E[X^k] = \sum_{i=1}^{n} x_i^k f(x_i)
$$

$$
E[X^k] = \int_{-\infty}^{\infty} x^k f(x) dx
$$

### Expectation and mean $(\mu)$
Mean is the **raw** first $(k=1)$ moment of the distribution. Or it represents the distance at which the center of mass of the distribution is located.

$$
E[X] = \sum_{i=1}^{n} x_i f(x_i)
$$

$$
E[X] = \int_{-\infty}^{\infty} x f(x) dx
$$

### Variance $(\sigma^2)$
Variance is the second **central** $(k=2)$ moment of the distribtion. It represents the spread of the distribution.

| <img src="https://github.com/pansworld/probability/blob/1dc0aa73349b4dc47af3dccdf3a8bc5e4604f91a/distirbutions/images/normal_with_diff_variances.png" width="50%" height="50%"> | 
|:--:| 
| Shows normal distribution with standard deviation $(\sigma)$ of 1, 0.5 and 0.33. The distribution with 0.33 $(\sigma)$ is more compact and 1.0 is spread out. |


Variance is calculated as

$$
Var(X) = E[(X - \mu_x)^2] = \sum_{i=1}^{n} (x_i - \mu_x)^2 f(x_i)
$$

$$
Var(X) = E[(X - \mu_x)^2] = \int_{-\infty}^{\infty} (x - \mu_x)^2 f(x) dx
$$

Variance can also be defined in terms of Expectations

$$
Var(X) = E[(X - E[X])^2] 
$$

$$
Var(X) = E[X^2 - 2XE[X] - (E[X])^2]
$$

$$
Var(X) = E[X^2] - E[2XE[X]] - E[(E[X])^2]
$$

$$
Var(X) = E[X^2] - 2E[X]E[X] - (E[X])^2]
$$

$$
Var(X) = E[X^2] - (E[X])^2
$$

### Standard Deviation $(\sigma)$
Standard deviation is another measure of the spread of the distribution that is compatible with the units of the random variable X. It is defined as:

$$
\sigma = \sqrt{Var(X)}
$$

### Skewness
The third **central** moment $(k=3)$ gives a measure of the skewness of the distribution. A distribution can be positively skewed or negatively skewed as shown below: Positively skewed (or right skewed) has values clustered around the left tail of the distribution whereas a negatively skewed (or left skewed) has values clustered around the right tail of the distribution. Probabilities taper off for higher values (positive), taper off for lower values (negative) and the extreme values are found either on the right or the left of the peak.

| <img src="https://github.com/pansworld/probability/blob/359fc15f0533888caeb0f54c21ea168a55f5dd24/distirbutions/images/positive_negative_skewed.png" width="100%" height="100%"> | 
|:--:| 
| Shows negatively and positively skewed distribution. |

Extreme skewness is not desireable and hence there are statistical methods to reduce the skewness:

| Positively Skewed | Negatively Skewed |
|:--:|:------:|
| Square Root | Squares |
| Cube Root | Cubes |
| Logarithms | Higher Powers |

Skewness is calculated as

$$
E[((X - \mu_x)/\sigma_x)^3] = \sum_{i=1}^{n} ((x_i - \mu_x)/\sigma_x)^3 f(x_i)
$$

$$
E[((X - \mu_x)/\sigma_x)^3] = \int_{-\infty}^{\infty} ((x - \mu_x)/\sigma_x)^3 f(x) dx
$$

### Kurtosis
The fourth **central** moment  $(k=4)$ gives a measure of peakeness of the distribution.


### Characteristic function (Fourier transform)


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
3. [Understanding Moment](https://gregorygundersen.com/blog/2020/04/11/moments/)
4. [Data Skewness Reducing Techniques](https://www.kaggle.com/getting-started/110134)
