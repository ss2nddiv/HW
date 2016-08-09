#!/usr/bin/env/python
import re
ncr_pattern=re.compile(r'&#x?[0-9,a-f,A-F]+;')

def _ncr_rpl(match):
    num=match.group()[2:-1]
    if num[0]=='x':
        return chr(int(num[1:],base=16))
    else:
        return chr(int(num))

def _ncr_gen_10(chn_chr):
   o=ord(chn_chr)
   if o < 256:
       return chn_chr
   else:
       return '&#'+str(o)+';'

def _ncr_gen_16(chn_chr):
   o=ord(chn_chr)
   if o < 256:
       return chn_chr
   else:
       return '&#'+hex(o)[1:]+';'


def ncr_replace(string):
	return re.sub(ncr_pattern,_ncr_rpl,string)

def ncr_generate_10(string):
	return ''.join(map(_ncr_gen_10,list(string)))

def ncr_generate_16(string):
	return ''.join(map(_ncr_gen_16,list(string)))
	


