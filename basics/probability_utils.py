#Probabalitic modeling
import numpy as np;
import itertools;
import math;

#Definition
#Val(X) = set D of all values assumed by X
#|Val(X)| = Number of elements in set D that contains all values assumed by X

#Stage 1
#REPRESENT the world as a collection of random variables X1, X2,...Xn with joint distrbution P(X1,X2, ...Xn)

#Stage 2
#LEARN the distribution of the data
#   How much data do we need?
#   How muhc computation does it take

#Stage 3
#PERFORM INGERENCE or comphte the conditional disributions p(Xi | X1=x1, ...Xm = Xm)
#List of events List(list(event1), list(event2)) Example: [[1,2,3,4,5,6]] or [[1,2,3,4,5,6],[1,2,3,4,5,6]]

class ProbablisticUtilClass():
    def __init__(self, events):
        self.outcome_space = list(itertools.product(*events))
        self.outcome_space_probs = self.find_outcome_space_probabilities(self.outcome_space)
        

    #Outcome space (upper case Omega) (All outcomes of a dice)
    #prob of one outcome = p(outcome)(lower case omega w) (Outcome of one roll)
    #Event is a subset of outcome space (Set of outcomes from 3 dice rolls or even outcomes or odd outcomes)
    #Prob = prob of event is the sum of the probabilities of the outcomes it contains.
    #p(E) = sigma p(w) where w is the outcome in that Event
    #Inputs: Samples = Array of outcome_space
    #Outputs: outcome_space_probabilities = Names array of probabilities
    
    '''
    Find the outcome space probabilities
    Input: List of Outcome Space
    '''
    def find_outcome_space_probabilities(self, outcome_space):
        outcome_space_counts = {}
        for i in outcome_space:
            if i in outcome_space_counts:
                outcome_space_counts[i]=outcome_space_counts[i]+1
            else:
                outcome_space_counts[i]=1
                
        
        for i in outcome_space_counts:
            outcome_space_counts[i]=outcome_space_counts[i]/len(outcome_space)
        
        return outcome_space_counts
            
            
    
    #2 events for dice rools C1={1,2} and C2={2}
    #C1 and C2 are arrays
    #P(C1) = 1/3 (1/6+1/6) and P(C2)= 1/6
    '''
    Get the probability of an event or a list of events
    '''
    def prob_of_event(self, C1):
        event_probs = 0
        for i in C1:
            event_probs = event_probs + self.outcome_space_probs[i]
        
        return event_probs

    #P(C1 intersect C2)=1/6 and P(C1 U C2)=1/3
    #C1 and C2 are arrays
    '''
    Get the probability of intersection between two list of events
    '''
    def prob_of_intersection(self, C1, C2):
        intersection_probs = 0
        for i in C1:
            for j in C2:
                if i == j:
                    intersection_probs = intersection_probs + self.outcome_space_probs[j]
        
        return intersection_probs
                

    #P(C1 intersect C2)=1/6 and P(C1 U C2)=1/3
    #C1 and C2 are arrays
    '''
    Get the probability of union between two list of events
    '''
    def prob_of_union(self, C1, C2):
        union_of_outcomes = {}
        union_probs = 0
        for i in C1:
            union_of_outcomes[i] = 1
        
        for j in C2:
            union_of_outcomes[j] = 1

        for i in union_of_outcomes:
           union_probs=union_probs + self.outcome_space_probs[i]

        return union_probs


    #Independence of events
    #Two events are independent if p(A intersection B)=p(A)p(B)
    '''
    Determine if the two list of events are independent
    '''
    def are_events_independent(self, C1, C2):
        independence=False
        #Caluculate the intersection
        intersection_prob = self.prob_of_intersection(C1,C2)
        event_C1_prob = self.prob_of_event(C1)
        event_C2_prob = self.prob_of_event(C2)
        
        if math.isclose(intersection_prob, event_C1_prob*event_C2_prob, rel_tol=1e-6):
            independence=True
            
        return independence
    

    '''
    Determine the conditional probability of A given B
    Inputs calculate A and B are events
    '''
    def get_conditional_probability(self, A, B):
        #Get the intersection probability
        #Get the C1 probability
        #divide the two
        conditional_probability = self.prob_of_intersection(A, B)/self.prob_of_event(B)

        return conditional_probability

    #Entropy of events
    '''
    Get the entropy given a list of probabilities and returns a list of entropies
    '''
    def get_individual_entropy(self, probabilities):
        entropy = -probabilities*np.log(probabilities)
        
        return entropy

    '''
    Get cross entropy given actual and predicted probabilities
    Inputs: Numpy Arrays of predicted and actula probabilities
    '''
    def get_cross_entropy(self, predicted_probabilities, actual_probabilities):
        cross_entropy = -actual_probabilities*np.log(np.clip(predicted_probabilities,1e-12,1))
        
        return np.sum(cross_entropy)

