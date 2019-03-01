#!/usr/bin/python
# -*-coding:utf-8-*-

import argparse
import random

import tensorflow as tf

def update_argparser(parser):
    parser.add_argument(
        '--train-batch-size',
        help='Batch size for training',
        type=int,
        default=32,
    )

