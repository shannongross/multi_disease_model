## Multi-Disease Model
By Shannon M. Gross
MSc Engineering and Policy Analysis

* This repository contains master's thesis work to complete Engineering and Policy Analysis program at TU Delft. The thesis can be viewed in the **results** directory.
* The **model** directory contains a system dynamics model for evaluating different public health policy options for combatting multiple infectious diseases in a population. The model is implemented in Vensim DSS. Data used to parameterize the model for a case study in Uganda are synthesized into *data/multi-disease-model-data.xlsx*.
* The model is extensively analyzed using the **exploratory modeling workbench**, which is available at: https://github.com/quaquel/EMAworkbench.
* Specifically, the analysis follows the **MORDM** approach outlined by
Kasprzyk et al. (2013) https://doi.org/10.1016/j.envsoft.2012.12.007. The steps of the MORDM analysis + visualizations can be found in four Jupyter notebooks above.
* The model is extended to consider four different problem formulations, which are specified in*disease_model_problems.py*. These formulations are used to test how subjective decision-maker perspectives can influence the subsequent Pareto-approximate front obtained.
