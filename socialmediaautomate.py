#package requires is selenium . pip install selenium
from selenium  import webdriver
import time#will help us in waiting until the webpage appears to perform action or fill in details .
#webdriver acts a interface between your command and the browser
from getpass import getpass#to not display your password in the console
#taking input from the user for the social media they want to login to 
socialmedia = input("Enter  the social media site  you want to login to?\n 1.FACEBOOK \t 2.INSTAGRAM\t 3.TWITTER\t 4.LINKEDIN\n").lower()

if(socialmedia =="facebook"):
    username =input("Type your FACEBOOK email/phone.\n")
    password =getpass('Type your FACEBOOK password\n')

    url ='https://www.facebook.com/'

    #download the chromedriver its an executable selenium uses to control chrome
    #a simple goole search will provide you where you can download chrome driver according to your chrome version

    driver  = webdriver.Chrome(r'C:\Users\pc\Downloads/chromedriver')
    driver.get(url)
    #so now our script is automated that it can visit the webpage
    #now we will find elements by id we need to fill in go to your browser and inspect element and find its id

    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('loginbutton').click()
#instagram automation
elif(socialmedia=="instagram"):

    username = input("Type your INSTAGRAM username.\n")
    password = getpass("Type your INSTAGRAM password.\n")

    url = "https://www.instagram.com/accounts/login/?source=auth_switcher"

    

    driver = webdriver.Chrome(r'C:\Users\pc\Downloads/chromedriver')#enter the path of chromedriver exceutable file as a raw string 
    driver.get(url)
    #this again does the same thing as it opens the instagram page for us
    time.sleep(5)#waits until the login page appers lets do 5 seconds .
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF').click()
    

#twitter automation
elif(socialmedia =="twitter"):

    username = input("Type your email or username or phone number.\n")
    password = getpass("Type your password.\n")

    url = "https://twitter.com/login?lang=en"

    driver = webdriver.Chrome(r'C:\Users\pc\Downloads/chromedriver')
    driver.get(url)

    driver.find_element_by_class_name('js-username-field').send_keys(username)
    driver.find_element_by_class_name('js-password-field').send_keys(password)
    driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').click()#because the class name is used by many

#linkedin login
elif(socialmedia =="linkedin"):
    username = input("Type in your LINKEDIN  email/phone.\n")
    password = getpass("Type in your LINKEDIN password.\n")

    url ="https://www.linkedin.com/uas/login?fromSignIn=true&trk=uno-reg-join-sign-in"

    driver = webdriver.Chrome(r'C:\Users\pc\Downloads/chromedriver')
    driver.get(url)
    
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_css_selector('button.btn__primary--large.from__button--floating').click()#use .find_element instead of .find_elements as it returns a list and its not clickable
    



    