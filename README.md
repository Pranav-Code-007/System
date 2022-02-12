# System
Project

1] How to Setup Pycharm :- 

2] install pycharm community edition

3] create project with virtual environment

4] Now open the terminal of pycharm not your system's terminal

5] Install further libraries pip install flask pip install cx-Oracle

'''Assummed that you have installed oracle database'''

6] Install the sql developer

7] Open windows search button and search for oracle. You will see a folder click on that folder. You will be able to see "local net configuration" click on that.
- Click on  "local net service Name configurations" 
- add
- next 
- Service Name: XEPDB1 
- next 
- Connection type: TCP 
- next 
- Hostname: localhost 
- Yes perform the test 
- port number : 1521 
- Click on change login 
- put the username and password and remember them <==== 
- next 
- Service Name: XEPDB1 
- Would you configure another net service name: No 
- Finish
- Refer the following link for above :- '''https://www.youtube.com/watch?v=gaelhF2us28'''

8] the url to access the database should be like username/password@//localhost:1521/XEPDB1 <==== username and password you set as above

9] Go to that sql developer and run the following query in worksheet

  ```
 create table usr( firstname varchar2(200 CHAR), lastname varchar2(200 CHAR), mobnum varchar2(10 CHAR), email varchar2(200 CHAR) primary key , passwd varchar2(200 CHAR), timest varchar2(50 CHAR) );
  ```

10] Now you can run the project

11] For your reference refer the following links

https://www.youtube.com/watch?v=6OwZvANOZaE

https://www.youtube.com/watch?v=d_CyuCLC3Ls

https://www.youtube.com/watch?v=oT_bjYUO4RQ

https://www.youtube.com/watch?v=_157RYEhpR4

https://www.youtube.com/watch?v=eMYFffdjyek

https://www.youtube.com/watch?v=ga8q90XFqDk

https://www.youtube.com/watch?v=gaelhF2us28

https://www.youtube.com/watch?v=PgFY3CScqJc
