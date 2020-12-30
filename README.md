# Tree Solution

> Please install the packages in `requirement.txt` file to execute the code.

> File to execute : `scripy.py`

Assumptions Made : Preprocessing done and converted the xlsx file to csv.

Reading and manipulating csv file is much simpler and fast compared to that of xlsx file. So i conveted the file into csv and then started working on it.

- Data cleaning : As the CEO reports to None and is represented my `numpy.nan`, i replaced it with None specifically so to make it easy to work on.

- Approach followed: I first looked for the CEO in our parsed dataset so that it could server as root node. then simply recursively called the tree generation function in BFS order to fill the reportees list and the entire graph generated itself.

- Output file: the whole output is dumped into `output.json` file.

