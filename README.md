# Collection of rheo data of yield stress fluids

Using sqlite
https://www.pythonforthelab.com/blog/storing-data-with-sqlite/

* xl folder contain csv files from webplotdigitizer
** one file per figure even if the figure contains multiple datasets
** filename google scholar bibtex label + '_figure#'

* yml folder keeps all metadata
** papers.yml
*** Bibtex from google (could be automatically generated from paper label + Scholarly)

** figures.yml
*** experiment_type: flow_curve
*** variable: volume_fraction
*** from_paper: dinkgreve2015universal
*** fig_number: 2
*** unit_x: 
*** unit_y:

** Samples.yml important to enagle meta_analysis i.e. (plot all **carbopol** **flow curve** with **vol fraction** larger than 64% and **solvent viscosity** larger than 0.5 Pa s)
*** ID
*** ...
*** tags

