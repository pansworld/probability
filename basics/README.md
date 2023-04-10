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
If there are $n_1$ outcomes from experiment 1 and for each outcome of experiement 1 we have $n_2$ outcomes for experiment 2 and consequenty after $r-1$ experiments we have $n_r$ outcomes then the total overall possible outcomes of all the combined experiments are $n_1\*n_2\*n_3...*n_r$

**Example**
If you have ice-cream with two things to experiment. One is to choose a cone (2 outcomes) and the second is to choose a flavor. You can get the ice cream with or without cone in three flavors which is vanilla, chocolate and strawberry (3 outcomes). The total number of outcomes for all choices is 6 as shown below:

| Choice of Cone | Choice of Flavor |
|----------------|------------------|
| No Cone        | Strawberry       |
| No Cone        | Chocolate        |
| No Cone        | Vanilla          |
| Cone           | Strawberry       |
| Cone           | Chocolate        |
| Cone           | Vanilla          |


### Permuatations
"The combination to the safe is 427" In this case the order in which the numbers are entered matter. A permutation is an ordered combination.
There are two types of permutations:
* Repetition is allowed: Suppose we make $r$ choices from $n$ items.<br /> **Example:** We choose three numbers $(r=3)$ from 0 through 9 numbers $(n=10)$ and we are allowed to choose the same number when making each choice. For each choice we have $n$ options and hence the total number of choices are $$^nP_r=n\*n\*n ...= n^r$$
* Repitition is not allowed: Suppose we make $r$ choices from $n$ items.<br /> **Example:** We choose three numbers $(r=3)$ from 0 through 9 numbers $(n=10)$ and we are not allowed choose the same number when making each choice. For each choice the number of options decrease by the number of prior choices made or 

$$^nP_r = n\*(n-1)\*(n-2)\*...(n-r+1) = \frac{n!}{(n-r)!}$$

### Combinations
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

### Birthday Paradox
Interesting example to study. The problem statement is "What is the probability that at least 2 out of n people in a room have the same birthday?" The best way to approach it is to determine the probability that none of the n people share the same birthday. So if $A$ is the event that at least one pair has the same birthday then $A^c$ represents the complement where no one has a shared birthday.

$$
P(A) = 1 - P(A^c)
$$


**Questions for total number of ways in which we can pick n birthdays:**
1. Does order matter? 
Yes. We could pick John first and then Fred or pick Fred first, then Sandy and then John.
2. Are repetitiions allowed? 
Yes. We are picking n dates from 365 dates. If we get day 1 as a birthday for person 1 then we can also have day 1 as a birthday for person 2. Hence they are all equally likely.

Hence, the number of permutations for picking n birthdays from 365 is $365^n$.

**Questions for total number of ways in which we can pick n birthdays such that two birthdays are not repeated:**
1. Does order matter? 
Yes. We could pick John first and then Fred or pick Fred first, then Sandy and then John.
2. Are repetitiions allowed? 
No. Once we pick a birth date, we cannot have another person with the same birth date. 

Hence, the number of permutations for picking non-repeating n birthdays from 365 is $\frac{365!}{(365-n)!}$.

Hence the probability of at least one birthday being shared between n people can be given as:

$$
P(A) = 1 - \frac{365!}{(365-n)!}.\frac{1}{365^n}
$$

## Inclusion Exclusion
If we have two interseting events $A$ and $B$ within sample space $S$ then the probability of the union of the two events (at least one outcome from the two events occuring) is given as

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

For three $A_1,A_2,A_3$ we can define it as 

$$
P(A_1 \cup A_2 \cup A_3) = P(A_1) + P(A_2) + P(A_3) - P(A_1 \cap A_2) - P(A_1 \cap A_3) - P(A_2 \cap A_3) + P(A_1 \cap A_2 \cap A_3)
$$

For n events $A_1..A_n$ we can generalize it as

$$
P(A_1 \cup A_2..\cup A_n) = \sum_{i=1}^{n} P(A_i) - \sum_{i=1, j=2, i \lt j}^{n} P(A_i \cap A_j) + \sum_{i=1,j=2,k=2, i \lt j \lt k }^{n} P(A_i \cap A_j \cap A_k) .. (-1)^{n+1} P(A_1 \cap A_2 .. \cap A_n)
$$

