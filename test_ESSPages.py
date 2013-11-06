# -*- coding: iso-8859-15 -*-
"""Simple FunkLoad test

$Id: test_Simple.py 53544 2009-03-09 16:28:58Z tlazar $
"""
from mechanize import ParseResponse, urlopen, urljoin
import unittest
from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase
from funkload.utils import xmlrpc_get_credential, xmlrpc_list_credentials


class Simple(FunkLoadTestCase):
    """This test use a configuration file Simple.conf."""

    def setUp(self):
        """Setting up test."""
        
        self.logd("setUp")
        
        self.server_url = self.conf_get('main', 'url')
        #credential_host = self.conf_get('credential', 'host')
        #credential_port = self.conf_getInt('credential', 'port')
        #self.credential_host = credential_host
        #self.credential_port = credential_port
        #self.cred_admin = xmlrpc_get_credential(credential_host,
        #                                        credential_port,
        #                                      'AdminZope')
        #self.cred_member = xmlrpc_get_credential(credential_host,
        #                                         credential_port,
        #                                         'FL_Member')
       
        """Setting up test."""
        self.logd("setUp")
        
        # test cred server
        #esslogin = self.get_cred()
        
        self.server_url = self.conf_get('main', 'url')
        print self.server_url
        
        self.setHeader("User-Agent","Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13")
        self.setHeader("Accept","text/html,application/xhtml+xml,application/x-www-form-urlencoded,application/xml;q=0.9,*/*;q=0.8")
        self.setHeader("Keep-Alive","115")
        #self.setHeader("Connection","keep-alive")
        #self.setHeader("Accept Encoding",'gzip,deflate')
        #self.setHeader("Cookie",'pageSize:alert/ListAlerts=100; JSESSIONID=3k4dxnkaut1am3z2lzgao6mp')
        #self.setHeader("Cookie",'pageSize:alert/ListAlerts=100')
        
