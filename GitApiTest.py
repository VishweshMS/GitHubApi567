# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:48:26 2023
The primary goal of this file is to demonstrate a simple unittest implementation
@author: Vishwesh
"""

# Importing the unittest module for writing test cases
import unittest
from GitApi import get_repo_info,my_brand
# Defining a TestRepoAPI class that inherits from unittest.TestCase 
class TestRepoAPI(unittest.TestCase):

    # Test case for when user does not exist
    def testUserNotFound(self):
        # Calling the GithubApi function with a non-existent user ID
        self.assertEqual(get_repo_info('ASD123'), "GitHub user not found.")

    # Test case for testing success message by calling my username
    def testRepoSuccess(self):
        # Calling the GithubApi function with an existing user ID
        self.assertEqual(get_repo_info('VishweshMS'), "Success")
        
       
    def testNoRepos(self):
        self.assertEqual(get_repo_info('Vishwesh119'), "No public repositories found.")
        
if __name__ == '__main__':
   my_brand("HW 04a")
   print('Running unit tests')
   unittest.main()
   my_brand("HW 04a")
