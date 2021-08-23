'''An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.'''
'''Example

For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;

For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.

There is no first number.'''

def isIPv4Address(inputString):
    l=inputString.split('.')
    if len(l)!=4:
        return False
    for i in range(len(l)):
        if l[i]=='':
            return False
        if l[i].isdecimal()==False:
            return False
        if l[i]!=str(int(l[i])):
            return False
        if int(l[i])>255:
            return False
    return True