### De Montmort matching problem
**Problem statement:** A deck of cards is labeled from 1 to n. As you flip each card you call out the card number. Find the probability that you call out the same card number as the one that is being flipped. Essentially, if $A_i$ is the event that the $i^{th}$ card is the winning card then the probability we are trying to compute is $P(\cup_{i=1}^{n} A_i)$. (Reproduced from Stat 110 Lectures 3 & 4. See link below)

**Strategy for finding the union.**
* We find the probability of the intersection from $1..k$ intersection of $P(A_1 \cap A_2 \cap .. A_k)$
* Use the generic intersection and summation expansion of the inclusion/exclusion for a union.

The probability of intersection can be given as:

$$
P(A_1 \cap A_2 .. \cap A_k) = \frac{(n-k)!}{n!}
$$

The denominator $n!$ since the total number of outcomes is the permutation of arranging n cards (without repetition - if we place one card we cannot reuse it. We are choosing n to place n cards out of n or $^nP_n$). In the numerator $k$ cards are fixed and we are finding the permutation of placing $n-k$ cards out of a total of $n-k$ cards or $^{(n-k)}P_{(n-k)}$.

Now we use the expansion. Notice that each summation contains a list of intersections which are non-repeating and order does not matter. For example $P(A_1 \cap A_2) = P(A_2 \cap A_1)$. Hence the $k_th$ summation term a choice of $k$ events from $n$ events or $^nC_k$ or $\frac{n!}{(n-k)!}.\frac{1}{k!}$

The $k_{th}$ term of the inclusion exclusion can be given as

$$
\sum_{(i \lt j \lt.. \lt m) and (i=1, j=2 ..m=k)}^{n} P(A_i \cap A_j \cap .. A_m) = \frac{(n-k)!}{n!}.\frac{n!}{(n-k)!}.\frac{1}{k!}
$$

$$
\sum_{(i \lt j \lt .. \lt m) and (i=1, j=2 ..m=k)}^{n} P(A_i \cap A_j \cap .. A_m) = \frac{1}{k!}
$$

The final inclusion exclusion summation will be:

$$
P(A_1 \cup A_2 \cup .. A_n) = 1 - \frac{1}{2!} + \frac{1}{3!} - .. (-1)^{(n+1)}\frac{1}{n!}
$$

Using the taylor series can be approximated to 

$$
P(A_1 \cup A_2 \cup .. A_n) = 1 - e^{-1}
$$


## Independence
### Definition
Two events are independent if the satisfy the following condition

$$
P(A \cap B) = P(A)P(B)
$$

This is different than disjoint since there is a dependence between A and B if they are disjoint. For example: If A occurs then B does not occur. Hence not independent.

For more than one events the following have to be true

$$
P(A \cap B \cap C)=P(A)P(B)P(C)
$$

$$
P(A \cap B)=P(A)P(B)
$$

$$
P(A \cap C)=P(A)P(C)
$$

$$
P(B \cap C)=P(B)P(C)
$$

### Newton Pepy's Problem
**Problem statement**: 

What are the probabilities for
* Getting at least 1 six in 6 independent die
* Getting at least 2 sixes in 12 independent die
* Getting at least 3 sixes in 18 independent die

**Solution**

Let $E$ be the event we get a six. Our general strategy is to find the complement of the desired outcomes with the different die sets.

**Case 1**

For a single die the probability of not getting a six is
$$P(E^{c})=\frac{5}{6}$$ 
For six die, since the die are fair and the roll of the die is independent the probability of not getting a single six with six die is $(\frac{5}{6})^6$. Hence the probability 

$$P(E=at \textunderscore least \textunderscore one \textunderscore six)=1 - (\frac{5}{6})^6$$

**Case 2**

For 12 die the probability the complement is the probability that we donot get a six and **we get exactly one six**
$$P((E=at \textunderscore least \textunderscore two \textunderscore six)^c)=(\frac{5}{6})^6  + ^{12}C_1 . ((\frac{1}{6}) . (\frac{5}{6})^{11})$$

Hence the probability of getting at least two sixes in a 12 die experiment is

$$P((E=at \textunderscore least \textunderscore two \textunderscore six))=1 - (\frac{5}{6})^6  - ^{12}C_1 . (\frac{1}{6}) . (\frac{5}{6})^{11}$$

