#!/usr/local/bin/python3

from time import time

# Parking Rule in JSON for now.
parkRule = {
        1 : 10,
        2 : 20,
        3 : 30 
        }

class Ticket:
    
    #ticket_id = 0
        
    def __init__(self,zoneId):
        #global ticket_id
        self.zoneId = zoneId
        self.starttime = time()
        self.endtime = 0
        self.cost=0
        #self.ticketId = ticket_id
        #ticket_id +=1

    def printTicket(self):
        #print("zoneId=%d, ticket_id =%d and time=%d"%(self.zoneId, self.ticketId,self.time))
        print("zoneId=%d, start time=%d, end time = %d, cost=%d"%(self.zoneId, self.starttime,self.endtime,self.cost))
        return self


class ProcessPayment:

    def __init__(self,ticket,ccDetails):
        self.ticket = ticket
        self.ccDetails = ccDetails

    def execute(self):
        return True


class TicketMachine:
    def __init__(self,zoneId):
        self.zoneId = zoneId
        
    def printTicket(self):
        ticket = Ticket(self.zoneId)
        ticket.printTicket()
        return ticket

    def readTicket(self,ticket):
        endTime = time()
        timeSpan = 3
        cost = parkRule[timeSpan]
        ticket.endtime = endTime
        ticket.cost = cost
        
        #Write to Database.

        #Return ticket
        return ticket
    

ticketM1 = TicketMachine(101)

ticket1 = ticketM1.printTicket()

ticket1 = ticketM1.readTicket(ticket1)

ticket1.printTicket()

#print("Ticket Cost = %d"%(ticket1.cost))
