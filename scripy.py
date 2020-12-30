"""
Assumptions Made

1. Preprocessing done and converted the xlsx file to csv as it is easy or read and manipulate.
2. ...
"""

import pandas as pd
import numpy as np
import os, json

SOURCE_FILE = os.path.join(".", "hierarchy_case_20May2020.csv")
DESCINATION_FILE = os.path.join(".", "output.json")

CEO_BOSS = "none"

class Employee:
    def __init__(self, EMPLOYEE_ID, DESIGNATION, DEPARTMENT, NAME, MANAGER_EMPLOYEE_ID):
        self.EMPLOYEE_ID = EMPLOYEE_ID
        self.DESIGNATION = DESIGNATION
        self.DEPARTMENT = DEPARTMENT
        self.NAME = NAME
        self.MANAGER_EMPLOYEE_ID = MANAGER_EMPLOYEE_ID
        self.reportees = []

    def fillReportees(self, dataList : list) -> None:
        """Fill the reportees list recursively using BFS

        Args:
            dataList (list[Employee]): Data Set read from csv file
        """
        self.reportees = []
        for item in dataList:
            if self.EMPLOYEE_ID == item.MANAGER_EMPLOYEE_ID:
                self.reportees.append(item)
        for item in self.reportees:
            item.fillReportees(dataList)

    def generateTree(self) -> dict:
        """Generate tree from this node till leafs as a dict

        Returns:
            dict: tree from this node.
        """
        respTree = dict()
        respTree["EMPLOYEE_ID"] = self.EMPLOYEE_ID
        respTree["NAME"] = self.NAME
        respTree["DEPARTMENT"] = self.DEPARTMENT
        respTree["DESIGNATION"] = self.DESIGNATION
        respTree["reportees"] = self.reportees

        for index in range(len(respTree["reportees"])):
            respTree["reportees"][index] = respTree["reportees"][index].generateTree()

        return respTree


if __name__ == "__main__":

    # ======== read csv data ===========
    readFile = pd.read_csv(SOURCE_FILE)
    readFile["MANAGER_EMPLOYEE_ID"].fillna(CEO_BOSS, inplace=True)
    count = len(readFile)

    readData = list()

    # ======== List of objects ==========
    for i in range(count):
        readData.append(
            Employee(
                readFile["EMPLOYEE_ID"][i],
                readFile["DESIGNATION"][i],
                readFile["DEPARTMENT"][i],
                readFile["NAME"][i],
                readFile["MANAGER_EMPLOYEE_ID"][i],
            )
        )

    # ======== getting the root ===========
    bossObj = None

    for item in readData:
        if item.MANAGER_EMPLOYEE_ID == CEO_BOSS:
            bossObj = item
            break
    
    # ======== generating the tree =========
    if bossObj != None:
        bossObj.fillReportees(readData)
        empTree = bossObj.generateTree()

        # ===== dump data in json file =====
        fileObj = open(DESCINATION_FILE, "w")
        json.dump(empTree, fileObj, indent=4)
        fileObj.close()
    else:
        print("No CEO found")
