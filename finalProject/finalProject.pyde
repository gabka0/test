global highestScore, stageNum
highestScore = 0 #we are putting highest score outside of setup, because it should not be updating each time user restarts the game. 
stageNum = 0 #stageNum is used to control what page to show the user
def setup():
    global xShot, yShot, dxShot, visible, totalNum, wShot, hShot
    global xShotOpp, yShotOpp, dxShotOpp, visibleOpp, totalNumOpp, wShotOpp, hShotOpp
    global stageNum, gamePlayBackGrounds
    global imgMainBackground, imgLogo, imgGamePlayBackground, imgExplosion, imgRocket, explosionAmount, rocketAmount, imgOuch
    global chosenCharacter, currentOpponent
    global characters, opponents, instructions
    global score, health, speed, highestScore
    global characterX, characterY, opponentX, opponentY, characterWidth, characterHeight, opponentWidth, opponentHeight, opponentChanged
    global gameOn
    global speedOpp
    global purple_lightning, red_explosion, fist, red_lightning, shoots, chosenShoot
    global last_lightning_time, lightning_interval
    global opponentNumber, currentOpponent
    global imgMenu, imgExit, imgRestart, imgNewRecord, imgMenuW, imgMenuH, imgRestartW, imgRestartH, imgExitW, imgExitH, imgMenuX, imgMenuY, imgRestartX, imgRestartY, imgExitX, imgExitY
    global frameCount, imgOuch_display
    global explosionSuperShotCount, rocketSuperShotCount, superShotType
    
    size(1500, 1000)      # set the window size
    
    #images
    imgMainBackground = loadImage("background.png")  # Main page background
    imgLogo = loadImage("strawHat.png") #logo of game
    imgBackGround1 = loadImage('gameplay_background.png') # Game Play page background
    imgBackGround3 = loadImage("background2.png")
    imgBackGround2 = loadImage("background3.png")
    imgBackGround4 = loadImage("background4.png")
    imgBackGround5 = loadImage("background5.png")
    gamePlayBackGrounds = [imgBackGround1, imgBackGround2, imgBackGround3,imgBackGround4, imgBackGround5]
    imgGamePlayBackground = gamePlayBackGrounds[0] #background that will be displayed
    
    #images of characters that user can choose
    imgCharacter1 = loadImage("monkey_d__luffy.png") #1st Character
    imgCharacter2 = loadImage("Zoro.png") #2nd Character
    imgCharacter3 = loadImage("Sanji.png") #3rd Charcter
    characters =[]
    characters = [imgCharacter1, imgCharacter2, imgCharacter3] # putting them to list to use specific chosen character in future. 
    chosenCharacter = characters[0] # in the beginning default chosen character is first one, however then user will chose wanted character
    
    #image that will be displayed when my character will be hurt
    imgOuch = loadImage("ouch.png")
    frameCount = 0 # I need this variable to control duration how long Ouch image will be displayed
    imgOuch_display = False # in the beginning display variabe is false because it should be displayed only when character is hurt. 
    
    #images of opponents, when opponents score is 10, 20, 30, and 40 opponent will change to next one. 
    imgOpponent1 = loadImage("Aarlong.png")
    imgOpponent2 = loadImage("doflamingo.png")
    imgOpponent3 = loadImage("Kaidoh.png")
    imgOpponent4 = loadImage("Akainu.png")
    imgOpponent5 = loadImage("Blackbeard.png")
    opponents = [imgOpponent1, imgOpponent2, imgOpponent3, imgOpponent4, imgOpponent5]
    opponentNumber = 0 #variable to change the currentOpponent
    currentOpponent = opponents[opponentNumber] #first character is imgOpponent1, then each time score will be 10, 20, 30, or 40 current opponent will change
    
    

    score = 0 #score is score, each time you will hit your opponent your score will increase by one. In the beginning it is 0. 
    
    #characteristics of Character that will be used in the game
    health = 0
    speed = 0
    
    #characteristics of your Character
    characterWidth = 200
    characterHeight = 200
    characterX = 0
    characterY = 30 #in the upper part there is a text, so character should be moving lower than that.
    
    #characteristics of your Opponent
    opponentWidth = 200
    opponentHeight = 200
    opponentX = width - opponentWidth
    opponentY = height - opponentHeight - 130 #in the bottom part there is a information about supershots left, so character should be moving higher than it. It is the reason why I am substracting additional 130. 
    opponentChanged = False
    
    fist = loadImage("fist.png") #red lightning is 1st characters Luffy's shot
    red_lightning = loadImage("red_lightning.png") #red lightning is 2nd characters Zoro's shot
    red_explosion = loadImage("shot1.png") #red explosion is 3rd characters Sanji's shot
    shoots = [fist, red_lightning,red_explosion]
    chosenShoot = shoots[0] #default chosen Shoot will be fist, but then according to chosen character it will change
    purple_lightning = loadImage("shot2.png") #purple lightning is your opponents shot
    
    #adding a shots to opponent, and characteristics for its shot. 
    totalNumOpp = 50
    xShotOpp = []
    yShotOpp = []
    visibleOpp = []
    wShotOpp = []
    hShotOpp = []
    dxShotOpp = []
    purple_lightning_active = False
    last_lightning_time = 0
    lightning_interval = 3000
    for i in range(totalNumOpp): 
        xShotOpp.append(0)
        yShotOpp.append(0)
        wShotOpp.append(0)
        hShotOpp.append(0)
        dxShotOpp.append(20)
        visibleOpp.append(False)
        
    #characters shot is called red explosion, assigning characteristics for characters shot
    totalNum = 50 
    xShot = [ ]
    yShot = []
    visible = []
    wShot = []
    hShot = []
    dxShot = []
    for i in range(totalNum): 
        xShot.append(0)
        yShot.append(0)
        wShot.append(0)
        hShot.append(0)
        dxShot.append(20)
        visible.append(False)

    
    #images for super powers
    imgExplosion = loadImage("explosion.png")
    imgRocket = loadImage("rocket.png")
    
    # Global variables for super shots
    explosionSuperShotCount = 3 #each game user has 3 explosion Super Shots
    rocketSuperShotCount = 3 #each game user has 3 rocket Super Shots
    superShotType = None  # can be 'explosion' or 'rocket', it will be assigned later according to the key pressed by User
    
    #instructions list
    instructions = ["1. Press 'W' or 'UP' key to move up", "2. Press 'S' or 'DOWN' key to move down", "3. Press Spacebar or Left Mouse Click to shoot", "4. Press A to use Strong Punch. It has bigger damaging radius, but you can use it only 3 times.", "5. Press D to use Fast Punch. It has faster speed, but you can use it only 3 times.", "6. Each time your shot lands on your enemy, your score increases by one.", "7. Each time your enemies land a shot on you, your health decreases by one.", "8. Each time you defeat an antagonist, a new antagonist appears.", "9. When your health will be equal to 0, game ends", "10. Your aim is to get highest score."]
    
    #images for the Game Over page
    imgMenu = loadImage('blue_button.png') #button to restart the game
    imgExit = loadImage('green_button.png') #button to exit the game
    imgNewRecord = loadImage('new_record.png') #image that will be displayed  only if your score is highest.
    imgMenuW = 200
    imgMenuH = 200
    imgMenuX = width/2-250
    imgMenuY = height/2-200
    imgExitW = 200
    imgExitH = 200
    imgExitX = width/2+50
    imgExitY = height/2-200


    
    speedOpp = 10 #Opponent Speed
    gameOn = False #checking if game has started or no
 


