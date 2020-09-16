# Running in windows
To Run the file in windows please follow the below steps:
- Download the oracle Instant Basic client for windows from the link [https://www.oracle.com/ie/database/technologies/instant-client/winx64-64-downloads.html] , please make sure to chose the correct architecture file 32/64 depending on the system configuration.
- In the main.py file please change the file location to the place where the unziped file for oracle instant classic is placed. Also please uncoment the line 29 to 32.
- create python virtual envoirnment and activate it with the below command in CMD (make sure u have python 3.6 or hiegher)
  - ``` python -m venv <NameOfEnvironment>```
  - ```<ProjectEnvFolder>\Scripts\activate```
- once the environment is running need to install all the libraries with the help of requirement.txt file and below command.
  - ``` pip install -r requirement.txt```
- **Please change the username and password to correct cred (given to candidate) on the main.py file on line 17 and 18 to connect the oracle instance (as this ia a public repository that is why it is removed from the code while uploading to git hub**.
- After doing the above steps run the main.py file with below command.
  - ``` python main.py```
- **While giving api request please pass "UserName":"Test" and "Password":"Password123" in the headers**

# Running in Linux
To run the file in Linux\Ubuntu please follow the below commands.
- Download the oracle Instant Basic client for Linux/Ubuntu from the link (.rpm file).
[https://www.oracle.com/ie/database/technologies/instant-client/linux-x86-64-downloads.html]
- to install the .rpm file please follow the below steps for respective systems.
  - ubuntu: if u don't have alien, please download it with below command and once installed use to run the .rpm file.
    - ```sudo apt-get install alien```
    - ```sudo alien -i oracle-instantclient19.8-basiclite-19.8.0.0.0-1.x86_64.rpm ```
  - linux or cent os: 
     - ``` sudo yum install oracle-instantclient19.8-basiclite-19.8.0.0.0-1.x86_64.rpm```
- For virtual environment if you don't have virtualenv install just run.
  - ```sudo apt-get install virtualenv```
- once installed run below command to create virtual environment and activate it.
  - ```virtualenv -p python3 <NameOfVirtual>```
  - ```source /<folder of virtual env>/bin/activate```
- once the environment is running need to install all the libraries with the help of requirement.txt file and below command.
  - ``` pip install -r requirement.txt```
- **Please change the username and password to correct cred (given to candidate) on the main.py file on line 17 and 18 to connect the oracle instance (as this ia a public repository that is why it is removed from the code while uploading to git hub**.
- After doing the above steps run the main.py file with below command.
  - ``` python main.py```
- **While giving api request please pass "UserName":"Test" and "Password":"Password123" in the headers**.

### If there are issues while running the app, please check the ip [http://34.252.45.14/employees] the application is hosted on AWS as well.






