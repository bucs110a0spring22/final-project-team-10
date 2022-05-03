:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Snake Game
## CS 110 Final Project
### Spring, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

[repl](https://replit.com/join/ikvdjlwjwx-miayan)

<< [link to demo presentation slides](#) >>

### Team: Team 10
#### Mia Yan, Nagima Dubanaeva, George Tzakas

***

## Project Description *(Software Lead)*

<< Give an overview of your project >>

***    

## User Interface Design *(Front End Specialist)*

* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
    ![63F7276B-01B0-4E99-9759-AB26FCEBBA3A](https://user-images.githubusercontent.com/98920760/162537262-eab3614e-5c6e-420f-84cb-e9670aa5183a.JPEG)
- The opening screen(start screen) shows the name of the game and lets the user start the game
![Team10_GUI-0](https://user-images.githubusercontent.com/98920760/162537340-fdc11bce-72fa-46a0-922d-b88f729a1859.png)
- In the game screen the user moves the snake around in order to collect food (apples)
![5A411926-A80F-47C0-A91C-5A952FBFE32F](https://user-images.githubusercontent.com/98920760/162537424-2f64d017-6a28-40a9-ad28-f450da60c024.JPEG)
- The last screen is the game over screen. When the user is done laying is shows how many apples were collected and their over all score. 

* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design *(Backend Specialist)*

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. >>
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
        * ![class diagram](assets/class_interface.png)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * << You should have a list of each of your classes with a description. >>

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:

* main.py
* src
    * <all of your python files should go here>
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*

   * You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Mia Yan

<< Worked as integration specialist by... >>

### Front End Specialist - Nagima Dubanaeva

<< Front-end lead conducted significant research on... >>

### Back End Specialist - George Tzakas

<< The back end specialist... >>

## Testing *(Software Lead)*

* << Describe your testing strategy for your project. >>
    * << Example >>

## ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | opening run page  |  the page opnes up to the gae window with words "Snake Game"   |          |
|  2  | start button  | the user presses "play/start" button the game starts with the snake appering on the page and the main game window with a timer  |                 |
|  3  |  the apples appear | the user has to move the snake around to eat the apples |                 |
|  4  | press up key  | the snake moves up along the tiles |                 |
|  5  | press down key  | the snake moves down along the tiles |                 |
|  6  | press right key  | the snake moves to the right on the tiles|                 |
|  7  | press left key  | the snake moves to the left on the tiles |                 |
|  8  | the timer runs out   | once the timer runs out the game ends |                 |
|  9  | game over page  |  the words "game over" with the number of apples eaten and the score appears
 |                 |
etc...