def draw():
    # stageNumbers, we have 4 stages:
    # 0: Main page
    # 1: Instruction page
    # 2: Game Play page
    # 3: Game Over page
    if stageNum == 0:
        drawMain()
    elif stageNum == 1:
        drawInstruction()
    elif stageNum == 2:
        drawGamePlay()
    elif stageNum == 3:
        drawGameOver()
    
    

def drawMain():
    global font
    #drawing background
    image(imgMainBackground, 0, 0)
    
    #writing name of the game
    fill(255,255,0)
    font   = createFont("Arial Bold", 100)
    textFont(font)
    text("PIRATE KING", 350, 100)
    #drawing game logo
    image(imgLogo, 950, 0, 250, 120)
  
    #writing text
    fill(255,255,255)
    font  = createFont("Arial Bold", 60)
    textFont(font)
    text("CHOOSE YOUR CHARACTER", 300, 250)
    
    #drawing all 3 characters
    characterWidth = 350
    characterHeight = 350
    for i in range(3):
        image(characters[i], 100 + i*(characterWidth+150), 500, characterWidth, characterHeight)
    
    #wiring how to choose each Character
    fill(255,255,255)
    font  = createFont("Arial Bold", 40)
    textFont(font)
    text("To choose Luffy", 100, 380)
    text("Press Q", 100, 450)
    
    text("To choose Zoro", 100 + (characterWidth+150), 380)
    text("Press W", 600, 450)
    
    text("To choose Sanji", 100 + (characterWidth+150)*2, 380)
    text("Press E", 1100, 450)

    #writing Health and Speed stats for each character
    fill(255,255,0)
    font   = createFont("Arial Bold", 30)
    textFont(font)
    #Writing Character1 stats
    text("Health:5", 220, 880)
    text("Speed:3", 220, 930)
    
    #Writing Character2 stats
    text("Health:4", 700, 880)
    text("Speed:4", 700, 930)

    #Writing Character3 stats
    text("Health:3", 1200, 880)
    text("Speed:5", 1200, 930)


    
    
