#!/usr/bin/env python                                                          
# -*- coding: utf-8                                                            
# ----------------------------------------------------------------------       
# Library for accessing poswebservice
# ----------------------------------------------------------------------       
# Ivan Vladimir Meza-Ruiz/ ivanvladimir at turing.iimas.unam.mx                
# 2015/IIMAS/UNAM                                                              
# ----------------------------------------------------------------------
import requests

class POSTagger():
    """Class for POS tagging a text"""

    def __init__(self, root=u"http://127.0.0.1:5000"):
        self.root = root
        self.apipos = u"/api/v1.0/tag/{0}"
        self.apipossntc = u"/api/v1.0/tag/{0}/{1}"

    def tag(self,text,lang="es"):
        """Tags a text by calling API poswebservice and a POST request"""
        url=self.root+self.apipos.format(lang)
        res=requests.post(url=url,
                          data=text.encode('utf-8'))
        return res.json()
        
    def tag_sntc(self,sntc,lang="es"):
        """Tags a sentence by calling API poswebservice and a POST request"""
        url=self.root+self.apipossntc.format(lang,sntc)
        res=requests.get(url=url)
        return res.json()
        
