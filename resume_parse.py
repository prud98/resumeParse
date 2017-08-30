import tika
from tika import parser
import re
class ResumeParsing:
    def parseEmail():
        tika.initVM()
        parsed = parser.from_file("MyResume.docx")
        regular_expression = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}", re.IGNORECASE)
        result = re.search(regular_expression,parsed["content"])
        print("Email id:"+result.group())
    def parsePhone():
        tika.initVM()
        parsed = parser.from_file("MyResume.docx")
        regular_expression = re.compile(r"[[+91]*[' ']*[0-9]{10}]*",re.IGNORECASE)
        result = re.search(regular_expression,parsed["content"])
        print("phone No:"+result.group())
    def parseAddress():
        tika.initVM()
        parsed = parser.from_file("MyResume.docx")
        regular_expression = re.compile(r"[a-z\s]+,[a-z\s]+\.", re.IGNORECASE)
        result = re.search(regular_expression,parsed["content"])
        print("Address:"+result.group())
    def parseName():
        tika.initVM()
        parsed = parser.from_file("MyResume.docx")
        regular_expression = re.compile(r"[a-z]+[\s]+[a-z\s]+", re.IGNORECASE)
        result = re.search(regular_expression,parsed["content"])
        print("Name:"+result.group())
ResumeParsing.parseEmail()
ResumeParsing.parsePhone()
ResumeParsing.parseName()
ResumeParsing.parseAddress()