def drawInstruction():
    #drawing background
    image(imgMainBackground, 0, 0)
    fill(255,255,0)
    font = createFont("Arial Bold", 100)
    textFont(font)
    #Writing title of page
    text("Instructions", 500, 100)
     
    #Writing instructions
    fill(255,255,0)
    font = createFont("Arial Bold", 30)
    textFont(font)   
    for i in range(10):
        text(instructions[i], 10, 200 + i*60)

    #writing how to move to next game play page    
    fill(255,255,255)
    font = createFont("Arial Bold", 46)
    textFont(font)
    text("PRESS ENTER OR LEFT MOUSE CLICK TO START THE GAME", 20, 900)
    

def drawGamePlay():
    global score, health, characterX, characterY, opponentY, speedOpp, currentOpponent, opponentChanged
    global purple_lightning_x, purple_lightning_y
    global purple_lightning_x, purple_lightning_active, last_lightning_time, opponent_y
    global stageNum, superShotType
    global xShot, yShot, visible, xShotOpp, yShotOpp, visibleOpp
    image(imgGamePlayBackground, 0, 0, width, height) #drawing background
    


    image(chosenCharacter, characterX, characterY, characterWidth, characterHeight) #drawing character in the top left corner
    image(currentOpponent, opponentX, opponentY, characterWidth, characterHeight) #drawing opponent in the bottom right corner, so they can not hit each other in the beginning
    
    #writing information about score and health
    fill(0,0,0)
    font = createFont("Arial Bold", 40)
    textFont(font)
    text("Score:"+str(score), 650, 50)
    text("Health:" + str(health), 650, 100)
    
    #drawing and writing information about how many super shots left
    fill(255,0,0)
    font = createFont("Arial Bold", 70)
    textFont(font)
    image(imgExplosion, width/2-150, height-120, 100, 100)
    text(explosionSuperShotCount, width/2-40, height-50)
    image(imgRocket, width/2+50, height-120, 100, 100)
    text(rocketSuperShotCount, width/2+160, height-50)
    

    
    opponentMovement() #making opponent move, please check function to see how it works
    characterInjured() #writing logic how character can be injured, please check function to see how it works
    opponentInjured() #writing logic how opponent can be injured, please check function to see how it works
    current_time = millis() #calculating time from the start of the program
    if current_time - last_lightning_time > lightning_interval: #checking if time from the last lightning time exceeded the interval to make a shot again
        opponentShot() #writing logic how opponent can make a shot, please check function to see how it works
        last_lightning_time = current_time #monitoring last time when opponent's shot lightning was used
    for i in range(totalNumOpp):
        if visibleOpp[i] == True: # in opponent shot function we assigned visible[i] to True, so shot becomes visible
            if yShotOpp[i]+hShotOpp[i]>height: #here we are checking so shot will be always visible
                yShotOpp[i] = height - hShotOpp[i]
            image(purple_lightning, xShotOpp[i], yShotOpp[i], wShotOpp[i], hShotOpp[i]) #drawing shoot
            xShotOpp[i] -= dxShotOpp[i] #moving the shoot
                
            # if shoot goes out of window, we making it not visible
            if xShotOpp[i] < 0: 
                visibleOpp[i] = False
    
    
    #character shooting logic
    for i in range(totalNum):
        if visible[i] == True: # in character shot function we assigned visible[i] to True, so shot becomes visible
            if yShot[i]+hShot[i]>height: #here we are checking so shot will be always visible
                yShot[i] = height - hShot[i]
            #if specific super shot was used, we are in the end making superShotType as none so it will not keep using super shots
            if superShotType == 'explosion': 
                image(chosenShoot, xShot[i], yShot[i], wShot[i], hShot[i])  # Larger explosion
                xShot[i] += dxShot[i]
                superShotType = None
            elif superShotType == 'rocket':
                image(chosenShoot, xShot[i], yShot[i], wShot[i], hShot[i]) 
                xShot[i] += dxShot[i]  # Rocket shoot moves faster and it is bigger
                superShotType = None
            else:
                image(chosenShoot, xShot[i], yShot[i], wShot[i], hShot[i]) 
                xShot[i] += dxShot[i] # Regular shoot image and speed
                
            # if shoot goes out of window, we making it not visible
            if xShot[i] > width:
                visible[i] = False
    
    # each time when your score will be 10, 20, 30, and 40 opponent will change to more strong opponent.  
    if score > 9 and score % 10 == 0 and opponentChanged==False and score<41:
        changeOpponent() #changing the opponent, please check the function for details
        opponentChanged = True #setting opponentChanged Variable to True, so my changeOpponent will not keep working infinite time when score is 10, 20, 30, or 40
    
    # Reset the opponentChanged value if the score is no longer a multiple of 10, because opponents change only when score is 10, 20, 30, or 40
    if score % 10 != 0:
        opponentChanged = False
    #if character is dead we are moving to next game over page.
    if health == 0:
        gameOn = False
        stageNum +=1
   
   

