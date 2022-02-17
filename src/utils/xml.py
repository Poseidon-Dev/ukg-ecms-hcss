from typing import Dict, OrderedDict
from requests.api import head, post
from src.utils.test import resp
from io import StringIO

import xml.etree.ElementTree as ET


__all__ = ['ReadXML', ]

class ReadXML:

    def __init__(self, resp=resp):
        self._resp = resp

        # if self._has_errors():
        #     raise ValueError('Response contained errors')
        
        # self.xml = self.cleaned_dict()

        # if 'PageTotal' in self.xml and int(self.xml['PageTotal']) > 1:
        #     print(True)


    @property
    def resp(self):
        responseXML = ET.iterparse(StringIO(self._resp))
        return responseXML
    

    def resp_to_dict(self):
        header_dict = OrderedDict()
        results_dict = dict()
        signal_num = 0
        count = 0
        tracker =  0

        ki = dict()
        ik = dict()

        for idx, (_,el) in enumerate(self.resp):
            print(idx, ': ', el.tag)


        # for idx, (_,el) in enumerate(self.resp):
        #     pre, namespace, post = el.tag.partition('}')
        #     ki[post] = idx
        #     ik[idx] = (post, el.text)
        #     if post == 'OperationResult':
        #         signal_num = idx + 1
        #     if post == 'TotalItems':
        #         count = int(el.text)
        
        # for idx, (_,el) in enumerate(self.resp):
        #     pre, namespace, post = el.tag.partition('}')
        #     if ki[post] < signal_num:
        #         header_dict[post] = el.text
        #     else:
        #         print(post, ': ', el.text)
        #         if tracker not in results_dict:
        #             results_dict[tracker] = {post: el.text}
        #         else:
        #             if post not in results_dict[tracker]:
        #                 results_dict[tracker][post] = el.text
                    # else:
            # tracker += 1

                # if post in results_dict[tracker]:
                #     tracker += 1
              
                # for i in range(0, count):
                #     if i not in results_dict:
                #         results_dict[i] = {post: el.text}
                #     else:
                #         results_dict[i][post] = el.text
                    
                

    
        print(results_dict)
        return 1
        # for _, el in self.resp:
        #     prefix, has_namespace, postfix = el.tag.partition('}')
        #     if has_namespace:
        #         resp_dict[postfix] = el.text
        #         if postfix == 'TotalItems':
        #             count = el.text
        #             print(count)
        #         print(postfix)
        # # del resp_dict['Header']
        # del resp_dict['Body']
        # del resp_dict['Envelope']
        # resp_dict['Action'] = resp_dict['Action'].split('/')[-1]
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