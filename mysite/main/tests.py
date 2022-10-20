#from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Create your tests here.
class PlayerFormTest(LiveServerTestCase):

    def testform(self):
        selenium = webdriver.Chrome()
        # Choose your url to visit
        selenium.get('http://localhost:8000/players')
        # find the elements you need to submit form
        print("Iam here")
        print(selenium)
        player_name = selenium.find_element(By.ID, "id_name")
        player_height = selenium.find_element(By.ID, 'id_height')
        player_team = selenium.find_element(By.ID, 'id_team')
        player_ppg = selenium.find_element(By.ID, 'id_ppg')

        submit = selenium.find_element(By.ID, 'submit_button')

        # populate the form with data
        player_name.send_keys('Lebron James')
        player_team.send_keys('Los Angeles Lakers')
        player_height.send_keys('6 feet 9 inches')
        player_ppg.send_keys('25.7')

        # submit form
        submit.send_keys(Keys.RETURN)

        # check result; page source looks at entire html document
        assert 'roro' in selenium.page_source


class TeamFormTest(LiveServerTestCase):

    def testform(self):
        selenium = webdriver.Chrome()
        # Choose your url to visit
        selenium.get('http://localhost:8000/teams')
        # find the elements you need to submit form
        Team_id = selenium.find_element(By.ID, "id_team_id")
        Team_name = selenium.find_element(By.ID, 'id_team_name')
        City = selenium.find_element(By.ID, 'id_city')
        Year_founded = selenium.find_element(By.ID, 'id_year_founded')

        submit = selenium.find_element(By.ID, 'submit_button')

        # populate the form with data
        Team_id.send_keys('12')
        Team_name.send_keys('Liverpool')
        City.send_keys('England')
        Year_founded.send_keys('25.7')

        # submit form
        submit.send_keys(Keys.RETURN)

        # check result; page source looks at entire html document
        assert 'Liverpool' in selenium.page_source
