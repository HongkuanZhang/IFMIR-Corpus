# A Japanese Medical Incident Report Corpus with Intention and Factuality Annotation.
This repository consists of the Japanese medical incident reports (MIRs) corpus and the script for accessing and generating the target annotation reports associated with our LREC 2020 paper for extracting information from MIRs.

## Introduction
Medical incident reports (MIRs) are documents that record what happened in a medical incident. A typical MIR consists of two sections: a structured categorical part and an unstructured text part. Most texts in MIRs describe what medication was intended to be given and what was actually given, since what happened in an incident is largely due to discrepancies between intended and actual medications. Recognizing the intention of clinicians and the factuality of medication is essential to understand the causes of medical incidents and avoid similar incidents in the future. Therefore, we are developing an MIR corpus with annotation of intention and factuality as well as of medication entities and their relations. In this paper, we present our annotation scheme with respect to the definition of medication entities that we take into account, the method to annotate the relations between entities, and the details of the intention and factuality annotation. We then report the statistics of our annotation of 349 Japanese incident reports.  

## How to use
This corpus annotated on MIR of the Japan Council for Qualtity Health Care (JQ) on April, 2018. We used the broswer annotation tool BRAT for annotation. The raw texts can be obtained by accessing the incident case search website on [http://www.med-safe.jp/mpsearch/SearchReport.action](http://www.med-safe.jp/mpsearch/SearchReport.action).

### Download MIR from case search website of JQ
The csv file can be downloaded with follwing 5 steps:
* #### Searching medication-related MIR on April, 2018.
![pic1](https://github.com/zhkleciel/JQMIR/blob/master/pics/pic1.png)
* #### Download incident reports as the csv file (***MedicalReportPub.csv***)
![pic2](https://github.com/zhkleciel/JQMIR/blob/master/pics/pic2.png)

### Generate .txt file

Put the downloaded ***MedicalReportPub.csv*** file into the root directory.

The txt generation script will generate 49 .txt files into the `/sample` by:
```python
python3 generate-txt.py
```
### Annotated samples visualization in BRAT tool
In the `/sample` file, there will be 49 .txt files, corresponding 49 .ann files, and .conf file for annotation defination. Annotated texts can be visualized by opening this file in BRAT, and the result will be like follows:

![pic3](https://github.com/zhkleciel/JQMIR/blob/master/pics/mir-in-brat.png)

The original incident contents are written in Japanese, and the contents in the figure above are translated into English only for easy to understand. 

### Requirements and Installation
* A computer running macOS or Linux
* Pandas python package
* BRAT tool (v1.3 Crunchy Frog) for visualization: https://brat.nlplab.org/

## Contact person:
If you have some suggestions and questions about this repository, please feel free to contact with us via: hang-hongkuan@a.mbox.nagoya-u.ac.jp
