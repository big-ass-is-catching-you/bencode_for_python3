useage example:  
Python 3.11.2 (main, Aug 26 2024, 07:20:54) [GCC 12.2.0] on linux  
Type "help", "copyright", "credits" or "license" for more information.  
>>> from bencode import bencode,bdecode  
>>> td_str = bdecode('d3:bar4:spam3:fooi42ee')   
>>> print (td_str)  
{'bar': 'spam', 'foo': 42}  
>>> tb_str = bencode('abcd')  
>>> print (tb_str)  
4:abcd  
>>>
Tested on Debian 12(bookworm) with Python 3.11.2.
