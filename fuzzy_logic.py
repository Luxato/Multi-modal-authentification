# Inspired by https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html#example-plot-tipping-problem-newapi-py

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import cv2

# New Antecedent/Consequent objects hold universe variables and membership
# functions
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')  # scale 10
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')  # scale 10
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')  # scale 25

# Auto-membership function population is possible with .automf(3, 5, or 7)
quality.automf(3)
service.automf(3)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# View the graph
quality['average'].view()
service.view()



rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

print("test111")

#rule1.view()

# Apply the rules
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

print("test123")

# Simulation
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

print("test456")

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

print("test789")

# Crunch the numbers
tipping.compute()

print(tipping.output['tip'])

tip.view(sim=tipping)


cv2.waitKey()