import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. 
'''

ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

urlString = '''
	url(r'^persons/(?P<pk>[0-9]+)$', views.persons_detail),
    url(r'^persons/$', views.persons_list),

    url(r'^authgroup/(?P<pk>[0-9]+)$', views.authgroup_detail),
    url(r'^authgroup/$', views.authgroup_list),

    url(r'^authgrouppermissions/(?P<pk>[0-9]+)$', views.authgrouppermissions_detail),
    url(r'^authgrouppermissions/$', views.authgrouppermissions_list),

    url(r'^authpermission/(?P<pk>[0-9]+)$', views.authpermission_detail),
    url(r'^authpermission/$', views.authpermission_list),

    url(r'^authuser/(?P<pk>[0-9]+)$', views.authuser_detail),
    url(r'^authuser/$', views.authuser_list),

    url(r'^authusergroups/(?P<pk>[0-9]+)$', views.authusergroups_detail),
    url(r'^authusergroups/$', views.authusergroups_list),

    url(r'^authuseruserpermissions/(?P<pk>[0-9]+)$', views.authuseruserpermissions_detail),
    url(r'^authuseruserpermissions/$', views.authuseruserpermissions_list),

    (fsdfsdf) (eererere)
'''


tableName = re.findall(r'[^][a-z]*[$]', urlString)
inBracket = re.findall(r'[(][a-z]*[)]', urlString)
print(tableName)
print(inBracket)