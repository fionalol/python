#!/bin/python
class AddrBookEntry(object):
    'address book entry class'
    def __init__(self, nm, ph):
        self.name=nm
        self.phone=ph
        print 'created instance for:', self.name
        print 'created instance for: %s' % self.phone
    def updatePhone(self,newphone):
        self.phone=newphone
        print 'update phone# for', self.name
        print 'created instance for: %s' % self.phone
        
addr=AddrBookEntry('fiona', '12345678')
addr.updatePhone('55555')


class EmailAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'
    def __init__(self, nm, ph,idnum, em):
        AddrBookEntry.__init__(self,nm, ph)
        self.empid=idnum
        self.email=em
        print 'created instance for:', self.name
        print 'created instance for: %s' % self.phone
        print 'created instance for:', self.empid
        print 'created instance for: %s' % self.email
            
    def updateEmail(self, newem):
        self.email = newem
        print 'Updated e-mail address for:', self.email

addr_email=EmailAddrBookEntry('test','64951419','00001','fiona@gmail.com')
addr_email.updateEmail('update')
addr_email.updatePhone('13810393028')