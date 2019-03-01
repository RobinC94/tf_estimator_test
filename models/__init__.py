#!/usr/bin/python
# -*-coding:utf-8-*-

import tensorflow as tf


def update_argparser(parser):
    parser.add_argument(
        '--learning-rate',
        help='Learning rate',
        default=0.0001,
    )


def model_fn(features, labels, mode, params, config):
    pass