# -*- coding: utf-8 -*-
import numpy as np
from ema_workbench.connectors.vensim import VensimModel
from ema_workbench import (SequentialEvaluator, MultiprocessingEvaluator,
                           Scenario, CategoricalParameter, Policy, Constant,
                           TimeSeriesOutcome, ScalarOutcome, IntegerParameter,
                           RealParameter)

def avg_over_period(parameter, time_start, time_end):
    index1 = time_start.astype(int)
    index2 = time_end.astype(int)
    period = parameter[index1[0]:index2[0]]
    sum_period = np.sum(period,axis=0)/len(period)
    return sum_period

def change_over_period(parameter, time_start, time_end):
    index1 = time_start.astype(int)
    index2 = time_end.astype(int)
    A = parameter[index1[0]]
    B = parameter[index2[0]]
    delta = -((A-B)/A)
    return delta

def total_over_period(parameter, time_start, time_end):
    index1 = time_start.astype(int)
    index2 = time_end.astype(int)
    period = parameter[index1[0]:index2[0]]
    tot_period = np.sum(period,axis=0)
    return tot_period



def get_model_for_problem_formulation(problem_formulation_idea):
    disease_model = VensimModel("multidisease", wd=r'.\models',
                        model_file='disease_model.vpm')

    disease_model.uncertainties = [
        # Sanitation Unknowns
        IntegerParameter('desire for improved sanitation', 10, 100),
        # Water Supply Unknowns
        IntegerParameter('Cost of well repair', 660, 1800),
        # Water Quality Unknowns
        IntegerParameter('use HWT', 10, 100),
        # Hygiene Unknowns
        IntegerParameter('Intensity of hygiene campaign', 10, 100),
        # Vaccination Unknowns
        IntegerParameter('Reliability of vaccine supply', 10, 100),
        # Treatment Unknowns
        IntegerParameter('seeking treatment', 10, 100),
        # Other Unknowns
        IntegerParameter('percent willing to accept MDA', 10, 100),
        # RealParameter('Childbearing years', 9, 14), #N.B. huge impact
        ]

    disease_model.constants = [
        Constant('Length latrine program', 10),
        Constant('Length GW supply program', 10),
        Constant('Length of water quality program',10),
        Constant("Duration of hygiene campaign",10),
        Constant("Length of ORT subsidy",10),
        Constant("Years of MDA campaign",10)]

    disease_model.levers = [
        # Sanitation Levers
        IntegerParameter("Number of new latrines to build", 0, 9000),
        IntegerParameter("Number of latrines to maintain", 0, 4000),
        # Water Supply Levers
        IntegerParameter("Number of new wells to drill", 0, 2000),
        IntegerParameter("Number of wells to repair", 0, 2000),
        # Water Quality Levers
        IntegerParameter("Availability HWT", 0, 100),
        # Hygiene Promotion Levers
        IntegerParameter("HW stations to build", 0, 8000),
        # Vaccination Levers
        IntegerParameter("percentage of infants to vaccinate", 0, 100),
        # Treatment Levers
        IntegerParameter("Access to tmt", 0, 100),
        # MDA levers
        IntegerParameter("percent adults given MDA", 0, 100),
        IntegerParameter("percent youth given Albendazole", 0, 100),
        ]

        # add policies
    disease_model.policies= [
        Policy('LatrineProgram', **{
                                "Number of new latrines to build":5000,
                                "Number of latrines to maintain":4000,
                                "Length latrine program":10,
                                "Number of new wells to drill":0,
                                "Number of wells to repair":0,
                                "Length GW supply program":0,
                                "Availability HWT":0,
                                "Length of water quality program":0,
                                "HW stations to build":0,
                                "Duration of hygiene campaign":0,
                                "percentage of infants to vaccinate":0,
                                "Access to tmt":0,
                                "Length of ORT subsidy":0,
                                "percent adults given Albendazole":0,
                                "percent youth given Albendazole":0,
                                "Years of MDA campaign":0,
                                }),
        Policy('GWsupply', **{
                                "Number of new latrines to build":0,
                                "Number of latrines to maintain":0,
                                "Length latrine program":0,
                                "Number of new wells to drill":1000,
                                "Number of wells to repair":100,
                                "Length GW supply program":10,
                                "Availability HWT":0,
                                "Length of water quality program":0,
                                "HW stations to build":0,
                                "Duration of hygiene campaign":0,
                                "percentage of infants to vaccinate":0,
                                "Access to tmt":0,
                                "Length of ORT subsidy":0,
                                "percent adults given Albendazole":0,
                                "percent youth given Albendazole":0,
                                "Years of MDA campaign":0,
                                }),
        Policy('ORT', **{
                                "Number of new latrines to build":0,
                                "Number of latrines to maintain":0,
                                "Length latrine program":0,
                                "Number of new wells to drill":0,
                                "Number of wells to repair":0,
                                "Length GW supply program":0,
                                "Availability HWT":0,
                                "Length of water quality program":0,
                                "HW stations to build":0,
                                "Duration of hygiene campaign":0,
                                "percentage of infants to vaccinate":0,
                                "Access to tmt":100,
                                "Length of ORT subsidy":10,
                                "percent adults given Albendazole":0,
                                "percent youth given Albendazole":0,
                                "Years of MDA campaign":0,
                                }),
        Policy('Hygiene', **{
                                "Number of new latrines to build":0,
                                "Number of latrines to maintain":0,
                                "Length latrine program":0,
                                "Number of new wells to drill":0,
                                "Number of wells to repair":0,
                                "Length GW supply program":0,
                                "Availability HWT":0,
                                "Length of water quality program":0,
                                "HW stations to build":1000,
                                "Duration of hygiene campaign":10,
                                "percentage of infants to vaccinate":0,
                                "Access to tmt":0,
                                "Length of ORT subsidy":0,
                                "percent adults given Albendazole":0,
                                "percent youth given Albendazole":0,
                                "Years of MDA campaign":0,
                                }),
        Policy('Vaccin', **{
                                "Number of new latrines to build":0,
                                "Number of latrines to maintain":0,
                                "Length latrine program":0,
                                "Number of new wells to drill":0,
                                "Number of wells to repair":0,
                                "Length GW supply program":0,
                                "Availability HWT":0,
                                "Length of water quality program":0,
                                "HW stations to build":0,
                                "Duration of hygiene campaign":0,
                                "percentage of infants to vaccinate":100,
                                "Access to tmt":0,
                                "Length of ORT subsidy":0,
                                "percent adults given Albendazole":0,
                                "percent youth given Albendazole":0,
                                "Years of MDA campaign":0,
                                }),
        Policy('DrinkingWater', **{
                                "Number of new latrines to build":0,
                                "Number of latrines to maintain":0,
                                "Length latrine program":0,
                                "Number of new wells to drill":0,
                                "Number of wells to repair":0,
                                "Length GW supply program":0,
                                "Availability HWT":100,
                                "Length of water quality program":10,
                                "HW stations to build":0,
                                "Duration of hygiene campaign":0,
                                "percentage of infants to vaccinate":0,
                                "Access to tmt":0,
                                "Length of ORT subsidy":0,
                                "percent adults given Albendazole":0,
                                "percent youth given Albendazole":0,
                                "Years of MDA campaign":0,
                                }),
        Policy('MDA', **{
                                "Number of new latrines to build":0,
                                "Number of latrines to maintain":0,
                                "Length latrine program":0,
                                "Number of new wells to drill":0,
                                "Number of wells to repair":0,
                                "Length GW supply program":0,
                                "Availability HWT":0,
                                "Length of water quality program":0,
                                "HW stations to build":0,
                                "Duration of hygiene campaign":0,
                                "percentage of infants to vaccinate":0,
                                "Access to tmt":0,
                                "Length of ORT subsidy":0,
                                "percent adults given Albendazole":100,
                                "percent youth given Albendazole":100,
                                "Years of MDA campaign":10,
                                }),
        Policy('DoNothing', **{
                                "Number of new latrines to build":0,
                                "Number of latrines to maintain":0,
                                "Length latrine program":0,
                                "Number of new wells to drill":0,
                                "Number of wells to repair":0,
                                "Length GW supply program":0,
                                "Availability HWT":0,
                                "Length of water quality program":0,
                                "HW stations to build":0,
                                "Duration of hygiene campaign":0,
                                "percentage of infants to vaccinate":0,
                                "Access to tmt":0,
                                "Length of ORT subsidy":0,
                                "percent adults given Albendazole":0,
                                "percent youth given Albendazole":0,
                                "Years of MDA campaign":0,
                                }),]
    # Problem formulations:
    direction = ScalarOutcome.MINIMIZE
    if problem_formulation_idea == 1: ##PF1: Minimum child (<5 yo) deaths due to Rotavirus
        disease_model.name = 'Minimize Child <5 Rotavirus infections by 2030'
        disease_model.outcomes.clear()
        disease_model.outcomes = [
            ScalarOutcome('Mortality', #Deaths due to Rotavirus
                                variable_name= ['children under 5 deaths[Rota]','ts until 2020','ts at 2030'],
                                function=avg_over_period,
                                kind=direction,
                                expected_range=(10000,250000)),
            ScalarOutcome('Morbidity', #Rota DALYs children
                                variable_name= ["Years Lost to Disability in Children[Rota]",'ts until 2020','ts at 2030'],
                                function=avg_over_period,
                                kind=direction,
                                expected_range=(6000,9000)),
            ScalarOutcome('Timeliness', #Delta child infections 2030
                                variable_name=["Number of Children Infected[Rota]", 'ts until 2020','ts at 2030'],
                                function=change_over_period,
                                kind=direction,
                                expected_range=(-0.9,0.1)),
            ScalarOutcome('CapEx',
                                variable_name=['Upfront Cost', 'ts until 2020', 'ts at 2040'],
                                function=total_over_period,
                                kind=direction,
                                expected_range=(0,3000000000000)),
            ScalarOutcome('OpEx',#Recurring Cost
                                variable_name=['Recurring Cost', 'ts until 2020', 'ts at 2040'],
                                function=total_over_period,
                                kind=direction,
                                expected_range=(0,2000000000000)),
            ]

    elif problem_formulation_idea == 2: ##PF2: Minimum prevalence of ascariasis in Youth (Infants, PreSACs, and SACs) in 5 years
        disease_model.name = 'Minimize Ascariasis in Youth by 2025'
        disease_model.outcomes.clear()
        disease_model.outcomes = [
            ScalarOutcome('Mortality',
                                variable_name=['Youth Mortality[Ascar]', 'ts until 2020','ts at 2025'],
                                function=avg_over_period,
                                kind=direction,
                                expected_range=(1000,20000)),
            ScalarOutcome('Morbidity',
                                variable_name=['Years Lost to Disability in Youth[Ascar]', 'ts until 2020','ts at 2025'],
                                function=avg_over_period,
                                kind=direction,
                                expected_range=(20000,160000)),
            ScalarOutcome('Timeliness', #Change in prevalence of ascariasis in youth by 2025
                                variable_name=['Number of Youth Infected[Ascar]', 'ts until 2020','ts at 2025'],
                                function=change_over_period,
                                kind=direction,
                                expected_range=(-1,0)),
            ScalarOutcome('CapEx', #Upfront Cost
                                variable_name=['Upfront Cost', 'ts until 2020', 'ts at 2040'],
                                function=total_over_period,
                                kind=direction,
                                expected_range=(0,3000000000000)),
            ScalarOutcome('OpEx',#Recurring Cost
                                variable_name=['Recurring Cost', 'ts until 2020', 'ts at 2040'],
                                function=total_over_period,
                                kind=direction,
                                expected_range=(0,2000000000000)),
        ]
    elif problem_formulation_idea == 3: #PF3: Minimum Child (<5 yo) mortality, all diseases, w/in one year
        disease_model.name = 'Immediately minimize Child <5 burden from all causes'
        disease_model.outcomes.clear()
        disease_model.outcomes = [
            ScalarOutcome('Mortality',
                                variable_name=['Total children under 5 deaths','ts until 2020', 'ts at 2021'],
                                function=avg_over_period,
                                kind=direction,
                                expected_range=(50000,400000)),
            ScalarOutcome('Morbidity',
                                variable_name=['morbidity in children','ts until 2020', 'ts at 2021'],
                                function=avg_over_period,
                                kind=direction,
                                expected_range=(40000,100000)),
            ScalarOutcome('Timeliness', #Delta child infections 2021
                                variable_name=['Total children w gastroenteric infection', 'ts until 2020', 'ts at 2021'],
                                function=change_over_period,
                                kind=direction,
                                expected_range=(-0.5,0)),
            ScalarOutcome('CapEx', #Upfront Cost
                                variable_name=['Upfront Cost','ts until 2020', 'ts at 2040'],
                                function=total_over_period,
                                kind=direction,
                                expected_range=(5000000,3000000000000)),
            ScalarOutcome('OpEx',#Recurring Cost
                                variable_name=['Recurring Cost', 'ts until 2020', 'ts at 2040'], #bc no rec cost will show up in 1 yr
                                function=total_over_period,
                                kind=direction,
                                expected_range=(50000000000,2000000000000)),
            ]
    elif problem_formulation_idea == 4: #PF4: Minimum number infected, all diseases, sustainably
        disease_model.name = 'Minimize number infected all diseases by 2040'
        disease_model.outcomes.clear()
        disease_model.outcomes = [
            ScalarOutcome('Mortality',
                                variable_name = ['Total lives lost', 'ts until 2020', 'ts at 2040'],
                                function=avg_over_period,
                                kind=direction,
                                expected_range=(50000,250000)),
            ScalarOutcome('Morbidity',
                                variable_name =['disability burden', 'ts until 2020', 'ts at 2040'],
                                function=avg_over_period,
                                kind=direction,
                                expected_range=(100000,900000)),
            ScalarOutcome('Timeliness', #delta infections 2040
                                variable_name=['Total number of gastroenteric infection', 'ts until 2020', 'ts at 2040'],
                                function=change_over_period,
                                kind=direction,
                                expected_range=(-1,-.45)),
            ScalarOutcome('CapEx', #Upfront Cost
                                variable_name=['Upfront Cost','ts until 2020', 'ts at 2040'],
                                function=total_over_period,
                                kind=direction,
                                expected_range=(20000000000,3000000000000)),
            ScalarOutcome('OpEx',#Recurring Cost
                                variable_name=['Recurring Cost', 'ts until 2020', 'ts at 2040'],
                                function=total_over_period,
                                kind=direction,
                                expected_range=(20000000000,2000000000000)),
                                ##recurring costs divided by 20 years
            ]


    else:
        raise TypeError('unknown problem identifier')
    return disease_model
