# Workflow

How to install and use?

`pip install workflow_uva`

Place Workflow.ipynb and workflow.json in the nbgrader folder.

In case you don't see the widget buttons, please enable the widgets in jupyter:
 `jupyter nbextension enable --py widgetsnbextension`

# Workflow.json (Config file)
A few things can or need to be added to `workflow.json`:
* sequence, a list of assignments in order
  * For example: `"sequence": [
        "AssignmentWeek1",
        "AssignmentWeek2",
        "AssignmentWeek3"]`
* groups, a dict of groups of assignments
  * It should be a dict with as key the name of a group. The value of this dict is again a dict, with keys "assignments" and "weight". The key "assignments" should have as value a list of assignments and "weight" should have the relative weight as a number (for the whole group).
  * For example: `"groups": {
        "Assignments": {
            "assignments": [
                "AssignmentWeek1",
                "AssignmentWeek2",
                "AssignmentWeek3",
            ],
            "weight": 20
        }}`
* resits, a dict of resits, and which assignments it replaces
  * It should be a dict with as key the name of the resit, and as value the list of assignments that are replaces by the resit
  * For example: `"resits": {
        "OverallResit": [
            "Exam1",
            "Exam2"
        ]
    }`
* requirements, a list of minimal grades students have to have for assignment groups to pass the course
  * It should be a list of dictionaries, with as keys "groups" and "min_grade". The value of groups can be a string or list and should refer to the name of a group. The value of min_grade should be a number.
  * For example: `"requirements": [
        {
            "groups": "Theoretical_Assignments",
            "min_grade": 4.5
        },
        {
            "groups": ["Practical_Assignments", "Theoretical_Assignments"],
            "min_grade": 5.5
        }
    ]`


# FAQ

## Where to get an Canvas API key?
[See the Canvas API Documentation](https://canvas.instructure.com/doc/api/file.oauth.html#manual-token-generation)

## Where to store the Canvas API key?
The Workflow notebook will ask for it. Otherwise, it can be changed in the `workflow.json` file.
