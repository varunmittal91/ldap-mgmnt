# 
# (C) 2013 Varun Mittal <varunmittal91@gmail.com>
# This program is distributed under the terms of the GNU General Public License v2
#
# This file is part of ldap-mgmnt.
# 
# ldap-mgmnt is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation version 3 of the License. 
#
# ldap-mgmnt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NeweraHPC. If not, see <http://www.gnu.org/licenses/>.
# 

from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^main/$', 'dashboard.authentication.views.main'),
    url(r'^login/$', 'dashboard.authentication.views.login_user'),
    #url(r'^$', include('ldap_mgmnt.dashboard.home')),
    #url(r'^dashboard/', include('ldap_mgmnt.dashboard.urls')),

    # Examples:
    # url(r'^$', 'ldap_mgmnt.views.home', name='home'),
    # url(r'^ldap_mgmnt/', include('ldap_mgmnt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
