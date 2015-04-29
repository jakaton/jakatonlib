#!/usr/bin/env python                                                          
# -*- coding: utf-8                                                            
# ----------------------------------------------------------------------       
# Library for accessing monkeylearn
# ----------------------------------------------------------------------       
# Ivan Vladimir Meza-Ruiz/ ivanvladimir at turing.iimas.unam.mx                
# 2015/IIMAS/UNAM                                                              
# ----------------------------------------------------------------------
import requests
import json

class MonkeyLearn():
    """Class for connecting with spanish modules in MonkeyLearn"""

    def __init__(self, api_token=None):
        if api_token:
            self.api_token=api_token
        else:
            self.api_token=raw_input("Type your api token: ")
        

    def language(self,text):
        """Language detection per line in text"""
        data={
            'text_list': text.split('\n')   
        }
        response = requests.post(
            "https://api.monkeylearn.com/v2/classifiers/cl_oJNMkt2V/classify/",
                data=json.dumps(data),
                headers={'Authorization': 'Token {0}'.format(self.api_token),
                        'Content-Type': 'application/json'})
        return json.loads(response.text)

        
    def keyword(self,text):
        """Keyword extractor per line in text"""
        data={
            'text_list': text.split('\n')   
        }
        response = requests.post(
             "https://api.monkeylearn.com/v2/extractors/ex_eV2dppYE/extract/",
                data=json.dumps(data),
                headers={'Authorization': 'Token {0}'.format(self.api_token),
                        'Content-Type': 'application/json'})
        return json.loads(response.text)

    def ner(self,text):
        """Name entity extractor per line in text"""
        data={
            'text_list': text.split('\n')   
        }
        response = requests.post(
            "https://api.monkeylearn.com/v2/extractors/ex_Kc8uzhSi/extract/",
                data=json.dumps(data),
                headers={'Authorization': 'Token {0}'.format(self.api_token),
                        'Content-Type': 'application/json'})
        return json.loads(response.text)

   