#3k4dxnkaut1am3z2lzgao6mp
        
        
        
        print self.server_url
        response = self.post(self.server_url)
        #self.debugHeaders(True)
        #print response.server + response.url
        print str(response.code) + " - " + response.url
        
        #login here: 
        #response = self.post(self.server_url + "/ess/j_spring_security_check", params=[
                                                                                        #['formids','login-form,j_username,j_password,login-btn'],
                                                                                        #['submitmode',''],
                                                                                        #['submitname',''],
                                                                                        #['userNameInput', 'ess@echo360.com'],
                                                                                        #['passwordInput', 'password'],
         #                                                                               ['j_username', 'ess@echo360.com'],
         #                                                                               ['j_password', 'password']],
                                                                                        #['passwordInput', 'y0SPqzft6'],
                                                                                        #['submit', 'login-btn'],
                                                                                        #['action','j_spring_security_check']],
        #                                                                                description="ESS Login Page")
        #print response.code, response.url      
             
         
        print "Done Setup"
    #def get_cred(self):
        
     #print self.cred_admin
        #print self.cred_member
        #return self.cred_member
        
        
        
           
    def test_page_verify(self):   
        # The description should be set in the configuration file
        fail = 0
        server_url = self.server_url
        # begin of test ---------------------------------------------
        nb_time = self.conf_getInt('test_page_verify', 'nb_time')
        pages = self.conf_getList('test_page_verify', 'pages')

        urlfile = self.conf_get('test_page_verify','urlfilename')
        print server_url

        #open urlfile list for processing
        testurls = open(urlfile,"r")
        #esslogin = self.get_cred()
        #print esslogin
        for i in range(nb_time):
            self.logd('Try %i' % i)
            for urls in testurls:
            #for page in pages:
                #print "XXXXX PAGE:  " + urls
                
                testerpage = urls.split(',')
                #print testerpage[0]
                #print testerpage[1]
                #print server_url + testerpage[0]
                response = self.get(server_url + testerpage[0], description='Get %s' % testerpage[0])
                #print response.server
                responseurl = response.protocol+"://"+response.server+":"+response.port
                #print response.body
                if response.url == "/ess/login.jsp":
                    li = "ess@echo360.com"
                    pw = "password"
                    #print li,pw
                    #response = self.get(responseurl + "/ess/ContentLogin.html")
                    
                    response = self.post(responseurl + "/ess/j_spring_security_check", params=[
                                                                                        #['formids','login-form,j_username,j_password,login-btn'],
                                                                                        #['submitmode',''],
                                                                                        #['submitname',''],
                                                                                        ['userNameInput', 'ess@echo360.com'],
                                                                                        ['passwordInput', 'password'],
                                                                                        ['j_username', li.strip()],
                                                                                        ['j_password', pw.strip()]],
            																			#['passwordInput', 'y0SPqzft6'],
                                                                                        #['submit', 'login-btn'],
                                                                                        #['action','j_spring_security_check']],
                                                                                        description="Post for login against LDAP")
                    print response.code, response.url
                    #self.clearContext() 
                #print "IN PAGE VERIFY"
                #print response.body
                print str(response.code) + " - " + response.url
                testbody = response.body
                #print testbody
                try:
                    
                    self.assert_(str(testerpage[1]).strip() in testbody,"FAILED")
                    self.logi(server_url + ": PASSED")
                    #print "PASSED STRING COMP"
                except AssertionError:
                    self.logi(server_url + " : "+testerpage[1]+ " not found on page")
                    fail = fail + 1
                    #print "FAILED STRING COMP"
                    #print testbody;
                    self.fail(server_url + " : "+testerpage[1]+ " not found on page")
                
                
                
                
            if fail != 0:
                self.fail(str(fail) + " :Failures")    
                #self.assertFalse('Login to EchoSystem Server' in response.body)

        # end of test -----------------------------------------------


    def test_simple(self):
        # The description should be set in the configuration file
        server_url = self.server_url
        # begin of test ---------------------------------------------
        nb_time = self.conf_getInt('test_simple', 'nb_time')
        pages = self.conf_getList('test_simple', 'pages')
        #esslogin = self.get_cred()
        #server_url = server_url + '/ess/echo/presentation/'
        for i in range(nb_time):
            self.logd('Try %i' % i)
            for page in pages:
            	response = self.get(server_url + page, description='Get %s' % page)
                #print response.body
                responseurl = response.protocol+"://"+response.server+":"+response.port
                if response.url == "/ess/login.jsp":
                    #print "submitting form" + responseurl + "/ess/ContentLogin.html"
                    #li = esslogin[0]
                    #pw = esslogin[1]
                    li = "ess@echo360.com"
                    pw = "password" 
                    #print li,pw
                    #response = self.get(responseurl + "/ess/ContentLogin.html")
                    
                    response = self.post(responseurl + "/ess/j_spring_security_check", params=[
                                                                                        #['formids','login-form,j_username,j_password,login-btn'],
                                                                                        #['submitmode',''],
                                                                                        #['submitname',''],
                                                                                        ['userNameInput', 'ess@echo360.com'],
                                                                                        ['passwordInput', 'password'],
                                                                                        ['j_username', li.strip()],
                                                                                        ['j_password', pw.strip()]],
                                                                                        #['passwordInput', 'y0SPqzft6'],
                                                                                        #['submit', 'login-btn'],
                                                                                        #['action','j_spring_security_check']],
                                                                                        description="ESS Login Page")
                    print response.code, response.url
                print response.code, response.url
                    #self.clearContext() 
                #print str(response.code) + " - " + response.url
                #print response.body
                #self.assert_("Login to EchoSystem Server" in response.body)
                #self.assertFalse('Login to EchoSystem Server' in response.body)

		# end of test -----------------------------------------------

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")


if __name__ in ('main', '__main__'):
    unittest.main()
