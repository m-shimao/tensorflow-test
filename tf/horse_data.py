# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas

#
ODDS_DIR = "../odds"
RESULTS_DIR = "../results"
TEST_ODDS_DIR = "../test_odds"
TEST_RESULTS_DIR = "../test_results"
#

def get_horse_and_label():
	train_horse = []
	train_label = []
        odds = os.listdir(ODDS_DIR)
	for file in odds:
		df = pandas.read_csv(ODDS_DIR + '/' + file)
                val_list = df.values.tolist()
                if len(val_list) < 8:
                    continue
		train_horse.append(val_list[0:7])
                print val_list[0:7]
        results = os.listdir(RESULTS_DIR)
	for file in results:
		df = pandas.read_csv(RESULTS_DIR+ '/' + file)
                val_list = df.values.tolist()
                if len(val_list) < 8:
                    continue
		train_label.append(val_list[0:7])

	train_horse = np.array(train_horse, dtype=np.float32)
	train_label = np.array(train_label, dtype=np.float32)
	return train_horse,train_label

def get_test_horse_and_label():
	train_horse = []
	train_label = []
        odds = os.listdir(TEST_ODDS_DIR)
	for file in odds:
		df = pandas.read_csv(TEST_ODDS_DIR + '/' + file)
                val_list = df.values.tolist()
                if len(val_list) < 8:
                    continue
		train_horse.append(val_list[0:7])
        results = os.listdir(TEST_RESULTS_DIR)
	for file in results:
		df = pandas.read_csv(TEST_RESULTS_DIR+ '/' + file)
                val_list = df.values.tolist()
                if len(val_list) < 8:
                    continue
		train_label.append(val_list[0:7])

	train_horse = np.array(train_horse, dtype=np.float32)
	train_label = np.array(train_label, dtype=np.float32)
	return train_horse,train_label
