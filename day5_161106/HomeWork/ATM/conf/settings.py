#!_*_coding:utf-8_*_
#__author__:"Alex Li"
import os
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}


LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},        #还款
    'withdraw':{'action':'minus', 'interest':5}, #取现
    'transfer':{'action':'minus', 'interest':5}, #转账
    'consume':{'action':'minus', 'interest':0},     #消费
}