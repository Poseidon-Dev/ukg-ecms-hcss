from src.utils.test import resp
from io import StringIO

import xml.etree.ElementTree as ET


__all__ = ['ReadXML', ]

class ReadXML:

    def __init__(self, resp=resp):
        self._resp = resp

        if self._has_errors():
            raise ValueError('Response contained errors')
        
        self.xml = self.cleaned_dict()


    @property
    def resp(self):
        responseXML = ET.iterparse(StringIO(self._resp))
        return responseXML
    

    def resp_to_dict(self):
        resp_dict = {}
        for _, el in self.resp:
            prefix, has_namespace, postfix = el.tag.partition('}')
            if has_namespace:
                resp_dict[postfix] = el.text
        del resp_dict['Header']
        del resp_dict['Body']
        del resp_dict['Envelope']
        resp_dict['Action'] = resp_dict['Action'].split('/')[-1]
        return resp_dict


    def cleaned_dict(self):
        pre_dict = self.resp_to_dict()
        idx = 0
        result = {}
        post_dict = {}
        for k,v in pre_dict.items():
            if v:
                v = v.strip().replace('\n', '')
            else:
                v = ''
            if k == 'OperationResult':
                idx += 1
            if idx > 0:
                result[k] = v
            else:
                post_dict[k] = v

        post_dict['results'] = result
        return post_dict


    def get_class(self):
        print(self.resp)
        resp_class = self.resp[re.search('Results', self.resp).span(0)[1]:].split()
        # resp_class = resp_class[0].replace('<', '')
        return resp_class

    
    def get_method(self):
        return self.xml['Action'].replace('Response', '')

    
    def _has_errors(self):
        if self.cleaned_dict()['HasErrors'] == 'true':
            return True


    def results(self):
        return self.xml['results']