def drawGameOver():
    global highestScore
    
    #basically is score is higher than previous highest score, this score will be saved as highest score
    if score>highestScore:
        highestScore = score
        image(imgNewRecord, 100, 100, 300, 200) #when user achieves new highest score, new Record images will be displayed
        image(imgNewRecord, width-400, 100, 300, 200)
        
    #writing game over    
    fill(255,0,0)
    font = createFont("Arial Bold", 70)
    textFont(font)
    text("GAME OVER", 550, height/2+130)
    
    #writing Highest score value
    font = createFont("Arial Bold", 40)
    textFont(font)
    text("Highest Score:"+str(highestScore), 590, 150)
    
    #drawing Restart and Exit buttons. 
    fill(255,255,255)
    image(imgMenu, imgMenuX, imgMenuY, imgMenuW, imgMenuH)
    text("Restart", width/2-220, height/2-90)
    image(imgExit, imgExitX, imgExitY, imgExitW, imgExitH)
    text("Exit", width/2+110, height/2-90)    
        
    
    

def opponentMovement():
    global opponentY, speedOpp
    opponentY-=speedOpp  #opponent initially moves up, as he is initially located in the bottom corner
    if opponentY<=30:
        speedOpp = -speedOpp   #when opponent reaches the top, just before the text starts, it changes direction   
    elif opponentY>=height - opponentHeight - 130:
        speedOpp = -speedOpp #when opponent reaches the bottom, just before the text starts, it changes direction  
        
