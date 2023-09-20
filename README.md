# aad64_Individual-Project1
Continuous Integration using GitHub Actions of Python Data Science Project

## Further Information about the Project:

For this project, I have created functions in my `lib.py` file dedicated to doing the following on a given dataset and returning the output: 
* Calculating the `mean` (rounded to two decimal places),
* Calculating the `median`,
* Calculating the `standard deviation` (rounded to two decimal places),

<p align = "center"><img width="471" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/34e5a3a6-f194-4abb-ba25-399472ebdf51"></p>

* Displaying the overall `summmary statistics` of a dataset. The picture below gives a snapshot of a portion of the entirety of the summary statistics for this dataset.
<p align = "center"><img width="663" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/30daee65-db61-4131-87f7-bc6ef39b668a"></p>

* `Visualizing` data in the form of a _violinplot_. It plots individuals Risk Preferences (y-axis) as per their Socioeconomic Status (x-axis), split by Gender (1: Male, 2: Female).

<p align = "center"><img src = "https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/88038ddc-c28d-4183-a4c9-5078abd7aa73" width = 500px></p>

These descriptive statistics and visualization are then performed in my `main.py` file. 

My test files are then used to test the functionality of the defined functions (in the `test_lib.py` file) and the validity inputs for each function (tested in the `test_script.py`).


The contents of this project are: 
* `.devcontainer` (with a [devcontainer.json](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/.devcontainer/devcontainer.json) and a [Dockerfile](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/.devcontainer/Dockerfile)), 
* [Github Actions](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/.github/workflows/actions.yml), 
* `.gitignore file`, 
* [Makefile](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/Makefile), 
* [requirements.txt](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/requirements.txt), 
* [main.py](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/main.py), 
* [test_main.py](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/test_main.py), and 
* [iris.csv](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/iris.csv).

Below are screenshots to show that my project is passing all formatting, linting, and tests. However, each workflow's validity can also be seen in the badges at the top of the README.md file.

### Linting
*With PyLint:

<p align = "center"><img width="614" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/7f64eef1-94fe-4d1b-8058-717746dea223"></p>

*With Ruff:

<p align = "center"><img width="525" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/a609f056-0954-4685-9acf-27960365e57c"></p>

### Formatting
<p align = "center"><img width="542" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/6ee317ac-2e46-443f-a5c7-650afeba56a6"></p>

### Testing
<p align = "center"><img width="1199" alt="image" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/f6a1400e-9011-4ff8-a040-94a703d34f46"></p>

