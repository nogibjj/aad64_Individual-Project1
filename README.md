# aad64_Individual-Project1
## Continuous Integration using GitHub Actions of Python Data Science Project

## Summary

This project is an example of using Continuous Integration (or CI) in Python script/project development using GitHub. This project acts as a stencil for future projects that as well since it provides a clear outline of the steps that a rpoject needs to follow to maintain consistency, robustness, and quality in the code. CI (here, the workflow) ensures that with git push, the code undergoes linting, formatting, installing dependencies, and testing of the entire project (both python script as well as Jupyter notebook).


![example workflow](https://github.com/nogibjj/aad64_Individual-Project1/actions/workflows/format.yml/badge.svg)![example workflow](https://github.com/nogibjj/aad64_Individual-Project1/actions/workflows/lint.yml/badge.svg)![example workflow](https://github.com/nogibjj/aad64_Individual-Project1/actions/workflows/install.yml/badge.svg)![example workflow](https://github.com/nogibjj/aad64_Individual-Project1/actions/workflows/test.yml/badge.svg)

This assignment is designed to introduce us to pandas descriptive scripts. For the same, the main edit made was to add pandas==2.1.0 to my requirements.txt file.

Here, I have created a project which has functions dedicated to doing the following on a given dataset and returning the output: 
* Calculating the `mean` (rounded to two decimal places),
* Calculating the `median`,
* Calculating the `standard deviation` (rounded to two decimal places),
<p align = "center"><img width="471" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/34e5a3a6-f194-4abb-ba25-399472ebdf51"></p>

* Displaying the overall `summmary statistics` of a dataset.

<p align = "center"><img width="663" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/30daee65-db61-4131-87f7-bc6ef39b668a"></p>

* `Visualizing` data in the form of a _violinplot_. It plots individuals Risk Preferences (y-axis) as per their Socioeconomic Status (x-axis), split by Gender (1: Male, 2: Female).

<p align = "center"><img src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/13af54c2-9718-4fcd-81d0-24da6005809f"></p>

These descriptive statistics and visualization are then performed in my `main.py` file. 

My test files are then used to test the functionality of the defined functions (in the `test_lib.py` file) and the validity inputs for each function (tested in the `test_script.py`).

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

Below are screenshots to show that my project is passing all formatting, linting, and tests. However, each workflow's validity can also be seen in the badges at the top of the README.md file.

### Linting
* With Ruff:
<p align = "center"><img width="525" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/a609f056-0954-4685-9acf-27960365e57c"></p>

* With Pylint (to check score):
<p align = "center"><img width="614" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/7f64eef1-94fe-4d1b-8058-717746dea223"></p>

### Formatting
<p align = "center"><img width="542" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/6ee317ac-2e46-443f-a5c7-650afeba56a6"></p>

### Testing
<p align = "center"><img width="1199" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/f6a1400e-9011-4ff8-a040-94a703d34f46"></p>