def opponentShot():
    global dxShotOpp, wShotOpp, hShotOpp
    foundOpp = False  #checking if there are shots that we can use again
    for i in range(totalNumOpp):
        if foundOpp == False and visibleOpp[i] == False: #if there are no reusable shots andthey are not visible, we are adding new shot
            #setting positions of our shot
            xShotOpp[i] = opponentX + opponentWidth / 2
            yShotOpp[i] = opponentY + opponentHeight / 2
            #making it visible
            visibleOpp[i] = True
            #setting width, height, and speed of the shot
            wShotOpp[i] = 140
            hShotOpp[i] = 140
            dxShotOpp[i] = 20
            #now it is found, so loop will work only once
            foundOpp = True
            
def characterShot():
    global superShotType,dxShot, wShot, hShot
    found = False #checking if there are shots that we can use again
    for i in range(totalNum):
        if found == False and visible[i] == False: #if there are no reusable shots andthey are not visible, we are adding new shot
            #setting positions of our shot
            xShot[i] = characterX + characterWidth / 2
            yShot[i] = characterY + characterHeight / 2
            #making it visible
            visible[i] = True
            #setting width, height, and speed of the shot
            wShot[i] = 100
            hShot[i] = 100
            dxShot[i] = 20
            #if user is using exposion super shot, we are using following characteristics for the shot
            if superShotType == 'explosion':
                wShot[i] = wShot[i] * 4  
                hShot[i] = hShot[i] * 4
            #if user is rocket super shot, we are using following characteristics for the shot
            elif superShotType == 'rocket':
                dxShot[i] = dxShot[i] * 2
                wShot[i] = wShot[i] * 2 
                hShot[i] = hShot[i] * 2  
            #now it is found, so loop will work only once
            found = True
            
def opponentInjured():
    global score
    #so basically for each of the character shots we are checking if they hitted opponent, if yes, score is increased by one
    for i in range(totalNum):
        if (opponentX+opponentWidth==xShot[i]+wShot[i] or opponentX+opponentWidth/2==xShot[i]+wShot[i]/2) and opponentY<yShot[i]+0.5*hShot[i] and opponentY+opponentHeight>yShot[i]+0.2*hShot[i]:
         score +=1
         
def characterInjured():
    global health, gameOn, frameCount, imgOuch, imgOuch_display
    #so basically for each of the opponent shots we are checking if they hitted character, if yes, health is decreasedd by one
    for i in range(totalNumOpp):
        if (characterX+characterWidth==xShotOpp[i]+wShotOpp[i] or characterX+characterWidth/2==xShotOpp[i]+wShotOpp[i]/2) and characterY<yShotOpp[i]+0.5*hShotOpp[i] and characterY+characterHeight>yShotOpp[i]+0.2*hShotOpp[i]:
         health -=1
         frameCount = 120  # we are setting frame count as 12
         imgOuch_display = True #and making Ouch image visible as indication that character is injured
         
        #each time while frame count is more than 0, we are entering the loop and displaying image Ouch, so as default value of frameRate is 60 frames per second, image will be showed for 2 second, as in 2 second you will enter loop 120 times before frameRate becomes 0.
        if frameCount > 0: 
         image(imgOuch, characterX + characterWidth, characterY, 100, 100)
         frameCount -= 1

