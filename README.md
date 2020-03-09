# Wedding gift list
First training project.
A gift list web app that has the functionality for the weding party to alter posts.

#### Run instructions

##### Using jenkins 

Copy the scripts from the jenkins directory an make them into jenkins paramertised jobs. The test will be run on the same VM that jenkins is hosted on. The deploy will deploy to a VM with a specified id. The SSH keys will have to be configured first but if the Run_Installs paramter is true everything should be set up for you with a databse configured. To gain acess to functionality of the hier teir roles you will need to manualy change one of the users in the databse to Couple.

##### Runnig localy 

To run localy you will have to create the venv and pip install -r requirements.txt then point the ap to your databse using export DATABASE_URI. Run the create.py file and then you should be good run the main app.py script.

### User Stories
* As the groom/bride I want to be able to add items to the list so my guest can see what I want.
* As the groom/bride I don't want to be able to see what people have selected so that it is a surprise on the day.
* As a member of the wedding party I want to be able to see the people that have signed up so that I can be sure that the commitments are legitimate.
* As the best man/ maid of honer I want to be able to see who has selected which gifts so I can give advice to guest as necessary.
* As the groom/bride I want to be able to alter peoples roles so that they have the correct level of privilege.
* As a guest I want to be able to claim a gift so that I can be sure that no one else will by the same thing.
* As a guest I want to be able to delete my account if I can not make it for some reason.
* As a user I want to be able to reset my password if I have forgotten it.
* As a guest I would like to be able to share the cost of the gift between multiple guests if it is expensive.

### ERD 

<img width="600" src="https://user-images.githubusercontent.com/32487202/76198871-ba0ce100-61e6-11ea-91a4-2e67d29eb016.png">

### Risk assessment
| Description | Assessment | Likehood | Impact | Overall | Responsibility | Current Mitagation | Proposed Mitigation | Responce | Control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Virtual machine hosting the app goes down. | Low | Medium | LM | Azure | Code base stored on git so another VM can be spun up quickly. | None | None | Treat |
| Database compramised | Database will hold valuable data from the users so needs to be secure. | Low | High | LH | Me | Database only accessible from specified VM and is password protected. | None | None | Treat |
| Test don’t catch a bug that breaks the app | The pipeline will deploy the app if test are passed so it would break for the user | Medium | Medium | M | Me | Trying to write comprehensive tests for the app. | Implement a selenium environment for testing. | Role back the app to the last stable version. | Treat |
| People put wrongly formatted data into the database | Can cause confusion between users over who owns a gift | Low | Low | L | Me | Strong validation checks on the forms to stop data being passed to the database in the wrong form. | None | Can repopulate the database from a separate file. | Treat |
| Browser trafic stolen | Would give attacker access to manipulate the database accessible from the app. The attacker could only cause real damage if they got access to an admin account. | Low | Medium | LM | Me | None | None | Repopulate the databases from files. | Tolerate |  

### Trello boards

Project progress was kep track on trello.
[Proudct backlog][pblink]
[Sprint planning][splink]
[pblink]: https://trello.com/b/TMfWbhRd/project-1-product-backlog
[splink]: https://trello.com/b/7qgVF9nr/p1-sprint-planning

### CI pipeline

![CI pipeline](https://user-images.githubusercontent.com/32487202/76200408-7e274b00-61e9-11ea-86f2-f77474b9c9c5.png)



### Testing

----------- coverage: platform linux, python 3.6.9-final-0 -----------
| Name | Stmts | Miss | Cover |
|---|---|---|---|
| application/__init__.py | 14 | 0 | 100% |
| application/forms.py | 83 | 25 | 70% |
| application/models.py | 25 | 2 | 92% |
| application/routes.py | 135 | 103 | 24% |
| TOTAL | 257 | 130 | 49% |

========================= 7 passed, 1 warning in 6.94s =========================

### Evaluation 

Not all functonality currently implemented the guests can't claim gifts yet so that databse relation hasesn't been used yet. Also the test require more work the only functionality currently being tested are the pathing for a user that isn't loged in. This is why the test coverage is low. The CI pipleine is in good shape and if the app needs to be transfered to a different VM 2 paremters need to be changed. The database wasn't moved to a hosted service but could be by changing the parameters of the scripts. The asthectics of the page need improving but that could be done by a web designer.  