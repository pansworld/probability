# Mathematics Review

## The beauty of e
The genesis of e is interesting. Consider $f(x)=2^x$. The plot is shown below:


To find the slope we increment $x$ by $dx$ and measure the rate of change as

$$ \frac{df(x)}{dx} =  \frac{2^{x+dx} - 2^x}{dx} $$


$$ \frac{df(x)}{dx} =  \frac{2^x (2^{dx} - 1)}{dx} $$

The fraction $\frac{2^{dx} - 1}{dx}$ varies at a particular starting value of $x$ depending on incremental change in $dx$. For example for for $dx=0.000091$ it's value is $0.693169041631$ and for $dx=0.000001$ it's value decreases slightly to $0.693147420794$. 

Now consider $f(x)=2.71828^x$. The fraction $\frac{2.71828^{dx} - 1}{dx}$ has a value $1.00004482867$ for $dx=0.000091$ and a value $0.999999827389
$ for $dx=0.000001$ or it is $\approx 1$



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


## Euler's formula

## Fourier Transform

## References
[Taylor Series: Essence of Caclulus](https://www.youtube.com/watch?v=3d6DsjIBzJ4)

[Taylor’s Series of sin x](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/242ad6a22b86b20799afc7f207cd4271_MIT18_01SCF10_Ses99c.pdf)
