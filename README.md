# aad64_Individual-Project1
## Continuous Integration using GitHub Actions of Python Data Science Project

## Summary

This project is an example of using Continuous Integration (or CI) in Python script/project development using GitHub. This project acts as a stencil for future projects that as well since it provides a clear outline of the steps that a rpoject needs to follow to maintain consistency, robustness, and quality in the code. CI (here, the workflow) ensures that with git push, the code undergoes linting, formatting, installing dependencies, and testing of the entire project (both python script as well as Jupyter notebook).

## Contents: 

The contents of this project are: 
* Jupyter Notebook with:
    Cells that perform descriptive statistics using Polars or Panda.
	Tested by using nbval plugin for pytest
* [Python Script](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/main.py) performing the same descriptive statistics using Polars or Panda
* lib.py file that shares the common code between the script and notebook
* [Makefile](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/Makefile) with the following:
    Run all tests (must test notebook and script and lib)
	Formats code with Python black
    Lints code with Ruff
    Installs code via:  pip install -r requirements.txt 
* [test_script.py](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/test_script.py) to test script
* [test_lib.py](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/test_lib.py) to test library
* Pinned [requirements.txt](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/requirements.txt)
* [Github Actions](https://github.com/nogibjj/aad64_Individual-Project1/edit/main/.github/workflows) performs all four Makefile commands with badges for each one in the README.md

## Further Information about the Project:

For this project, I have created functions in my `lib.py` file dedicated to doing the following on a given dataset and returning the output: 
* Calculating the `mean` (rounded to two decimal places),
* Calculating the `median`,
* Calculating the `standard deviation` (rounded to two decimal places),
* Displaying the overall `summmary statistics` of a dataset.
<p align = "center"><img width="580" alt="Screenshot 2023-09-11 at 11 47 40 AM" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/b0795143-b33d-461f-8459-3859896b7978"></p>

* `Visualizing` data in the form of a _violinplot_. It plots individuals Risk Preferences (y-axis) as per their Socioeconomic Status (x-axis), split by Gender (1: Male, 2: Female).

<p align = "center"><img src = "https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/88038ddc-c28d-4183-a4c9-5078abd7aa73" width = 500px></p>

These descriptive statistics and visualization are then performed in my `main.py` file. 

My test files are then used to test the functionality of the defined functions (in the `test_lib.py` file) and the validity inputs for each function (tested in the `test_script.py`).


## Workflows:

Below are screenshots to show that my project is passing all formatting, linting, and tests. However, each workflow's validity can also be seen in the badges at the top of the README.md file.

### Linting
<p align = "center"><img width="417" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/d1ba1d1e-b29d-401c-a3fc-2d00b1569df3"></p>

### Formatting
<p align = "center"><img width="407" alt="Screenshot 2023-09-11 at 11 53 56 AM" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/00680819-8369-44f1-b55f-6e30ce41da3f"></p>

### Testing
<p align = "center"><img width="1277" alt="Screenshot 2023-09-11 at 11 53 40 AM" src="https://github.com/nogibjj/aad64_Individual-Project1/assets/143753050/6e4f0fce-c5b7-440b-9278-4ab91c1655bf"></p>

