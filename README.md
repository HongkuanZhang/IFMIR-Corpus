# Intention and Factuality Annotated Medical Incident Report Corpus
This repository consists of the Japanese medical incident reports (MIRs) corpus and the script for accessing and generating the target annotation reports associated with our LREC 2020 paper for information extraction on MIRs.

## Introduction
Medical incident reports (MIRs) are documents that record what happened in a medical incident. A typical MIR consists of two sections: a structured categorical part and an unstructured text part. Most texts in MIRs describe what medication was intended to be given and what was actually given, since what happened in an incident is largely due to discrepancies between intended and actual medications. Recognizing the **intention of clinicians** and the **factuality of medication** is essential to understand the causes of medical incidents and avoid similar incidents in the future. Therefore, we developed an MIR corpus with annotation of **intention and factuality** as well as of **medication entities** and **entity relations**. In this paper, we present our annotation scheme with respect to the definition of medication entities that we take into account, the method to annotate the relations between entities, and the details of the intention and factuality annotation. We then report the statistics of our annotation of 349 Japanese incident reports.  

## How to use
Our target MIRs for annotation are from the incident case search page of [Japan Council for Qualtity Health Care](http://www.med-safe.jp/mpsearch/SearchReport.action) (JQ). The procedure for accessing and generating the target annotation reports are shown as follows:

### 1. Downloading MIRs from the case search page of JQ
The csv file of MIRs for a specified month can be downloaded with 5 steps:
* #### Searching medication-related MIRs of a specified month (e.g., April, 2018).
![pic1](https://github.com/zhkleciel/JQMIR/blob/master/pics/pic1.png)
* #### Downloading the csv file of MIRs (***MedicalReportPub.csv***).
![pic2](https://github.com/zhkleciel/JQMIR/blob/master/pics/pic2.png)

### 2. Generating the .txt files of target MIRs for annotation

Placing the downloaded ***MedicalReportPub.csv*** file into the root directory.

Generating the annotation target (.txt files) into the output path with the script ***generate-txt.py*** and correspoding index file by (using the April as an example):
```python
python3 generate-txt.py MedicalReportPub.csv /WMR_indexes/2018-Apr-indexes.txt /output/path
```

### 3. Visualizing the annotated data with BRAT tool
In this work, we used the BRAT, a broswer annotation tool, for our annotation. With the .txt files and their corresponding .ann files, the BRAT can provide a visual interface like below:

![pic3](https://github.com/zhkleciel/JQMIR/blob/master/pics/mir-in-brat.png)

Notice that the original incident contents are written in Japanese, and the contents in the figure above are translated into English only for easy to understand. 

For utilizing the annotated data conveniently, in this repository we also provide 49 pilot annotation MIRs in `/49_pilot_annotation` file and 300 final annotation MIRs in `/300_final_annotation` file respectively, and each file contains generated .txt files, corresponding .ann files, and .conf file for annotation defination. The annotated data can be viewed by placing two files under the `/Brat/brat-v1.3_Crunchy_Frog/data/` without downloading them from the website as we mentioned above.

## Requirements and Installation
* A computer running macOS or Linux
* Pandas python package
* BRAT tool (v1.3 Crunchy Frog) for visualization: https://brat.nlplab.org/

## Contact person:
If you have some suggestions and questions about this repository, please feel free to contact with us via: zhang-hongkuan@a.mbox.nagoya-u.ac.jp