def changeOpponent():
    #when this function is called next opponent will be displayed
    global opponentNumber, currentOpponent, purple_lightning_speed, lightning_interval, highestScore, purple_lightning_width, purple_lightning_height
    global dxShotOpp, wShotOpp, hShotOpp, imgGamePlayBackground
    opponentNumber +=1
    if opponentNumber<=4: #as there are only 5 opponents, and opponentNumber starts from 0, it should go untill 4.
     currentOpponent = opponents[opponentNumber] #changing the image of the opponent
     lightning_interval -=500 #changning lightning interval, so now opponent becomes more difficult and shot more frequently
     imgGamePlayBackground = gamePlayBackGrounds[opponentNumber] #changing background for each opponent
    


def keyPressed():
    global chosenCharacter, stageNum, characterY, speed, health, gameOn
    global explosionSuperShotCount, superShotType, rocketSuperShotCount
    global chosenShoot
    if stageNum==0 and (key=='Q' or key=='q'): #at Main Page
        chosenCharacter = characters[0]
        chosenShoot = shoots[0]
        speed = 7 #assinging attributes of chosen character
        health = 5 #assinging attributes of chosen character
        stageNum=1 #move to Instruction if character is chosen
    elif stageNum==0 and (key=='W' or key=='w'): #at Main Page
        chosenCharacter = characters[1]
        chosenShoot = shoots[1]
        speed = 10 #assinging attributes of chosen character
        health = 4 #assinging attributes of chosen character
        stageNum=1 #move to Instruction if character is chosen
    elif stageNum==0 and (key=='E' or key=='e'): #at Main Page
        chosenCharacter = characters[2]
        chosenShoot = shoots[2]
        speed = 13 #assinging attributes of chosen character
        health = 3 #assinging attributes of chosen character
        stageNum=1 #move to Instruction if character is chosen
        
    if stageNum==1 and key == ENTER: #at Instruction Page
        stageNum = 2 #move to gamePlay page if enter is pressed and you are in instruction page
    
    #character Movement
    #if you are in second stage game automatically starts working
    if gameOn == False and stageNum==2:
        gameOn = True          
    # if you are in game play stage and pressing W or UP, and you are not in the top, character moves up                              
    if gameOn == True and stageNum==2 and (key=='W' or key=='w' or keyCode==UP) and characterY>=30:
        characterY -= speed
    # if you are in game play stage and pressing S or DOWN, and you are not in the bottom, character moves dowm    
    elif gameOn == True and stageNum==2 and (key=='S' or key=='s' or keyCode==DOWN) and characterY<=height-characterHeight - 130:
        characterY += speed
    # # if you are in game play stage and pressing space character Shots      
    if gameOn == True and stageNum==2 and key == ' ':
        characterShot() #check the function to understand how it works
    # if you are in game play stage and you have enough amount of specific super shot, you will use super shot, and amount of super shots left will decrease to 1. 
    elif gameOn == True and stageNum == 2:
            if (key == 'a' or key == 'A') and explosionSuperShotCount > 0:
                superShotType = 'explosion' #we are setting superShotType so in characterShot function it will assign specific attributes according to super shot type
                characterShot()
                explosionSuperShotCount -= 1
            elif (key == 'D' or key =='d') and rocketSuperShotCount > 0:
                superShotType = 'rocket' #we are setting superShotType so in characterShot function it will assign specific attributes according to super shot type
                characterShot()
                rocketSuperShotCount -= 1


    

def mousePressed():
    global stageNum
    if stageNum==1 and mouseButton == LEFT: #if you are in instruction page and pressing left mouse button you are moving to game play page
        stageNum=2            
    if gameOn == True and stageNum==2 and mouseButton == LEFT: #if you are in game play page and pressing left mouse button your character shots. 
        characterShot()
    if stageNum==3: #if you are in game over page and pressing menu/restart button, game restarts
        if imgMenuX<mouseX<imgMenuX + imgMenuW and imgMenuY<mouseY<imgMenuY+imgMenuH:
         setup()
         stageNum = 0
    if stageNum==3: #if you are in game over page and pressing exit button, you are exitting the game
        if imgExitX<mouseX<imgExitX + imgExitW and imgExitY<mouseY<imgExitY+imgExitH:
            exit()
    
