# A Japanese Medical Incident Report Corpus with Intention and Factuality Annotation.
This project for 

In this project, we develop a corpus for information extraction from medical incident reports (MIR). This repository provides the script to generate MIR corpus using the medication-related incident reports from Japan Council for Quality Health Care.


> Developing

#### Contact person:
* Hongkuan Zhang, zhang-hongkuan AT a.mbox.nagoya-u.ac.jp

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
