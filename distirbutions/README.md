# Study in Distributions
A probability distribution of a random variable X is the set of probabilities assigned to each possible value of X.

## Probability Distribution Function vs. Cumulative Distribution Function

### Probability Distribution Fuction (PDF)
1. The probability density function $f(x)$ is the probability that $X$ takes on values between two adjacent realizations of the random variable.
2. Focuses on one specific value

### Cumulative Distribution Function (CDF)
1. Monotonically non-decreasing function (Function that may be flat in some ranges and increasing in others but never decreasing)
2. Such that $\lim_{x\to-\infty} f(x) = 0$ and $\lim_{x\to\infty} f(x) = 1$
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

Here standard score or **Z-score** is also defined as $(X - \mu_x)/\sigma_x$ 

**How does it measure skewness?**
A standard score or z-score of a point close to $\mu_x$ will have a small value where as a data point farther away from $\mu$ will have a larger value. When the difference is cubed, it preserves the +ve and -ve signs of the difference and it makes small values smaller and large values comparatively larger. Summing up all the standard scores gives us the overall +ve or -ve tendency of the z-scores (or skewness). A normal distribution with no skewness will have a skewness value of zero. 

Note: Skewness is **not** a test of symmetry. Asymmetric distributions can have zero skewness. But Symmetric distributions always have zero skewness.

### Kurtosis
The fourth **central** moment  $(k=4)$ gives a measure of peakiness of the distribution.


### Characteristic function for Random Variables
Characteristic functions are moment generating functions that can be used to analyze the characteristics (moments) of a random variable. A characteristic function uses Inverse Fourier Transform a analyze random variable in a different space. Each random variable generally has a unique characteristic function and it makes it easier to mathematically analyze combinations of characteristic functions rather than PMFs or PDFs.

The characteristic function uses the Inverse Fourier transform to represent the random variable as:

$$ \phi_x(\omega) = E_x[e^{ix\omega}] $$

or

$$ \phi_x(\omega) = \int_{-\infty}^{\infty} f(x)e^{ix\omega} dx $$

where $f(x)$ represents the Probability Density Function for random variable X.

**Why is $e^{ix\omega}$ a moment generating function?**
For a random variable X, 

$$e^{X} = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!} + .... $$

$$e^{\omega X} = 1 + \frac{\omega x}{1!} + \frac{(\omega x)^2}{2!} + \frac{(\omega x)^3}{3!} + \frac{(\omega x)^4}{4!} + \frac{(\omega x)^5}{5!} + .... $$


$$E[e^{\omega X}] = 1 + \frac{\omega}{1!} E[X] + \frac{\omega^2}{2!} E[X^2] + \frac{\omega^3}{3!} E[X^3] + \frac{\omega^4}{4!} E[X^4] + \frac{\omega^5}{5!} E[X^5] .... $$

Provided Expectation exists from some \omega in the neighborhood of 0, we can find the coefficients by taking the differential and setting $\omega=0$

$$\frac{dE[e^{\omega X}]}{d\omega} |_{\omega=0} = 0 + E[X] + 0 + 0 ... $$ 

$$\frac{d^2E[e^{\omega X}]}{d\omega} |_{\omega=0} = 0 + 0 + E[X^2] + 0 + 0 ... $$ 

Hence $e^{ix \omega}$ is a moment generating function.

## Common Distribution Types
#### Bernoulli (Discrete)
A Bernoulli distribution captures the probabiliy of a binary outcome. It is represented as $Bern(p)$ where $p$ is the probability of a successful outcome and $q$ is the probability of an unsuccessful outcome where $q=1-p$.

The Probability Mass Function (PMF) for a Bernoulli distribution is give as 

$$
f(x;p) = p^x.(1-p)^{1-x} 
$$

Alternatively the PMF can be represented as

$$
f(x;p) = p.x + (1-p).(1-x)
$$

where,

$$
x \in {0,1}
$$

and

$$
p = P(X=1)
$$

**Expected Value**

$$
E(X) = 1.p(X=1) + 0.p(X=0)
$$

or

$$
E(X) = p(X=1)
$$

Here X is considered an indicator variable. It acts as a bridge between Expected value and probability.

#### Binomial (Discrete)
The Binomial distribution captures the proability of x successes in n independent and indentically distributed (each trail has the same probability of sucess $p$) bernoulli trails. The notation is represented as $X \tilde Bin(n,p)$

The PMF for k successes is given as

$$
f(x=k:n,p) = ^{n}C_{k}.p^{k}.(1-p)^{(n-k)}
$$

or it $q = 1-p$ then,

$$
f(x=k:n,p) = ^{n}C_{k}.p^{k}.(q)^{(n-k)}
$$

where 

$$
x \in {0,1,..n}
$$

and $k>0$

We can prove the that the sum of all the probabilities given by the PMF is 1

$$
\sum_{k=0}^{n} (^{n}C_{k}.p^{k}.(q)^{(n-k)})
$$

The above is a Binomial expression for $(p+q)^n$

