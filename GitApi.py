# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:34:54 2023

The primary goal of this file is to list of the names of the repositories that the user has, along with the number of commits that are in each of the listed repositories.
@author: Vishwesh
"""
import datetime
import requests
import json
def get_repo_info(username):
    try:
        # Call GitHub API to retrieve user's repositories
        response = requests.get(f"https://api.github.com/users/{username}/repos")
        # Check for successful response
        response.raise_for_status()

        # Parse response to get a list of user's repositories
        repos = response.json()
        # Check if user has any public repositories
        if len(repos) == 0:
            return "No public repositories found."

        # Loop through each repository and get commit count
        for repo in repos:
            # Get commits URL for the repository
            commits_url = repo['commits_url'].split("{")[0]
            # Call GitHub API to retrieve commit information for the repository
            response = requests.get(commits_url)
            # Check for successful response
            response.raise_for_status()
            # Parse response to get a list of commits for the repository
            commits = response.json()
            # Print repository name and commit count
            print(f"Repo: {repo['name']} \nNumber of commits: {len(commits)} commits")

        return "Success"

    except requests.exceptions.HTTPError as err:
        # Check if GitHub user not found
        if err.response.status_code == 404:
            return "GitHub user not found."
        else:
            # Return HTTP error message
            return f"HTTP error: {err}"
    except Exception as e:
        # Return general error message
        return f"Error: {e}"


def my_brand(assignment_name):
    print("=*=*=*= Vishwesh Malur Somashekar =*=*=*=")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*=")
    print("=*=*=*= " + assignment_name + " =*=*=*=")
    print("=*=*=*= " + str(datetime.datetime.now()) + " =*=*=*=")