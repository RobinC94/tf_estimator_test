#!/usr/bin/python
# -*-coding:utf-8-*-

import os
import argparse
import importlib
from termcolor import cprint

import tensorflow as tf

parser = argparse.ArgumentParser()
parser.add_argument(
    '--dataset',
    help='Dataset name',
    default=None,
    type=str,
)
parser.add_argument(
    '--model',
    help='Model name',
    default=None,
    type=str,
)
parser.add_argument(
    '--job-dir',
    help='GCS location to write checkpoints and export models',
    required=True,
)

# Argument to turn on all logging
parser.add_argument(
    '--verbosity',
    choices=['DEBUG', 'ERROR', 'FATAL', 'INFO', 'WARN'],
    default='INFO',
    help='Set logging verbosity'
)

# Parser arguments
args, _ = parser.parse_known_args()


if __name__ == '__main__':
    dataset_module = importlib.import_module('datasets.' + args.dataset
                                             if args.dataset else 'datasets')
    dataset_module.update_argparser(parser)

    model_module = importlib.import_module('models.' + args.model
                                           if args.model else 'models')
    model_module.update_argparser(parser)
    hparams = parser.parse_args()
    cprint(("hparams: ", hparams), 'blue')

    # Set python level verbosity
    tf.logging.set_verbosity(hparams.verbosity)
    # Set C++ Graph Execution verbosity
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = str(
        tf.logging.__dict__[hparams.verbosity] / 10
    )

    

