## Instruction to run the program 

# Description
The intend of this project is to meet all the requirements presented in the Data Engineering Task that was presented to Dražen Matijević.

Presented Requirements:
1. Create ER diagram
2. Develop Data Pipeline
3. Create DQ checks for source data
4. Use Apache Spark - not mandatory

# Deliverables

To meet all the requirements different elements are created:
1. ER diagram picture.png
2. DataPipeline.py + .env + Unit test elements (UnitTestPipeline.py, TestUnitTestPipeline.py) + Dockerfile
3. DQ.py
4. CopyData.ipynb which could be script inside Spark cluster (DataBricks or Synapse) and as such a part of bigger data pipeline defined in ADF or Synapse for example


# Outcome
After running the DataPipeline.py a connection to SQL Server db defined in .env will be made and all the tables inside dbo schema will be copied to landing zone on local computer. If landing zone is not existing one will be made with the filepath c:\demo\landing_zone.
DQ.py will produce a report for each table with some standard DQ checks in data engineering
TestUnitTestPipeline.py will make unit test for some functions used in the data pipeline.