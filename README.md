# aad64_Individual-Project1
Continuous Integration using GitHub Actions of Python Data Science Project


![example workflow](https://github.com/nogibjj/aad64_Individual-Project1/actions/workflows/format.yml/badge.svg)![example workflow](https://github.com/nogibjj/aad64_Individual-Project1/actions/workflows/lint.yml/badge.svg)![example workflow](https://github.com/nogibjj/aad64_Individual-Project1/actions/workflows/install.yml/badge.svg)![example workflow](https://github.com/nogibjj/aad64_Individual-Project1/actions/workflows/test.yml/badge.svg)

This assignment is designed to introduce us to pandas descriptive scripts. For the same, the main edit made was to add pandas==2.1.0 to my requirements.txt file.

Here, I have created a project which has functions dedicated to doing the following on a given dataset and returning the output: 
* Calculating the `mean` (rounded to two decimal places),
* Calculating the `median`,
* Calculating the `standard deviation` (rounded to two decimal places),

<p align = "center"><img width="471" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/34e5a3a6-f194-4abb-ba25-399472ebdf51"></p>

* Displaying the overall `summmary statistics` of a dataset. The picture below gives a snapshot of a portion of the entirety of the summary statistics for this dataset.
<p align = "center"><img width="663" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/30daee65-db61-4131-87f7-bc6ef39b668a"></p>

* `Visualizing` data in the form of a _violinplot_. It plots individuals Risk Preferences (y-axis) as per their Socioeconomic Status (x-axis), split by Gender (1: Male, 2: Female).

<p align = "center"><img src = "https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/88038ddc-c28d-4183-a4c9-5078abd7aa73" width = 500px></p>

I have also created a test file to ensure that the mean, median, and standard deviation functions are correctly functioning (using asserts).

The contents of this project are: 
* `.devcontainer` (with a [devcontainer.json](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/.devcontainer/devcontainer.json) and a [Dockerfile](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/.devcontainer/Dockerfile)), 
* `Github Actions`, 
* `.gitignore file`, 
* [Makefile](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/Makefile), 
* [requirements.txt](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/requirements.txt), 
* [main.py](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/main.py), 
* [test_main.py](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/test_main.py), and 
* [RiskData_SumScores.csv](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/RiskData_SumScores.csv).

As visible below, my project is passing all formatting, linting, and tests:

### Linting
*With PyLint:

<p align = "center"><img width="614" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/7f64eef1-94fe-4d1b-8058-717746dea223"></p>

*With Ruff:

<p align = "center"><img width="525" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/a609f056-0954-4685-9acf-27960365e57c"></p>

### Formatting
<p align = "center"><img width="542" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/6ee317ac-2e46-443f-a5c7-650afeba56a6"></p>

### Testing
<p align = "center"><img width="1208" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/818db623-f42d-4fb6-964c-62fc00b6cdfa"></p>