'''
#Get probs for coin toss
coin = [[1,0]]
coin_exp = ProbablisticUtilClass(coin)
print(coin_exp.outcome_space_probs)
'''

#Get probs for single dice
dice = [[1,2,3,4,5,6]]
dice_exp = ProbablisticUtilClass(dice)

#Intersection Probabilities for two eventsclear
dice_C1 = [(1,),(2,)]
dice_C2 = [(1,)]
print(f'Probability of Events: C1={dice_exp.prob_of_event(dice_C1)} C2={dice_exp.prob_of_event(dice_C2)}')
print(f'Probability of Intersection: {dice_exp.prob_of_intersection(dice_C1, dice_C2)}')
print(f'Probability of Union: {dice_exp.prob_of_union(dice_C1, dice_C2)}')
print(f'Are events independent: {dice_exp.are_events_independent(dice_C1, dice_C2)}')

dice_C1=[(1,)]
dice_C2=[(2,)]
print(f'Are events independent: {dice_exp.are_events_independent(dice_C1, dice_C2)}')

#Get probs for two dice
dice = [[1,2,3,4,5,6],[1,2,3,4,5,6]]
dice_exp = ProbablisticUtilClass(dice)
#print(dice_exp.outcome_space)

#Intersection Probabilities for two events
dice_C1 = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6)]
dice_C2 = [(1,2),(2,2),(3,2),(4,2),(5,2),(6,2)]
print(f'Probability of Events: C1={dice_exp.prob_of_event(dice_C1)} C2={dice_exp.prob_of_event(dice_C2)}')
print(f'Probability of Intersection: {dice_exp.prob_of_intersection(dice_C1, dice_C2)}')
print(f'Probability of Union: {dice_exp.prob_of_union(dice_C1, dice_C2)}')
print(f'Are events independent: {dice_exp.are_events_independent(dice_C1, dice_C2)}')
print(f'Conditional Probability C1 given C2: {dice_exp.get_conditional_probability(dice_C1, dice_C2)}')
print(f'Conditional Probability C2 given C1: {dice_exp.get_conditional_probability(dice_C2, dice_C1)}')

dice_C1=[(1,1)]
dice_C2=[(2,1),(3,1)]
print(f'Probability of Events: C1={dice_exp.prob_of_event(dice_C1)} C2={dice_exp.prob_of_event(dice_C2)}')
print(f'Are events independent: {dice_exp.are_events_independent(dice_C1, dice_C2)}')
prob_c1 = dice_exp.prob_of_event(dice_C1)
prob_c2 = dice_exp.prob_of_event(dice_C2)
print(f'Cross Entropy: {dice_exp.get_individual_entropy(np.array([prob_c1, prob_c2]))}')

'''
Cross-entropy
'''
predicted_probabilities=np.array([0.1,0.5,0.3,0.1])
actual_probabilities=np.array([0.5,0.1,0.1,0.3])
print(f'Cross Entropy (Flipped probs): {dice_exp.get_cross_entropy(predicted_probabilities,actual_probabilities)}')

predicted_probabilities=np.array([0.3,0.2,0.1,0.2])
actual_probabilities=np.array([0.5,0.1,0.1,0.3])
print(f'Cross Entropy (Closer): {dice_exp.get_cross_entropy(predicted_probabilities,actual_probabilities)}')

predicted_probabilities=np.array([0.5,0.1,0.1,0.3])
actual_probabilities=np.array([0.5,0.1,0.1,0.3])
print(f'Cross Entropy (Equal - Best case): {dice_exp.get_cross_entropy(predicted_probabilities,actual_probabilities)}')

'''
Categorical cross-entropy
'''
predicted_probabilities=np.array([0.5,0.1,0.1,0.3])
actual_probabilities=np.array([0,1.0,0.0,0.0])
print(f'Categorical Cross Entropy (Wrong Category): {dice_exp.get_cross_entropy(predicted_probabilities,actual_probabilities)}')

predicted_probabilities=np.array([0.0,0.9,0.05,0.05])
actual_probabilities=np.array([0,1.0,0.0,0.0])
print(f'Categorical Cross Entropy (Close to category): {dice_exp.get_cross_entropy(predicted_probabilities,actual_probabilities)}')

predicted_probabilities=np.array([0.0,1.0,0,0])
actual_probabilities=np.array([0,1.0,0.0,0.0])
print(f'Categorical Cross Entropy (Matches category): {dice_exp.get_cross_entropy(predicted_probabilities,actual_probabilities)}')

