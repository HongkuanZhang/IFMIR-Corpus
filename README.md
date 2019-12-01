# A Pilot Corpus for Medical Incident Reports
In this project, we develop a corpus for information extraction from medical incident reports (MIR). This repository provides the script to generate MIR corpus using the medication-related incident reports from Japan Council for Quality Health Care.

> Medical incident reports (MIR) are documents that record what happened in a medical incident. A typical MIR consists of two sections: structured categorical part and unstructured text part. Most texts in MIR describe what medication is intended to be given and what is actually given, since what happened in an incident is largely due to the discrepancies between intended and actual medications. Recognizing such intention of clinicians and factuality of medication is essential to extract important information from MIR. Therefore, we are developing an MIR corpus with intention and factuality annotation as well as the annotation of medication entities and their relations. 

>In this paper, we develop a Japanese medical incident report corpus as the first step of information extraction from medical incident reports. The corpus contains three types of annotations, i.e., medication entity, entity relation, and intention/factuality annotations. Among them, intention/factuality is considered to be characteristic of corpora on incident reports. 

#### Contact person:
* Hongkuan Zhang, zhang-hongkuan AT a.mbox.nagoya-u.ac.jp

## How to use
This corpus annotated on MIR of the Japan Council for Qualtity Health Care (JQ) on April, 2018. We used the broswer annotation tool BRAT for annotation. The raw texts are public available on website [http://www.med-safe.jp/mpsearch/SearchReport.action](http://www.med-safe.jp/mpsearch/SearchReport.action).

### Download MIR from Japan Council for Qualtity Health Care
The csv file can be accessed with follwing 5 steps:
#### Selecting items
![pic1](https://github.com/zhkleciel/JQMIR/blob/master/pics/pic1.png)
#### Download as csv file
![pic2](https://github.com/zhkleciel/JQMIR/blob/master/pics/pic2.png)
