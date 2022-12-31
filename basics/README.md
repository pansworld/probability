# Mathematics Review

## The beauty of e
Consider $f(x)=2^x$. To find the slope we increment $x$ by $dx$ and measure the rate of change as

$$ \frac{df(x)}{dx} =  \frac{2^{x+dx} - 2^x}{dx} $$


$$ \frac{df(x)}{dx} =  \frac{2^x (2^{dx} - 1)}{dx} $$

The fraction $\frac{2^{dx} - 1}{dx}$ varies at a particular starting value of $x$ depending on incremental change in $dx$. For example for for $dx=0.000091$ it's value is $0.693169041631$ and for $dx=0.000001$ it's value decreases slightly to $0.693147420794$. 

Now consider $f(x)=2.71828^x$. The fraction $\frac{2.71828^{dx} - 1}{dx}$ has a value $1.00004482867$ for $dx=0.000091$ and a value $0.999999827389
$ for $dx=0.000001$ or it is $\approx 1$.  

$$ \frac{df(x)}{dx} = e^x $$

where $e=2.718281828459045...$


## Taylor Series
Useful for approximating functions in terms of ploynomials. 

Example:
When calculating $cos(\theta)$ we can approximate it the following polynomial. It is easy to derive this value. See [Taylor Series: Essence of Caclulus](https://www.youtube.com/watch?v=3d6DsjIBzJ4)

$$ cos(\theta) \approx 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} $$  

can be visualized as:

| <img src="https://github.com/pansworld/probability/blob/30ca01efd9d445a81e55adebef5828982f0f64c9/basics/images/Taylor_Polynomial_cos_theta.png" width="50%" height="50%"> |

When we add infinte number of terms to the polynomial it forms the taylor series which converges to the true value of the function (hence the equality instead of approximation).

$$ cos(\theta) = 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} ...  $$

or 

$$ cos(\theta) = \sum^{\infty}_{n=0} (-1)^{n} \frac{\theta^{2n}}{2n!} $$

Similarly $sin(\theta)$ can we written in terms of the Taylor series as

$$ sin(\theta) = \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} ...  $$

or 

$$ sin(\theta) = \sum^{\infty}_{n=0} (-1)^{n} \frac{\theta^{2n+1}}{(2n+1)!} $$

The first three terms can be visualized as shown below

| <img src="https://github.com/pansworld/probability/blob/30ca01efd9d445a81e55adebef5828982f0f64c9/basics/images/Taylor_Polynomial_cos_theta.png" width="50%" height="50%"> |

This power series expansion of functions is good for approximation and may be useful in computations, but it does not tell us the whole story about the function itself. For example the power series does not indicate that sine and cosine functions are periodic in $2\pi$.


## Taylor Series for e
The Taylor series for $e^x$ can be written as 

$$ e^x =  \sum^{\infty}_{n=0} \frac{x^{n}}{(n)!} $$

## Euler's formula

Consider the Taylor series for complex function $e^{ix}$

$$ e^{ix} =  \sum^{\infty}_{n=0} \frac{(ix)^{n}}{(n)!} $$

$$ e^{ix} = \sum^{\infty}_{n=0} i^{n} \frac{(x)^{n}}{(n)!} $$

Expanding the summation

$$ e^{ix} = 1 + \frac{ix}{1!} - \frac{x^2}{2!} - \frac{ix^3}{3!} + \frac{x^4}{4!} + \frac{ix^5}{5!} ... $$

Separating the real and imaginary parts

$$ e^{ix} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} ... + i(\frac{x}{1!} - \frac{x^3}{3!} + \frac{x^5}{5!} ...) $$


$$ e^{ix} = cos(x) + isin(x) $$

You can also derive Euler's identity as by setting $x=\pi$

$$ e^{i\pi} = cos(\pi) + isin(\pi) $$

$$ e^{i\pi} = -1  + 0 $$

$$ e^{i\pi} + 1 = 0 $$


## Fourier Series
Basic concept is that any waveform can we represented as a combination of sinusoids. The transform converts a time series function into the frequency domain. For example the $\sin\left(x\right)-\sin\left(2x\right)+\cos\left(5x\right)-\cos\left(10x\right)$ can be represented as shown below:

| <img src="https://github.com/pansworld/probability/blob/10f8a62875dd1505afffcb70c1f649d2be785896/basics/images/Fourier_Transform_Combined_Sinusoids.png" width="50%" height="50%"> |

The discrete combination in general can be represented as basis functions cosine / sine and coefficients $a_n$ and $b_n$

$$ f(x) = \sum_{n=0}^{\infty} a_n cos(nx) + \sum_{n=0}^{\infty} b_n sin(nx) $$

or

$$ f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx} $$

We use the orthogonality between basis functions of different frequencies to find values of $a_n$ and $b_n$. The dot product is represented as:

$$ \int_{-\infty}^{\infty} cos(nx) cos(kx) dx = 0 $$

$$ \int_{-\infty}^{\infty} sin(nx) sin(kx) dx = 0 $$

$$ \int_{-\infty}^{\infty} cos(nx) sin(kx) dx = 0 $$

To get $a_k$ we multiply both sides of the series by $cos(kx)$ and integrate over $=\pi$ to $\pi$ or

$$ \int_{-\pi}^{\pi} f(x) cos(kx) dx = \int_{-\pi}^{\pi} \sum_{n=0}^{\infty} a_n cos(nx) cos(kx) dx + \int_{-\pi}^{\pi} \sum_{n=0}^{\infty} b_n sin(nx) cos(kx) dx $$

