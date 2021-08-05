# airflow-api-tests
This is a collection of Pytest for the 2.0 Stable Rest Apis for Apache Airflow. I have another repo where you could setup airflow locally and play around with these. I am used to RestAssured, but trying out pytest here.

<h3 align="center">Apache Airflow 2.0 Stable Rest Api calls - Python</h3>

<p align="center"> I am used to RestAssured for api testing. Trying out python api testing with Airflow stable rest api
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Uses](#uses)  
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Running the tests](#tests)
- [Github Workflow](#githubworkflow)
- [Airflow Apis](#airflow_api)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>
This repository will contain api calls to stable Airflow Rest apis. Having worked in airflow, I felt the lack of it. Come Airflow 2.0, it resolved the issues for me.
It is also an attempt to understand api testing with python as I usually prefer Rest Assured (Java).  This is a WIP repo as I continue to build and add calls to all apis. 
I have another repo which can help people setup airflow locally and then play around with these api.

## Uses <a name="uses"></a>
Listing out some reasons why I created this for myself:
- Learn about airflow apis.
- Learn about Python api testing.
- Understand use cases of api and document for future needs.

## 🏁 Getting Started <a name = "getting_started"></a>
Sequence of steps to be followed to be able to use this successfully:
- Clone the [airflow-docker](https://github.com/anilkulkarni87/airflow-docker) repo.
- Follow the instructions there to start running airflow locally.
- Execute some DAGS that are part of my repo or create your own DAGS.
- Start playing with the apis.

## 🎈 Usage <a name="usage"></a>

## 🔧 Running the tests <a name = "tests"></a>
Here is an example of how you could run the tests. I will continue to evolve this
```
pytest test_dag.py
```

## Github Workflow for running tests <a name="githubworkflow"></a>
  I added this step for me to understand more about github workflows and how i can leverage it for this specific usecase. Essentially what I will have to do is within the workflow:
- Clone airflow-docker repo
- Start Airflow
- Run these tests
- Do something with the results

## ⛏️Airflow APIs <a name = "airflow_api"></a>
I know you could get your hands on the swagger doc for these. But I still wanted to list down here.
- [Get Config](tests/test_config.py)
    - This is usually forbidden from the administrator owing to security reasons.
- [Connection](tests/test_connection.py)
  - Get connections : To list all connections currently available
  - Post : To create a new connection Id
  - Patch : To patch means to update an existing connection Id
  - Delete : To delete a connection
  - Get Connection Id : Get details of a specific connection based on the id
- [DAG](tests/test_dag.py) 
  - Get Dag Source code : We can get the dag source code by passing a file token, We can get file_token by calling the get dag by dag id
  - Get DAGS : Able to get all DAGS
  - Get DAG Info : Get basic info about a DAG
  - Patch : This is to update the dag. You can refer the example I have.
  - Post - clear tasks instances of a DAG : #TODO
  - Get Dag details : Get Basic info about dags
  - Get Dag tasks : Get all tasks for the dag.
  - Get Task details : Get a representation of the task
  - Post UpdateTaskInstanceState : #TODO
  

## ✍️ Authors <a name = "authors"></a>

- [@anilkulkarni87](https://github.com/anilkulkarni87) 

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
