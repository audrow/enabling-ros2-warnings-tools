README
======

This project aims to automate repeated actions in adding warnings to ROS2 projects.

Planned Tools
-------------
* Google sheet tool to keep track of warnings and their status
  * States: Not started, Open Issue, Open PR, Added
  * Getters 
    * Get warnings a specific packages has or needs
    * Get a package's URL 
* Create issues for groups of warnings
* Higher-level automation tool that integrates several tools from this repository and [`ros2-workflow-tools`](https://github.com/audrow/ros2-workflow-tools)
  * Create PR from warnings added and updating the sheet and possibly running CI
  * Merging a PR and updating the warnings
  
  Implementation
  --------------
  These tools will heavily rely on [Github's command line interface](https://cli.github.com/) and will interface with Google sheets ([here](https://towardsdatascience.com/how-to-import-google-sheets-data-into-a-pandas-dataframe-using-googles-api-v4-2020-f50e84ea4530) is information on using Google Sheet's API)
