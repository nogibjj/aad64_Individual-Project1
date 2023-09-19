# aad64_Individual-Project1
Continuous Integration using GitHub Actions of Python Data Science Project

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
<p align = "center"><img width="417" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/d1ba1d1e-b29d-401c-a3fc-2d00b1569df3"></p>

### Formatting
<p align = "center"><img width="407" alt="Screenshot 2023-09-11 at 11 53 56 AM" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/00680819-8369-44f1-b55f-6e30ce41da3f"></p>

### Testing
<p align = "center"><img width="1277" alt="Screenshot 2023-09-11 at 11 53 40 AM" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/6e4f0fce-c5b7-440b-9278-4ab91c1655bf"></p>

