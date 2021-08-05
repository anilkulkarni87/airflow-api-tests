# airflow-api-tests
This is a collection of Pytest for the 2.0 Stable Rest Apis for Apache Airflow. I have another repo where you could setup airflow locally and play around with these. I am used to RestAssured, but trying out pytest here.

<h3 align="center">Apache Airflow 2.0 Stable Rest Api calls - Python</h3>

<p align="center"> I am used to RestAssured for api testing. Trying out python api testing with Airflow stable rest api
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Running the tests](#tests)
- [Github Workflow](#githubworkflow)
- [Airflow Apis](#airflow_api)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

## 🏁 Getting Started <a name = "getting_started"></a>

## 🎈 Usage <a name="usage"></a>

## 🔧 Running the tests <a name = "tests"></a>

## Github Workflow for running tests <a name="githubworkflow"></a>


## ⛏️Airflow APIs <a name = "airflow_api"></a>
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
