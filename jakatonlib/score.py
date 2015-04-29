#!/usr/bin/env python                                                          
# -*- coding: utf-8                                                            
# ----------------------------------------------------------------------       
# Library for accessing poswebservice
# ----------------------------------------------------------------------       
# Ivan Vladimir Meza-Ruiz/ ivanvladimir at turing.iimas.unam.mx                
# 2015/IIMAS/UNAM                                                              
# ----------------------------------------------------------------------
import requests

class Scorer():
    """Class for scoring based on sentiment analysis"""

    def __init__(self, root=u"http://127.0.0.1:5000"):
        self.root = root

    def sentimiento(self,text):
        """Scores of sentiment based on sentimineto list"""
        url=self.root+"/api/v1.0/score/sentimiento"
        res=requests.post(url=url,
                          data=text.encode('utf-8'))
        return res.json()
        
    def whissell(self,text):
        """Scores of pleasentness, activation, imaginery based on Whissell list"""
        url=self.root+"/api/v1.0/score/whissell"
        res=requests.post(url=url,
                          data=text.encode('utf-8'))
        return res.json()
    
    def afinn(self,text):
        """Scores of affinity based on affinity list"""
        url=self.root+"/api/v1.0/score/afinn"
        res=requests.post(url=url,
                          data=text.encode('utf-8'))
        return res.json()
    
    def sentiwn(self,text):
        """Scores of positive and negative based on senti word net list"""
        url=self.root+"/api/v1.0/score/sentiwn"
        res=requests.post(url=url,
                          data=text.encode('utf-8'))
        return res.json()
   