**Case 3**

We can generalize case 3 as

$$P(E=at \textunderscore least \textunderscore three \textunderscore six)=1 - \sum_{k=0}^2 (^nC_k . ((\frac{1}{6}^k) . (\frac{5}{6})^{18-k}))$$

## Conditional Probability
How should you **update your belief / probability / undertainty** based on new evidence?

**Notation**

A conditional probability is specified as $P(A | B)$ which is read as the probability of A given B has occurred.

**Intuition**

Consider 9 pebbles in a box. Consider we define 4 pebbles as event B occurring and 5 pebbles as event A occurring. We assume that the total of all 9 pebbles is 1 unit. There is one overlapping pebble between A and B. Per the definition of conitional probability of we consider only the pebbles in event B (or B has occured) then all the other 5 pebbles are no longer considered to be part of the event space or the event space shrinks to the 4 pebbles the signify event B. The pebbles for A is now reduced to the 1 pebble that overlaps with B. 

$$P(A | B)=\frac{1}{4}$$

$$P(A | B)=\frac{\frac{1}{9}}{\frac{4}{9}}$$

$$P(A | B)=\frac{P(A \cap B)}{P(B)}$$

**Bayes Rule**

Consider,

$$P(A \cap B)=P(A | B)P(B)$$

$$P(B \cap A)=P(B | A)P(A)$$

Since $P(A \cap B)=P(B \cap A)$ we can write

$$P(A | B)P(B)=P(B | A)P(A)$$

$$P(A | B)=\frac{P(B | A)P(B)}{P(A)}$$

**Chain Rule**

Using Bayes rule for $n$ events we can write the intersection of events as

$$P(A_1 \cap A_2 \cap ... \cap A_n) = P(A_n | A_1 \cap A_2 \cap .. A_{n-1})P(A_1 \cap A_2 \cap .. A_{n-1})$$

$$P(A_1 \cap A_2 \cap ... \cap A_n) = P(A_n | A_1 \cap A_2 \cap .. A_{n-1})P(A_{n-1} | A_1 \cap A_2 \cap .. A_{n-2})P(A_1 \cap A_2 \cap .. A_{n-2})$$

$$P(A_1 \cap A_2 \cap ... \cap A_n) = P(A_n | A_1 \cap A_2 \cap .. A_{n-1})P(A_{n-1} | A_1 \cap A_2 \cap .. A_{n-2}) ... P(A_2 | A_1)P(A_1)$$

$$P(A_1 \cap A_2 \cap ... \cap A_n) = \prod_{i=1}^{k} P( A_k | \cap_{j=1}^{k-1} A_j )$$

### Law of Total Probability 

The law of total proability relates marginal proability to conditional probabilities. Consider the following. We have a sample space $S$ with events $B$. The sample space is also partitioned into events $A_1,A_2,A_3...A_n$ which also interset with $B$. The the marginal probability $P(B)$ is given as

$$
P(B) = \sum_{k=1}^{n} P(B | A_k)
$$

### Example illustrating why conditional probabilities are important

We are dealt two cards.

**Problem Statement 1**
What is the probability that we have two aces given that the first card is an case $P(\text{two aces} | \text{have an ace})$? We are going to assume that ordering is not important. "Have an ace" can be seen as "at least one card is an ace"

$$ 
P(\text{two aces} | \text{have an ace}) = \frac{P(\text{two aces} \cap \text{first card is an ace})}{P(\text{have an ace})}
$$

$P(\text{two aces} \cap \text{have an ace})$ is the same as having two aces or $P(\text{two aces})$

$$ 
P(\text{two aces} | \text{have an ace}) = \frac{P(\text{two aces})}{P(\text{have an ace})}
$$

$$ 
P(\text{two aces} | \text{have an ace}) = \frac{P(\text{two aces})}{1 - P(\text{**do not** have an ace})}
$$

$$ 
P(\text{two aces} | \text{have an ace}) =  \frac{\frac{^4C_2}{^52C_2}}{1 - \frac{^48C_2}{^52C_2}} = \frac{1}{33}
$$

**Problem Statement 2**
What is the proability that the second card is an ace given that the once of the cards is an ace of spades $P(two aces | one of the cards is an ace of spade)$?

