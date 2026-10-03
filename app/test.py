import pandas as pd
import json


df = pd.read_csv('computing_courses.csv')

courses = []
already_exists = []

for course in list(df.to_dict(orient='records')):
  if course['course_code'] in [c['course_code'] for c in courses]:
    already_exists.append(course)
  else:
    courses.append({
      "course_id": int(course['course_id']),
      "course_code": course['course_code'],
      "course_title": course['course_title']
    })
# print(courses)