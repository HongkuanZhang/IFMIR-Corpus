# Intention and Factuality Annotated Medical Incident Report Corpus
This repository consists of the Japanese medical incident reports (MIRs) corpus and the script for accessing and generating the target annotation reports associated with our LREC 2020 paper for information extraction on MIRs.

## Introduction
Medical incident reports (MIRs) are documents that record what happened in a medical incident. A typical MIR consists of two sections: a structured categorical part and an unstructured text part. Most texts in MIRs describe what medication was intended to be given and what was actually given, since what happened in an incident is largely due to discrepancies between intended and actual medications. Recognizing the **intention of clinicians** and the **factuality of medication** is essential to understand the causes of medical incidents and avoid similar incidents in the future. Therefore, we developed an MIR corpus with annotation of **intention and factuality** as well as of **medication entities** and **entity relations**. In this paper, we present our annotation scheme with respect to the definition of medication entities that we take into account, the method to annotate the relations between entities, and the details of the intention and factuality annotation. We then report the statistics of our annotation of 349 Japanese incident reports.  

## How to use
Our target MIRs for annotation are from the incident case search page of [Japan Council for Qualtity Health Care](http://www.med-safe.jp/mpsearch/SearchReport.action) (JQ). The procedure for accessing and generating the target annotation reports are shown as follows:

### 1. Downloading MIRs from the case search page of JQ
The csv file of MIRs for a specified month can be downloaded with 5 steps:
* #### Searching medication-related MIRs of a specified month (e.g., April, 2018).

<p align="center">
<img src="https://github.com/zhkleciel/JQMIR/blob/master/pics/pic1.png" />
</p>

* #### Downloading the csv file of MIRs (***MedicalReportPub.csv***).
![pic2](https://github.com/zhkleciel/JQMIR/blob/master/pics/pic2.png)

### 2. Generating the .txt files of target MIRs for annotation

With the downloaded ***MedicalReportPub.csv*** file, we can generate the annotation target files (.txt files) into the output path with the script ***generate-txt.py*** and correspoding index file containing the indexes of wrong medication MIRs. The output paths for pilot annotation and final annotation are `/49_pilot_annotation` and `/300_final_annotation` respectively. Here we use the downloaded MIRs from April in 2018 as an example to show the generation of annotation target files:

```python
python3 generate-txt.py path/to/MedicalReportPub.csv /WMR_indexes/2018-Apr-indexes.txt /49_pilot_annotation
```  

When generating the 300 final annotation target files, we need to generate the data from May 2018 to January 2019 in order to keep the consistency with the corresponding .ann files.


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
