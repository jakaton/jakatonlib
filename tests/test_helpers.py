#!/usr/bin/env python
# coding=utf-8

import unittest

from jakatonlib.pos import POSTagger

pt=POSTagger(root="http://127.0.0.1:5000")

text_es=u"""
Este es un texto.

Y este es otro escrito muy rápido.
"""
text_en=u"""
This is a text.

This is one writen very fast.
"""

res_text_es={u'POS': [[u'Este', u'pd000000'], [u'es', u'vsip000'], [u'un',
u'di0000'], [u'texto', u'nc0s000'], [u'.', u'fp'], [u'Y', u'cc'], [u'este',
u'dd0000'], [u'es', u'vsip000'], [u'otro', u'di0000'], [u'escrito', u'aq0000'],
[u'muy', u'rg'], [u'rápido', u'aq0000'], [u'.', u'fp']]}
res_text_es_2={u'POS': [[u'Este', u'pd000000'], [u'es', u'vsip000'], [u'un',
u'di0000'], [u'texto', u'nc0s000']]}
res_text_en={u'POS': [[u'This', u'DT'], [u'is', u'VBZ'], [u'a', u'DT'],
[u'text', u'NN'], [u'.', u'.'], [u'This', u'DT'], [u'is', u'VBZ'], [u'one', 
u'CD'], [u'writen', u'JJ'], [u'very', u'RB'], [u'fast', u'RB'], [u'.',
u'.']]}
res_text_en_2={u'POS': [[u'This', u'DT'], [u'is', u'VBZ'], [u'a', u'DT'],
[u'text', u'NN']]}


class Test(unittest.TestCase):
    """Unit tests for POSTagger"""

    def test_pos_es(self):
        """Evaluate pos tagger"""
        result = pt.pos(text_es)
        self.assertEqual(res_text_es, result)
   
    def test_pos_es_sntc(self):
        """Evaluate pos tagger"""
        result = pt.pos_sntc(u"Este es un texto")
        self.assertEqual(res_text_es_2, result)
  
    def test_pos_en(self):
        """Evaluate pos tagger in English"""
        result = pt.pos(text_en,lang="en")
        self.assertEqual(res_text_en, result)
   
    def test_pos_en_sntc(self):
        """Evaluate pos tagger in English"""
        result = pt.pos_sntc(u"This is a text",lang="en")
        self.assertEqual(res_text_en_2, result)
   

if __name__ == "__main__":
    unittest.main()
