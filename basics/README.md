# Mathematics Review

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


## Euler's formula

## Fourier Transform