$$ \int_{-\pi}^{\pi} f(x) cos(kx) dx = \int_{-\pi}^{\pi} a_k cos(kx)^2 dx $$

$$ \int_{-\pi}^{\pi} f(x) cos(kx) dx = a_k \pi $$

$$ a_k = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) cos(kx) dx $$

$$ a_0 = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) dx $$

Similarly,

$$ b_k = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) sin(kx) dx $$

When dealing with complex functions the Fourier series (using Euler's formula) can be represented as,

$$ f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}$$

**Random Tidbits:**
Sine function is an odd function and satisfies $f(-x) = -f(x)$ and cosine is an even function that statisfies $f(-x)=f(x)$. The Integral of $-\pi$ to $\pi$ of odd function is 0 and even function is 2 times. All even functions $f(x)$ will have cosine basis functions in their fourier series and odd functions will have sine basis functions.

## Fourier Transform
We can convert the function from a time domain to frequency domain by using the Fourier transform given as

$$ x(i\omega) = \int_{-\infty}^{\infty} x(t) e^{-i\omega t} dt $$

or the inverse transform

$$ x(t) = \int_{-\infty}^{\infty} x(i\omega) e^{-i\omega t} d\omega $$


# Probability Review

## Definitions
### Sample Space (S)
Set of all possible outcomes of an experument.

### Event (E)
Event is a subset of the sample space.

### Probability
Defined as P(E), is the odds that the event E will occur. Defined as 

$$ \frac{no \textunderscore of \textunderscore favorable \textunderscore outcomes}{no \textunderscore of \textunderscore possible \textunderscore
 outcomes} $$

This is a naive definition that assumes all outcomes are equally likely and it is the finite sample space. Naive definition works some cases but the equally likely is a very strong assumption.

## How do we count?
### Multiplication rule
If there are $n_1$ outcomes from expeirment 1 and for each outcome of experiement 1 we have $n_2$ outcomes for experiment 2 and consequenty after $r-1$ experiments we have $n_r$ outcomes then the total overall possible outcomes of all the combined experiments are $n_1\*n_2\*n_3...*n_r$

**Example**
If you have ice-cream with two things to experiment. Once is choose a cone and the second choose a flavor. You can get the ice cream with or without cone in three flavors which is vanilla, chocolate and strawberry. The total number of outcomes for all choices is 6 as shown below:

| Choice of Cone | Choice of Flavor |
|----------------|------------------|
| No Cone        | Strawberry       |
| No Cone        | Chocolate        |
| No Cone        | Vanilla          |
| Cone           | Strawberry       |
| Cone           | Chocolate        |
| Cone           | Vanilla          |


## Permuatations
"The combination to the safe is 427" In this case the order in which the numbers are entered matter. A permutation is an ordered combination.
There are two types of permutations:
* Repetition is allowed: Suppose we make $r$ choices from $n$ items.<br /> **Example:** We choose three numbers $(r=3)$ from 0 through 9 numbers $(n=10)$ and we are allowed to choose the same number when making each choice. For each choice we have $n$ options and hence the total number of choices are $$^nP_r=n\*n\*n ...= n^r$$
* Repitition is not allowed: Suppose we make $r$ choices from $n$ items.<br /> **Example:** We choose three numbers $(r=3)$ from 0 through 9 numbers $(n=10)$ and we are not allowed choose the same number when making each choice. For each choice the number of options decrease by the number of prior choices made or 

$$^nP_r = n\*(n-1)\*(n-2)\*...(n-r+1) = \frac{n!}{(n-r)!}$$

## Combinations
"My fruit salad is a combination of apples, grapes and bananas" We do not care about the order of items in the salad and repetition is allowed. There are two types of combinations:
* Repetition is not allowed: Suppose we make $r$ choices from $n$ items.<br /> **Example:** We choose the three characters (a,b,c) from a set of 27 characters (a .. z). In permutations the order matters and we have 6 more choices we consider vs. combinations where order does not matter. We overcount by 6 or the number of ways a,b,c (3x2x1) can be placed as shown below. 

| All Choices where order matters | Choices where order does not matter |
|---------------------------------|-------------------------------------|
| a,b,c                           |                                     |
| a,c,b                           |                                     |
| b,a,c                           | a,b,c                               |
| b,c,a                           |                                     |
| c,b,a                           |                                     |
| c,a,b                           |                                     |

We adjust the permutations to reduce the number of times we have overcounted due to the order.

$$ ^nC_r = \frac{n!}{(n-r)!} \cdot \frac{1}{r!} $$

This is also know as the **binomial coefficient**.


## Types of probability

## Birthday Paradox


## References
- [Taylor Series: Essence of Caclulus](https://www.youtube.com/watch?v=3d6DsjIBzJ4)
- [Taylor’s Series of sin x](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/242ad6a22b86b20799afc7f207cd4271_MIT18_01SCF10_Ses99c.pdf)
- [What's so special about Euler's number e?](https://www.youtube.com/watch?v=m2MIpDrF7Es&t=55s)
- [Introduction of Fourier Series](https://www.youtube.com/watch?v=vA9dfINW4Rgurl)
- [Examples of Fourier Series](https://www.youtube.com/watch?v=lL0oUZGMhXc)
- [Fourier Transform Explained](https://www.youtube.com/watch?v=8V6Hi-kP9EE)
- [Stat 110 : Probability](https://www.youtube.com/watch?v=KbB0FjPg0mw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=1)
- [Permutations and Combinations Review](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)
- [Desmos Graphing Calculator](https://www.desmos.com/calculator)