Hence,

$$
= (p+q)^n
$$

$$
= (p + 1 - p)^n = 1
$$

We can also prove that we can combine $X \sim Bin(n,p)$ and $Y \sim Bin(m,p)$ to $X+Y \sim Bin(n+m,p)$. This is known as a convolution. By convention if we have n i.i.d Bern(p) trials and m i.i.d Bern(p) trials then we have a total of n+m i.i.d Bern(p) trials. We are tossing the coin n+m times instead of n and m times. Since these are i.i.d events, each trial itself has not impact on any prior or future trial which allows us to combine them. This is known as **convolution**.

Mathematically to get the convolution we want to determine $P(X+Y=k)$. Here we assume that we already know X. They by law of total probability

$$
P(X+Y=k) = \sum_{j=0}^{k} P(X+Y=k | X=j) P(X=j)
$$

$$
P(X+Y=k) = \sum_{j=0}^{k} P(j+Y=k | X=j) ^{n}C_{j}.p^j.q^{k-j}
$$


$$
P(X+Y=k) = \sum_{j=0}^{k} P(j+Y=k | X=j) ^{n}C_{j}.p^j.q^{n-j}
$$

$$
P(X+Y=k) = \sum_{j=0}^{k} P(Y=k-j | X=j) ^{n}C_{j}.p^j.q^{n-j}
$$

Since X and Y are i.i.d $P(Y=k-j | X=j) = P(Y=k-j)$

$$
P(X+Y=k) = \sum_{j=0}^{k} P(Y=k-j).^{n}C_{j}.p^j.q^{(n-j)}
$$

$$
P(X_Y=k) = \sum_{j=0}^{k} (^{m}C_{k-j}.p^{(k-j)}.q^{(m-k+j)}).^{n}C_{j}.p^j.q^{n-j}
$$

$$
P(X_Y=k) = p^{(k)}.q^{(m+n-k)} \sum_{j=0}^{k} (^{m}C_{k-j}.^{n}C_{j})
$$

The last part is the [Vandermonde identity](https://en.wikipedia.org/wiki/Vandermonde%27s_identity) and can be written as

$$
P(X_Y=k) = p^{(k)}.q^{(m+n-k)}.^{m+n}C_{k}
$$

**Expected Value**

The expected value of a Binomial distruibution can be give as:

$$
E(X) = \sum_{k=0}^{n} k.^{n}C_{k}.p^{k}.q^{n-k}
$$

or since for $k=0$ the value is zero we can ignore the $0^{th}$ term

$$
E(X) = \sum_{k=1}^{n} k.^{n}C_{k}.p^{k}.q^{n-k}
$$

To solve this, we consider that $k.^{n}C_{k}$ can be written as $n.^{n-1}C_{k-1}$. Essentially this is like choosing a committee of $k$ from $n$ people and then choosing a president. We can alternatively choose a president and then choose a committed of $k-1$ people from $n-1$ people.

$$
E(X) = \sum_{k=1}^{n} n.^{n-1}C_{k-1}.p^{k}.q^{n-k}
$$

$$
E(X) = n.p.\sum_{k=1}^{n} n.^{n-1}C_{k-1}.p^{k-1}.q^{n-k}
$$

Let $j = k - 1$ or $k=j+1$ we get,

$$
E(X) = n.p.\sum_{j=0}^{n} n.^{n-1}C_{j}.p^{j}.q^{n-1-j}
$$

The last term is summation of the binomial distribution and hence it is 1. 

$$
E(X) = n.p
$$

#### Hypergeometric (Discrete)
The Binomial distribution captures distribution of i.i.d events or like shuffling a deck of cards where we pick a card and replace it back into the deck. But what about the successes of trials which are not i.i.d. where we pick a card and we do not replace it. Hypergeometric captures the distribution of the second case where the trials are without replacement. 

**Example:**
We have $w$ white marbles and $b$ black marbles. We choose or sample $n$ marbles and find the probability $k$ marbles in the sample. $n$ represents the trials and $k$ represents the successes.

The PMF of the above example is given by,

$$
f(x=k;n,w,b) =  \frac{^bC_k.^{w}C_{(n-k)}}{^{(w+b)}C_{n}}
$$

The sum of the PMF should be equal to 1. This can be show as,

$$
\sum_{k=0}^{n} \frac{^bC_k.^{w}C_{(n-k)}}{^{(w+b)}C_{n}}
$$

$$
\frac{1}{^{(w+b)}C_{n}} \sum_{k=0}^{n} (^bC_k.^{w}C_{(n-k)})
$$

which by Vandermonde identity is

$$
\frac{1}{^{(w+b)}C_{n}}.(^{(w+b)}C_{n}) = 1
$$


#### Gemoetric (Discrete)

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
5. [What are moment generating functions?](https://www.youtube.com/watch?v=dVRWBmykncQ&t=313s)
6. [What are characteristic functions?](https://www.youtube.com/watch?v=mYhca1p26n4)
