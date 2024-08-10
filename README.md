# Project - Data Extraction I

<summary><h2>Context</h3></summary>

Context:
The group works in the data engineering team at HealthGen, a company specializing in genomics and personalized medicine research. Genomics is the study of an organism's complete set of genes and plays a fundamental role in personalized medicine and biomedical research. It allows DNA analysis to identify genetic variants and mutations associated with diseases and facilitates the personalization of treatments based on the individual genetic characteristics of patients.

The company needs to stay up to date on the latest advances in genomics, identify opportunities for research and development of personalized treatments, and monitor trends in genomics that may influence research and development strategies. With this in mind, the data team presented a proposal to develop a system that collects, analyzes and presents the latest news related to genomics and personalized medicine, and also studies the advancement of the field in recent years.


<summary><h2>Creating Environment Variables - ENV</h3></summary>

Using .env files in Python is a common practice to store sensitive information or settings that should not be hard-coded into your source code. In this project we are using the python-dotenv library to load environment variables from a .env file.

```bash
API_KEY= SUA_CHAVE_DE_API_AQUI

```

<summary><h2>Execution with Virtual Environment</h2></summary>

<details>
<summary><h3>Linux</h3></summary>

## Install virtualenv

To install `virtualenv`, open the terminal and run the following command:

```bash
pip install virtualenv
```

## Creating and Activating a Virtual Environment

Open the terminal and navigate to the root directory of the project, there create the environment with the following command:

```bash
virtualenv venv
```

Now activate your virtual environment:

```bash
source venv/bin/activate
```

## Installing the necessary tools:

Now you can, still in the root folder, install the necessary tools to run the application using the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Deactivating the virtual environment:

To deactivate your virtual environment, simply run the following command:

```bash
deactivate
```

</details>

<details>
<summary><h3>Windows</h3></summary>

## Install virtualenv

To install `virtualenv`, open the Command Prompt or PowerShell as administrator and run the following command:

```bash
pip install virtualenv
```

## Creating and Activating a Virtual Environment

Open the Command Prompt or PowerShell and navigate to the root directory of the project, there create the environment with the following command:

```bash
virtualenv venv
```

Now activate your virtual environment:

```bash
venv/bin/activate
```

## Installing the necessary tools:

Now you can, still in the root folder, install the necessary tools to run the application using the file requirements.txt:

```bash
pip install -r requirements.txt
```

## Deactivating the virtual environment:

To deactivate your virtual environment, simply run the following command:
```bash
deactivate


