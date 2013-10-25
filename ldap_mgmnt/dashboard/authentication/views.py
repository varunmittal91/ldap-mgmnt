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


from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
 
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password) 
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('login.html', context_instance=RequestContext(request))
 
@login_required(login_url='/login/')
def main(request):
    return HttpResponse("Hello, world. You're at the polls index.")
