import csv
import os
import re
import json
import shutil
import subprocess
import nbformat
import sys
import urllib.request
import warnings
import itertools

import matplotlib.pyplot as plt
from notebook import notebookapp
import nbconvert
import nbgrader
from nbconvert.preprocessors import CellExecutionError, ExecutePreprocessor
import numpy as np
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
from canvasapi import Canvas
from collections import defaultdict, Counter
from IPython.display import Javascript, Markdown, display, clear_output
from ipywidgets import (Button, Layout, fixed, interact, interact_manual,
                        interactive, widgets)
from nbgrader.apps import NbGraderAPI
from tqdm.notebook import tqdm  # Progress bar
from traitlets.config import Config
warnings.filterwarnings('ignore')

canvas_id = 10499
key = ""
canvas_obj = Canvas("https://canvas.uva.nl", key)
canvas_course = canvas_obj.get_course(int(canvas_id))

def get_student_ids():
    return {
        student.id: student.sis_user_id
        for student in canvas_course.get_users()
    }

def get_assignment_obj(assignment_name):
    return {
        assignment.name: assignment
        for assignment in canvas_course.get_assignments()
    }[assignment_name]

def download_files(assignment_file,file_with_students):
        """Downloads all the files from Canvas for an assignment
        If none were found on Canvas, uses zip collect in the download folder"""
        list_of_students_in_section = pd.read_excel(file_with_students)['UvAnetID'].to_list()
        if canvas_course is not None:
            if canvas_name in [
                    assignment.name
                    for assignment in canvas_course.get_assignments()
            ]:
                # Get sis id's from students
                student_dict = get_student_ids()

                # Get the Canvas assignment id
                assignment = get_assignment_obj(canvas_name)
                groups = []

                for submission in tqdm(
                    assignment.get_submissions(
                        include=['group'])):
                    if submission.group['id'] is not None:
                        if submission.group['id'] in groups:
                            continue
                        else:
                            groups.append(submission.group['id'])
                            
                    # Check if submission has attachments
                    if 'attachments' not in submission.attributes:
                        continue
                        
                    # Download file and give correct name
                    student_id = student_dict[submission.user_id]
                    if student_id
                    attachment = submission.attributes["attachments"][0]

                    directory = "submitted/%s/%s/" % (student_id,
                                                      assignment_folder)
                    if not os.path.exists(directory):
                        os.makedirs(directory)

                    filename = assignment_file + ".ipynb"
                    urllib.request.urlretrieve(attachment['url'],
                                               directory + filename)
                    
                    # Clear all notebooks of output to save memory
                    subprocess.run(["nbstripout", directory + filename])
        else:
            print("No assignment found on Canvas")
            
download_files("AssignmentWeek1","students_D.xlsx")
