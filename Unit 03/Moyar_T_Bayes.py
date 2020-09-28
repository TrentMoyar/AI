from pomegranate import *

#Parent node: Probaility of graduation
graduate_prob = DiscreteDistribution({'graduated':0.9, 'not_graduated':0.1})
#Child node: Probaility of company one  acceptance
company_one = ConditionalProbabilityTable([
   ['graduated','accepted',0.5],
   ['graduated','rejected',0.5],
   ['not_graduated','accepted',0.05],
   ['not_graduated','rejected',0.95]], [graduate_prob]
)
#Child node: Probaility of company two acceptance
company_two = ConditionalProbabilityTable([
   ['graduated','accepted',0.75],
   ['graduated','rejected',0.25],
   ['not_graduated','accepted',0.25],
   ['not_graduated','rejected',0.75]], [graduate_prob]
)
s_one = State(graduate_prob, name='grad')
s_two = State(company_one, name='comp_one')
s_three = State(company_two, name='comp_two')
model = BayesianNetwork('pop_quiz')
model.add_states(s_one,s_two,s_three)
model.add_edge(s_one,s_two)
model.add_edge(s_one,s_three)
model.bake()
# Probability company 2 accepted given that you graduated and company one rejected you
print(model.predict_proba({'comp_one':'rejected','grad':'graduated'})[2].parameters[0]["accepted"])

# Probability you graduated given that company one and company two accepted you
print(model.predict_proba({'comp_one':'accepted','comp_two':'accepted'})[0].parameters[0]["graduated"])

# Probability you graduated given that company one rejected you and company two accepted you
print(model.predict_proba({'comp_one':'rejected','comp_two':'accepted'})[0].parameters[0]["graduated"])

# Probability you graduated given that company one and company two rejected you
print(model.predict_proba({'comp_one':'rejected','comp_two':'rejected'})[0].parameters[0]["graduated"])

# Probability company one accepted you given that company two accepted you
print(model.predict_proba({'comp_one':'accepted'})[2].parameters[0]["accepted"])

print()
#Parent node: Probability it is sunny
sunny_prob = DiscreteDistribution({'sunny':0.7, 'not_sunny':0.3})
#Parent node: Probability you get a raise
raise_prob = DiscreteDistribution({'raise':0.01, 'no_raise':0.99})
#Child node: Probability you are happy
happy_prob = ConditionalProbabilityTable([
   ['sunny','raise','happy',1.0],
   ['sunny','raise','not_happy',0],
   ['not_sunny','raise','happy',0.9],
   ['not_sunny','raise','not_happy',0.1],
   ['sunny','no_raise','happy',0.7],
   ['sunny','no_raise','not_happy',0.3],
   ['not_sunny','no_raise','happy',0.1],
   ['not_sunny','no_raise','not_happy',0.9]], [sunny_prob,raise_prob]
)
s_one = State(happy_prob, name='happy_prob')
s_two = State(sunny_prob, name='sunny_prob')
s_three = State(raise_prob, name='raise_prob')
model = BayesianNetwork('happiness')
model.add_states(s_one,s_two,s_three)
model.add_edge(s_two,s_one)
model.add_edge(s_three,s_one)
model.bake()
#Probability that you get a raise given that it is sunny
print(model.predict_proba({'sunny_prob':'sunny'})[2].parameters[0]["raise"])

#Probability that you get a raise given that you are happy and it is sunny
print(model.predict_proba({'happy_prob':'happy','sunny_prob':'sunny'})[2].parameters[0]["raise"])

#Probability that you get a raise given that you are happy
print(model.predict_proba({'happy_prob':'happy'})[2].parameters[0]["raise"])

#Probability that you get a raise given that you are happy and it is not sunny
print(model.predict_proba({'happy_prob':'happy','sunny_prob':'not_sunny'})[2].parameters[0]["raise"])