# /home/lududu/anaconda3/bin/activate
# lu 2019 copyright
# Stylometric Test: John Burrows’ Delta Method
# Gutenberg corpus: Distinguish the three authors
# 1. the King James version of the Bible
# 2. three novels by Jane Austen
# 3. three novels or collections of short stories by G. K. Chesterton.
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import gutenberg
import math
import pickle
import os

def DeltaMethod(subcorpora_by_author_string, Authors):
  # Simplifiy Samples
  subcorpora_by_author_tokens = {}
  subcorpora_by_author_length_distributions = {}
  for author in Authors:
      tokens = nltk.word_tokenize(subcorpora_by_author_string[author])
      subcorpora_by_author_tokens[author] = ([token for token in tokens if any(c.isalpha() for c in token)])
    
      token_lengths = [len(token) for token in subcorpora_by_author_tokens[author]]
      subcorpora_by_author_length_distributions[author] = nltk.FreqDist(token_lengths)

  whole_corpus = []
  for author in Authors:
      whole_corpus += subcorpora_by_author_tokens[author]

  whole_corpus_freq_dist = list(nltk.FreqDist(whole_corpus).most_common(30))

  # Calculate each feature's presence in the subcorpus, for each candidate's features
  features = [word for word, freq in whole_corpus_freq_dist]

  # Calculate feature freqs
  feature_freqs = {}
  
  for author in Authors:
    feature_freqs[author] = {} 
    
    sum_tokens_author = len(subcorpora_by_author_tokens[author])
    
    for feature in features:
        presence = subcorpora_by_author_tokens[author].count(feature)
        feature_freqs[author][feature] = presence / sum_tokens_author

  # Find a “mean of means” and a standard deviation for each feature
  corpus_features = {}

  # Calculate the mean
  for feature in features:
    corpus_features[feature] = {}

    feature_average = 0
    for author in Authors:
        feature_average += feature_freqs[author][feature]
    feature_average /= len(Authors)
    corpus_features[feature]['Mean'] = feature_average

    # Calculate the standard deviation
    feature_stdev = 0
    for author in Authors:
      diff = feature_freqs[author][feature] - corpus_features[feature]['Mean']
      feature_stdev += diff*diff
      if len(Authors) != 1:
        feature_stdev /= (len(Authors) - 1)
      feature_stdev = math.sqrt(feature_stdev)
      corpus_features[feature]['StdDev'] = feature_stdev

  # Calculating z-scores, its definition = (value - mean) / stddev
  feature_zscores = {}
  for author in Authors:
    feature_zscores[author] = {}
    for feature in features:
      feature_val = feature_freqs[author][feature]
      feature_mean = corpus_features[feature]['Mean']
      feature_stdev = corpus_features[feature]['StdDev']
      feature_zscores[author][feature] = ((feature_val-feature_mean) / feature_stdev)

  return features, feature_zscores, corpus_features

def read_files_into_string(filenames):
  strings = []
  for filename in filenames:
    with open(f'/home/lududu/Documents/python_vm/USpeakIGuess/AuthorIdentification/{filename}', encoding = "ISO-8859-1") as f:
      strings.append(f.read())
  return ''.join(strings)
  

def deltamethod(filename):
  text = read_files_into_string(file)
  return DeltaMethodText(text)


def DeltaMethodText(text):
  curren_path = os.getcwd()
  classifier_f = open(f"{curren_path}/AuthorIdentification/DeltaMethod.pickle", "rb") 
  feature_zscores = pickle.load(classifier_f) 

  # Author candidate to be confirmed
  Authors = ['Bible', 'Austen', 'Chesterton']

  TestCase_by_author = {}  
  TestCase_by_author['UnknownAuthors'] = text

  testcase_tokens = nltk.word_tokenize(TestCase_by_author['UnknownAuthors'])
      
  # Filter out punctuation and lowercase the tokens
  testcase_tokens = [token.lower() for token in testcase_tokens if any(c.isalpha() for c in token)]

  # Calculate the test case's features
  overall = len(testcase_tokens)

  if overall < 25:
      Deltascore_data=''
      result ='Text is too short, can not be authenticated. '
      return Deltascore_data, result

  testcase_freqs = {}
  for feature in feature_zscores[0]:
      presence = testcase_tokens.count(feature)
      testcase_freqs[feature] = presence / overall

  corpus_features = feature_zscores[2]

  # Calculate the test case's feature z-scores
  testcase_zscores = {}
  for feature in feature_zscores[0]:
      feature_val = testcase_freqs[feature]
      feature_mean = corpus_features[feature]['Mean']
      feature_stdev = corpus_features[feature]['StdDev']
      testcase_zscores[feature] = (feature_val - feature_mean) / feature_stdev
  # print("Test case z-score for feature", feature, "is", testcase_zscores[feature])

  #----------------Delta Method----------------
  # Calculating Delta-  the formula for Delta defined by Burrows
  author_by_delta = {}
  Deltascore = ''
  Deltascore_data = []
  delta_list =[]

  for author in Authors:
      delta = 0
      for feature in feature_zscores[0]:
          delta += math.fabs((testcase_zscores[feature] - 
                              feature_zscores[1][author][feature]))
      delta /= len(feature_zscores[0])

      author_by_delta[delta] = author

      delta_list.append(delta)

      Deltascore = "Delta score for candidate  " + author + " is " + str(delta)
      Deltascore_data.append(Deltascore)

  min_delta = min(delta_list)
  most_likely_author = author_by_delta[min_delta]

  result = 'Elta Identifition Result: " ' + most_likely_author + ' " as TestCase most likely author.'

  return Deltascore_data, result
