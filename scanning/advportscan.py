#! usr/bin/python

from socket import *
import optparse
from threading import *

def main():

    parser = optparse.OptionParser('Usage: ' + '-H <target host> -p <target ports>')
    parser.add_option('-H', dest = 'tgtHost', type = 'string', 
                        help = 'specify target host')
    parser.add_option('-p', dest = 'tgtPort', type = 'string', 
                        help = 'specify target ports seperated by comma')

    (options, args) = parser.parse.args()
    
    if (tgtHost == None) | (tgtPorts[0]):
        print(parser.usage)
        exit(0)
        
    #portScan(tgtHost, tgtPorts)

main()