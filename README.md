# Collection of rheo data of yield stress fluids

* xl folder contain csv files from webplotdigitizer
  * one file per figure even if the figure contains multiple datasets
  * filename google scholar bibtex label + '_figure#'

* yml folder keeps all metadata
  * papers.yml
    * Bibtex from google (could be automatically generated from paper label + Scholarly)

  * figures.yml
    * experiment_type: flow_curve
    * variable: volume_fraction
    * from_paper: dinkgreve2015universal
    * fig_number: 2
    * unit_x: 
    * unit_y:

  * Samples.yml important to enagle meta_analysis i.e. (plot all *carbopol* *flow_curve* with *volume_fraction* larger than 64% and *solvent_viscosity* larger than 0.5 Pa.s)
    * ID
    * ...
    * tags

## Data schema (temporary, to be discussed)

![IMG_20211119_115153](https://user-images.githubusercontent.com/16650466/142611930-bd6be6bc-3b95-4c5a-8a69-3045f3590be8.jpg)
