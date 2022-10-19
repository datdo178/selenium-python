# ALLURE REPORT FOR PYTEST

## 1. Define:
- Allure Framework is lightweight multi-language test report tool 

## 2. Install:
`pip install allure-pytest`

## 3. Usage:
### 3.1. Create allure report folder
`allure generate`<br>
This command generates a folder named allure_reports with some empty data report files inside. Simply, we can an empty allure_report folder manually

### 3.2. Provide allure report path when running pytest
`pytest --alluredir=<allure_report_folders_path>`

### 3.2. Open allure report
`allure serve <allure_report_folders_path>`

## 4. Feature:
- Add test title:<br>
`@allure.title()`<br><br>

- Mark a step for fixture or method:<br>
`@allure.step()`<br><br>

- Group test step inside test case:
```python
def test_case():
    with allure.step():
        print('Welcome')
```

- Attach file:<br>
`@allure.attach(body, name, attachment_type, extension)`<br>
`allure.attach.file(source, name, attachment_type, extension)`<br><br>

- Add test description:<br>
`@allure.description()`<br>
`@allure.description_html`<br><br>
Or add multiple-line comment directly to test case

- Add links:<br>
`@allure.link`<br>
`@allure.issue`<br>
`@allure.testcase`<br>
To create link template, add this option when running pytest:<br>
`--allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}`<br><br>

- Test Feature/Story:<br>
`@allure.feature`<br>
`@allure.story`<br>
To filter test by feature/story for running, add this option when running pytest:<br>
`--allure-features feature_1,feature2`<br>
`--allure-stories story_1,story_2`<br><br>

- Test severity:<br>
To filter test by severity for running, add this option when running pytest:<br>
`@allure.severity(allure.severity_level.XXX)`<br>
`--allure-severities normal,critical`<br><br>

## 5. Example:
- Test script: test_allure_report.py
- Allure Report:
![image](../test_allure_report.png)
