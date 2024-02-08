
import yaml

# Read LeetCode submissions data from a YAML file
with open('leetcode_submissions.yml', 'r', encoding='utf-8') as file:
    submissions_data = yaml.safe_load(file)

# Extract relevant data for updating badges
solved_count = submissions_data['solved_count']
total_problems = submissions_data['total_problems']
easy_count = submissions_data['easy_count']
medium_count = submissions_data['medium_count']
hard_count = submissions_data['hard_count']

# Update badge URLs in README file
with open('README.md', 'r', encoding='utf-8') as file:
    readme_content = file.read()

readme_content = readme_content.replace(
    '<img src="https://img.shields.io/badge/Solved-43%2F3032%20=1.42%25-blue.svg?style=flat-square" />',
    f'<img src="https://img.shields.io/badge/Solved-{solved_count}%2F{total_problems}%20={solved_count*100/total_problems:.2f}%25-blue.svg?style=flat-square" />'
)

readme_content = readme_content.replace(
    '<img src="https://img.shields.io/badge/Easy-18/767-5CB85D.svg?style=flat-square" />',
    f'<img src="https://img.shields.io/badge/Easy-{easy_count}/767-5CB85D.svg?style=flat-square" />'
)

readme_content = readme_content.replace(
    '<img src="https://img.shields.io/badge/Medium-21/1594-F0AE4E.svg?style=flat-square" />',
    f'<img src="https://img.shields.io/badge/Medium-{medium_count}/1594-F0AE4E.svg?style=flat-square" />'
)

readme_content = readme_content.replace(
    '<img src="https://img.shields.io/badge/Hard-4/671-D95450.svg?style=flat-square" />',
    f'<img src="https://img.shields.io/badge/Hard-{hard_count}/671-D95450.svg?style=flat-square" />'
)

# Write the updated content back to the README file
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(readme_content)
