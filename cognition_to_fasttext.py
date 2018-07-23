import numpy as np
import pandas as pd
import argparse
import os

from utils import log

def run(args):

    check_output_dir()
    output_filename = str(args.name).lower().replace(" ", "_")
    full_output_filename = os.path.join("results", output_filename + ".full.ft")
    training_output_filename = os.path.join("results", output_filename + ".train.ft")
    test_output_filename = os.path.join("results", output_filename + ".test.ft")

    try:
        annotations = pd.read_csv(args.input)
    except Exception as e:
        raise Exception("Cannot read input file. Encountered error: {}".format(str(e)))

    if 0.01 > args.split > 0.99:
        raise Exception("Invalid split. Value should be between 0.01 and 0.99")

    msk = np.random.rand(len(annotations)) < (1-args.split)
    training_set = annotations[msk]
    test_set = annotations[~msk]

    log.info("Size of training set: {}".format(len(training_set)))
    log.info("Size of test set:     {}".format(len(test_set)))

    if len(training_set) == 0:
        raise Exception("Training set is empty")

    if len(test_set) == 0:
        raise Exception("Test set is empty")

    log.info("Writing full data to {}".format(full_output_filename))
    with open(full_output_filename, "w+") as out_full:


        log.info("Writing training data to {}".format(training_output_filename))
        with open(training_output_filename, 'w+') as out:

            for index, row in training_set.iterrows():
                try:
                    out.write(concat_label_and_text(row['label'], preprocess_text(row['text']), args.label)+'\n')
                    out_full.write(concat_label_and_text(row['label'], preprocess_text(row['text']), args.label) + '\n')
                except:
                    log.warn("Encountered an invalid row, skipping.")
                    pass

        log.info("Writing test data to {}".format(test_output_filename))
        with open(test_output_filename, 'w+') as out:

            for index, row in test_set.iterrows():
                try:
                    out.write(concat_label_and_text(row['label'], preprocess_text(row['text']), args.label)+'\n')
                    out_full.write(concat_label_and_text(row['label'], preprocess_text(row['text']), args.label) + '\n')
                except:
                    log.warn("Encountered an invalid row, skipping.")
                    pass

    log.info("Success")

def check_output_dir():

    if not os.path.exists("results"):
        log.info("Results directory does not exist, creating now.")
        os.mkdir("results")

def concat_label_and_text(label, text, pos_label):

    if label in ["yes",1,"true", "1", True, pos_label]:
        return "{} {}".format("__label__{}".format(pos_label), text)

    elif label in ["no", 0, "false", "0", False]:
        return "{} {}".format("__label__no", text)

    else:
        err = "Invalid label: {} <{}>. Labels must be either 'yes/1/{}' or 'no/0'.".format(label,type(label), pos_label)
        raise Exception(err)

def preprocess_text(text):

    return text.replace('\n', ' ').replace('\r','')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Converts raw Cognition output into FastText format")

    parser.add_argument("--input-csv", help="Cognition annotation file (CSV Format)",
                        dest="input", type=str, action="store", required=True)

    parser.add_argument("--name", help="Model Name",
                        dest="name", type=str, action="store", required=True)

    parser.add_argument("--label", help="Positive annotation label",
                        dest="label", type=str, action="store", default="yes")

    parser.add_argument("--split", help="Size of test split (0.01-0.99)",
                        dest="split", type=float, action="store", default=0.2)

    args = parser.parse_args()

    log.info("Input file:        {}".format(args.input))
    log.info("Model name:        {}".format(args.name))
    log.info("Positive label:    {}".format(args.label))
    log.info("Test split size:   {}".format(args.split))

    run(args)