from django.shortcuts import render

# Create your views here.

# Note: Important think which you have must knowladge 
# a = {'dk':'gupta','pk':'sharma'}
# print(a['dk']) # it will through error if key not exist in dictionary
# print(a.get('dk')) # get method will never through any error either key exist or not 
# print(a.get('sk')) # return None value because we don't set default value if key don't exist in dictionary
# print(a.get('sk','verma')) # here  i set default value for if any key will not match/exist in dictionary

# e.g: (cmd execuited code)
# >>> a = {'dk':'gupta','pk':'sharma'}
# >>> print(a['dk'])
# gupta
# >>> print(a.get('dk'))
# gupta
# >>> print(a.get('sk','verma'))
# verma
# >>> print(a.get('sk'))
# None
# >>> print(a['sk'])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'sk'

# ================================================================================================================
def page_counter_view(request):
    count = int(request.COOKIES.get('count',0)) # getting cookies from the request avilable or not?
    count = count + 1 # algo
    response = render(request,'index.html',{'count':count})
    response.set_cookie('count',count) #adding cookies with response
    return response # sending response with cookies