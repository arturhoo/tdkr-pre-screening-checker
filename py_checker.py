# -*- coding: utf-8 -*-
from subprocess import check_output, call
from os import remove
from sys import exit

try:
    from email_to_send import *
except ImportError:
    exit("No receiver found!")


def build_msg(sender_address, receiver_address):
    msg = open('msg.txt', 'w')
    msg.write('To: ' + receiver_address)
    msg.write('\nFrom: ' + sender_address)
    msg.write('\nSubject: The Dark Knight Pre Screening!!')
    msg.write('\n\nGo buy it now!')

if __name__ == '__main__':
    # Execute casperjs
    output = check_output(['casperjs', 'checker.js'])

    # Get the first line from casper's output, indicates
    # the number of dates available on the website
    dates_len = output.split('\n')[0]

    # Get the second line from casper's output
    next_session_text = output.split('\n')[1]
    default_next_session_text = open('default_next_session_text.txt',
                                     'r').read()
    if dates_len != '8' or default_next_session_text != next_session_text:
        build_msg(SENDER, RECEIVER)
        call('ssmtp ' + RECEIVER + ' < msg.txt', shell=True)
        remove('msg.txt')
