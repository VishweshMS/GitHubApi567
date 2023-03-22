# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:48:26 2023
The primary goal of this file is to demonstrate a simple unittest implementation
@author: Vishwesh
"""

# Importing the unittest module for writing test cases
import unittest
from GitApi import get_repo_info,my_brand
from unittest.mock import patch
import GitApi
# Defining a TestRepoAPI class that inherits from unittest.TestCase 
class TestRepoAPI(unittest.TestCase):

    # Test case for when user does not exist
    def testUserNotFound(self):
        # Calling the GithubApi function with a non-existent user ID
        self.assertEqual(get_repo_info('ASD4567898765434567'), "GitHub user not found.")

    # Test case for testing success message by calling my username
    def testRepoSuccess(self):
        # Calling the GithubApi function with an existing user ID
        self.assertEqual(get_repo_info('VishweshMS'), "Success")
        
       
    def testNoRepos(self):
        self.assertEqual(get_repo_info('Vishwesh119'), "No public repositories found.")
        
    @patch("GitApi.get_repo_info")
    def testUserSuccess_mock(self, mock_get_repo):
        mock_get_repo.return_value = [200, {"Weather-Detection": "8"
                                            }]
        self.assertTrue(GitApi.get_repo_info("VishweshMS")[0])

    @patch("GitApi.get_repo_info")
    def testUserSuccess_mock_return_value(self, mock_get_repo):
        mock_get_repo.return_value = [200, {"Weather-Detection": "8"
                                            }]
        self.assertEqual(mock_get_repo()[1], GitApi.get_repo_info("VishweshMS")[1])

    @patch("GitApi.get_repo_info")
    def testNoRepos_mock(self, mock_get_repo):
        mock_get_repo.return_value = [200, {""}]
        self.assertTrue(GitApi.get_repo_info("Vishwesh119")[0])

    @patch("GitApi.get_repo_info")
    def testNoRepos_mock_return_value(self, mock_get_repo):
        mock_get_repo.return_value = [200, {""}]
        self.assertIs(mock_get_repo()[1], GitApi.get_repo_info("Vishwesh119")[1])

    
    @patch("GitApi.get_repo_info")
    def testUserNotExist_mock(self, mock_get_repo):
        mock_get_repo.return_value = False
        self.assertFalse(GitApi.get_repo_info('ASD4567898765434567'))

    @patch("GitApi.get_repo_info")
    def testUserNotExist_mock_return_value(self, mock_get_repo):
        mock_get_repo.return_value = False
        self.assertIs(mock_get_repo(), GitApi.get_repo_info('ASD4567898765434567'))

    
if __name__ == '__main__':
   my_brand("HW 04a")
   print('Running unit tests')
   unittest.main()
   my_brand("HW 04a")