We have assumed that order does not matter we have to choose from 3 aces (since we know that one card is already known) and we have to choose from 51 cards.

$$
$P(two aces | one of the cards is an ace of spade)$ = \frac{3}{51} = \frac{1}{17}
$$

**Insight:** Knowing that the card that we have is an ace of spade rather than one of the cards is an ace doubles the probability of the second card being an ace. Essentially, the more evidence the more we know about the probability of an outcome. That is why conditioning is important. It is also important to know what to condition on. It is a fallacy to think that $P(A|B) = P(B|A)$. **In fact, $P(A|B) \ne P(B|A)$ but they are related by Bayes rule.** 

**Probability of innocence given the evidence**

Assume that there is a theft.  The thief is described as a male, $5^{'}6^{"}$ in height and is read headed. The prosecution catches a person and claims that there is a $\frac{1}{50000}$ chance that a person matching this description is innocent. Hence he must be guilty.

$$
P(male, 5^{'}6^{"} in height | innocence) = \frac{1}{50,0000}
$$

What we are really interested in is 

$$
P(innocence | male, 5^{'}6^{"} in height ) = \frac{P(innocence \cap male, 5^{'}6^{"} in height)}{P(male, 5^{'}6^{"} in height)}
$$

$$
P(innocence | male, 5^{'}6^{"} in height ) = \frac{P(male, 5^{'}6^{"} in height | innocence)P(innocence)}{P(male, 5^{'}6^{"} in height)}
$$

$P(innocence) \approx 1$ and $P(male, 5^{'}6^{"} in height)$ is likely to be low given the number of people in the city etc., the $P(innocence | male, 5^{'}6^{"} in height )$ is likely to be high. The prosecutor's fallacy ignores the prior probabilites and assumes $P(A|B) = P(B|A)$

**Note:** $P(A)$ is call the prior probability and $P(A | B)$ is the posterior probability given that the event $B$ has occurred.


### Example illustrating why how conditional probabilities impact the outcome
Suppose that 1% of the population have a disease. A test for the disease is 95% accurate. If a person gets a positive result, then what is the probability that they have the disease. 

Let,

$T$: event that the test result is positive.

$T^c$: event that the test result is negative

$D$: event that the person has the disease

$D^c$: event that the perons does not have the disease

We are interested in finding $P(D|T)$. We start with the Bayes rule

$$
P(D|T) = \frac{P(T|D)P(D)}{P(T)}
$$

By law of total probability

$$
P(T) = P(T|D)P(D) + P(T|D^c)P(D^c)
$$

Hence,

$$
P(D|T) = \frac{P(T|D)P(D)}{P(T|D)P(D) + P(T|D^c)P(D^c)}
$$

$$
P(D|T) = \frac{0.95 \cdot 0.01}{0.95 \cdot 0.01 + 0.05 \cdot 0.99} = 0.16
$$

Or there is a 16% probability that if the test is positive the person has the rare disease. Most people focus on $P(T|D)$ but ignore the fact that the disease itself is rare $P(D)=0.01$ and how it plays into the overall probability. 

## Conditional Independence
Two events $A$ and $B$ are said to be conditionally independent give that even $C$ occurred if:

$$
P(A \cap B | C) = P(A)P(B)
$$

### Are A and B independent if their conditional probabilities given C are independent?
You are playing chess with a person. You play a few games and you have an idea of the strength of the person. Given then you know their strengths each game is now conditionally independent, since you already know the player well. But unconditionally, especially in the beginning the games are not independent since each game informs you about the strength of the person.

Summarizing...

$$
P(Game_1, Game_2 | known strength) = P(Game_1)P(Game_2)
$$

But 

$$
P(Game_1, Game_2) \ne P(Game_1)P(Game_2)
$$

Since outcome of $Game_1$ gives you more knowledge about the person and you are likely to change how you play $Game_2$.

### Given that A and B are independent are they conditionally independent given C?
Suppose a fire alarm ($C$) can go off because of a fire ($A$) or someone making food ($B$). The $P(Fire)$ and $P(Someone making food)$ is independent. But they are conditionally dependent given that the Alarm goes off. For example to explain the proability of fire $P(A | C \cap B^{c}) = 1$ or the fire can be explained as alarm and no one is making food.  

### Monty Hall problem
The setup. There are three doors. There is a car behind one door and two goats behind the other two. You choose one door. Monty Hall then opens one of the other two doors and asks if you want to switch. The question what should be your strategy. Should you switch? The following conditions are assumed:

- Monty Hall knows which door has the car
- Monty Hall will open the door which does not have the car
- If both doors do not have the car then Monty Hall is likely to open the door with equal probability

To determine our strategy we need to find the probability that the car is behind one of the other two doors. Let's assume that we always choose door 1. The prior probability after we choose door 1 for each door is $\frac{1}{3}$


**Using Law of total probability**
Let's assume that our strategy is to always switch. The by law of total probability the probability of switching can be written as

$$
P(switching) = P(switch|car=door1)P(door1) + P(switch|car=door2)P(door2) + P(switch|car=door3)P(door3)
$$

$$
P(switching) = 0 + \frac{1}{3} + \frac{1}{3} = \frac{2}{3}
$$

**Using graphical analysis**

<img src="https://github.com/pansworld/probability/blob/b4aaf33dd9ad6d23b05a6c5996823f0a5c04b216/basics/images/monty_hall.png" width="25%" height="25%"> 

Looking at the diagram if Monty Hall opens door 

$$
P(C=1 | M=2) = \frac{1}{2}.\frac{1}{3} = \frac{1}{6}
$$

$$
P(C=1 | M=3) = \frac{1}{2}.\frac{1}{3} = \frac{1}{6}
$$

$$
P(C=3 | M=2) = 1.\frac{1}{3} = \frac{1}{3}
$$

$$
P(C=2 | M=3) = 1.\frac{1}{3} = \frac{1}{3}
$$

We renormalize since we are conditioning on partial outcomes by multiplying P(C=1 | M=2) with 2 ($\frac{1}{\frac{1}{2}}$). Hence,

$$
P(C=1 | M=2) = \frac{1}{3}
$$

$$
P(C=3 | M=2) = \frac{2}{3}
$$


### Simpsons Paradox
Consider the following example where we have two doctors. Dr. Hibbert and Dr. Nick

| Result   |Dr. Hibbert Surgery  | Dr. Hibbert Band Aid |
|----------|---------------------|----------------------|
| Success  |                   70|                    10|
| Failure  |                   20|                     0|


| Result   |Dr. Nick Surgery     | Dr. Nick Band Aid    |
|----------|---------------------|----------------------|
| Success  |                    2|                    81|
| Failure  |                    8|                     9|

In the above case the success rate given surgery and band aid for each doctor is given by:

$$
P(Dr. Hibbert Success | Surgery) = \frac{7}{9}
$$

$$
P(Dr. Hibbert Success | Band Aid) = \frac{10}{10}
$$

$$
P(Dr. Nick Success | Surgey) = \frac{2}{10}
$$

$$
P(Dr. Nick Success | Band Aid) = \frac{81}{90}
$$

Aggregating or unconditionally the probability of success for Dr. Hibbert and Dr. Nick are given as follows:

$$
P(Dr. Hibbert Success) = \frac{80}{100}
$$


$$
P(Dr. Nick Success) = \frac{83}{100}
$$

The paradox is that given the overall success Dr. Nick might seem better than Dr. Hibbert but given under conditions Dr. Hibbert is clearly the better overall doctor. This is why conditioning is important.
$$
\frac{2}{5} + \frac{1}{3} \ne \frac{3}{8}
$$

Let events defined as $A: Success$, $B: Nick$ and $C: Surgery$ then we get

$$
P(A | B, C) < P(A|B^c, C)
$$

$$
P(A | B, C^c) < P(A|B^c, C^c)
$$

Aggregating the probabilities gives,

$$
P(A | B) > P(A|B^c)
$$

The ineqality flips when the condition on type of event $C$ is taken away. Here $C$ is called the $Confounder$. 

By law of total probability,

$$
P(A | B) = P(A | B,C)P(C|B) + P(A|B,C^c)P(C^c|B)
$$

Here $P(C|B)$ and $P(C^c|B)$ act was weights and influence the outcome.

**Note** From Lecture 6 of Harvard Stat 110.


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
