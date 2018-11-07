# Inspired by https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_fused_probabilityping_problem_newapi.html#example-plot-fused_probabilityping-problem-newapi-py

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import cv2

face = ctrl.Antecedent(np.arange(0, 101, 1), 'face')  # scale 100
voice = ctrl.Antecedent(np.arange(0, 101, 1), 'voice')  # scale 100
fused_probability = ctrl.Consequent(np.arange(0, 101, 1), 'fused_probability')  # scale 100

face.automf(3)
voice.automf(3)

fused_probability['No'] = fuzz.trimf(fused_probability.universe, [0, 0, 45])
fused_probability['Not sure'] = fuzz.trimf(fused_probability.universe, [20, 60, 70])
fused_probability['Yes'] = fuzz.trimf(fused_probability.universe, [35, 90, 100])


rule1 = ctrl.Rule(face['poor'] | voice['poor'], fused_probability['No'])
rule2 = ctrl.Rule(face['poor'] & voice['poor'], fused_probability['No'])
rule3 = ctrl.Rule(face['poor'] & voice['average'], fused_probability['Not sure'])
rule10 = ctrl.Rule(face['poor'] & voice['good'], fused_probability['Not sure'])

rule6 = ctrl.Rule(face['average'] & voice['poor'], fused_probability['No'])
rule7 = ctrl.Rule(face['average'] & voice['average'], fused_probability['Not sure'])
rule9 = ctrl.Rule(face['average'] & voice['good'], fused_probability['Yes'])

rule4 = ctrl.Rule(voice['good'] | face['good'], fused_probability['Yes'])
rule5 = ctrl.Rule(voice['good'] & face['good'], fused_probability['Yes'])
#rule8 = ctrl.Rule(face['good'] & voice['average'], fused_probability['Yes'])



# Apply the rules
fused_probabilityping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule9, rule10])

def get_fusion_face_voice_accuracy(face_probability, voice_probablity, show_graphs = False):

    # View the graph
    if show_graphs:
        face['average'].view()
        voice.view()

    # See the rules.
    if show_graphs:
        rule1.view()

    # Simulation
    fused_probabilityping = ctrl.ControlSystemSimulation(fused_probabilityping_ctrl)

    fused_probabilityping.input['face'] = face_probability
    fused_probabilityping.input['voice'] = voice_probablity

    # Crunch the numbers
    fused_probabilityping.compute()

    if show_graphs:
        fused_probability.view(sim=fused_probabilityping)
        cv2.waitKey()

    return fused_probabilityping.output['fused_probability']
    #TODO output as json





# print("35 and 35: " + str(get_fusion_face_voice_accuracy(35, 35, 0)))
# print("90 and 90: " + str(get_fusion_face_voice_accuracy(90, 90, 0)))
# print("25 and 25: " + str(get_fusion_face_voice_accuracy(25, 25, 0)))
# print("90 and 25: " + str(get_fusion_face_voice_accuracy(90, 25, 0)))
# print("25 and 90: " + str(get_fusion_face_voice_accuracy(25, 90, 0)))
#
#
# print("80 and 40: " + str(get_fusion_face_voice_accuracy(80, 40, 0)))
# print("80 and 60: " + str(get_fusion_face_voice_accuracy(80, 60, 0)))
# print("50 and 50: " + str(get_fusion_face_voice_accuracy(50, 50, 0)))
# print("40 and 40: " + str(get_fusion_face_voice_accuracy(40, 40, 0)))
# print("60 and 40: " + str(get_fusion_face_voice_accuracy(60, 40, 0)))
# print("40 and 60: " + str(get_fusion_face_voice_accuracy(40, 60, 0)))
# print("30 and 30: " + str(get_fusion_face_voice_accuracy(30, 30, 0)))
# print("10 and 30: " + str(get_fusion_face_voice_accuracy(10, 30, 0)))
# print("30 and 10: " + str(get_fusion_face_voice_accuracy(30, 10, 0)))
# print("15 and 15: " + str(get_fusion_face_voice_accuracy(15, 15, 0)))
# print("5 and 5: " + str(get_fusion_face_voice_accuracy(5, 5, 0)))


