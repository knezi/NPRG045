#!/bin/env python3
# TODO COMMENT AUTHOR
from math import log2, ceil

import nltk

from load_data import Data, SampleTypeEnum

# data = Data('data/data_sample.json', 'data/geneea_data_extracted_sample.json')
data = Data('data/data.json', 'data/geneea_data_extracted.json')

train_size = data.generate_sample('useful')
# data.limit_train_size(2)
# data.dump_fasttext_format('useful', 'data/data_fasttext')
# data.plot([[(1,2), (1,1)], [(2,2), (3,3)]], 'a')

plot_data = [[], []]
# TODO this cannot exceed, but doesn't use up all data
for train_size in map(lambda x: 2**x, range(1, ceil(log2(train_size)))):
    data.limit_train_size(train_size)

    train_set = data.get_feature_dict(SampleTypeEnum.TRAIN)
    test_set = data.get_feature_dict(SampleTypeEnum.TEST)
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    print("SIZE {}".format(train_size))
    print(nltk.classify.accuracy(classifier, test_set))
    print(nltk.classify.accuracy(classifier, train_set))

    plot_data[0].append((train_size, nltk.classify.accuracy(classifier, test_set)))
    plot_data[1].append((train_size, nltk.classify.accuracy(classifier, train_set)))

data.plot(plot_data, 'accuracy_bayes')


# pridani jednotlivych slov tady snizi presnost jen na 65, je to ocekavane?

# classifier.show_most_informative_features(30)

# # classifier = nltk.DecisionTreeClassifier.train(train_set)
# # print(nltk.classify.accuracy(classifier, test_set))
# # print(nltk.classify.accuracy(classifier, train_set))


# # # get feature matrix

# # In[42]:


# X, Y = [x[0] for x in feature_sets], [x[1] for x in feature_sets]

# # In[43]:


# from sklearn.datasets import fetch_20newsgroups
# from sklearn.feature_selection import mutual_info_classif
# from sklearn.feature_extraction.text import CountVectorizer

# # In[44]:


# X[0]

# # In[45]:


# cv_gain = CountVectorizer(max_df=0.95, min_df=2,
# max_features=10000)  # WTF

# # In[46]:


# all_keys = [set(x.keys()) for x in X]

# # In[47]:


# import functools

# all_fs = functools.reduce(lambda a, b: a.union(b), all_keys)
# all_fs = list(all_fs)

# # In[48]:


# len(all_fs)


# # In[49]:


# def get_int(val):
# if isinstance(val, int):
# return val
# if isinstance(val, float):
# return val
# vals = {'Yes': 1, 'No': 0, 'middle': 1, 'long': 2, 'short': 0, 'good': 1, 'bad': 0}
# return vals[val]


# # In[50]:


# # X_matrix=[]
# #
# # for x in X:
# #    row=[]
# #    for key in all_fs:
# #        if key in x:
# #            row.append(get_int(x[key]))
# #        else:
# #            row.append(0)
# #    X_matrix.append(row)


# # In[51]:


# import scipy

# # In[52]:


# row = []
# x = X[0]

# for key in all_fs:
# if key in x:
# row.append(get_int(x[key]))
# else:
# row.append(0)

# X_matrix = scipy.sparse.lil_matrix([row])

# i = 0
# for x in X[1:]:
# row = []
# for key in all_fs:
# if key in x:
# row.append(get_int(x[key]))
# else:
# row.append(0)
# X_matrix = scipy.sparse.vstack((X_matrix, scipy.sparse.lil_matrix([row])), format='lil')
# i += 1
# # if i==1000:
# # break

# # In[53]:


# len(X)

# # In[54]:


# X_matrix

# # ## logistic regression

# # In[55]:


# from sklearn.linear_model import LogisticRegression

# # In[56]:


# lr = LogisticRegression()

# # In[57]:


# half = int(len(X) / 2)
# print(half)

# # In[58]:


# train_set_X, test_set_X = X_matrix[:half, :], X_matrix[half:, :]
# train_set_Y, test_set_Y = Y[:half], Y[half:]

# # In[59]:


# lr.fit(train_set_X, train_set_Y)

# # In[60]:


# lr.score(test_set_X, test_set_Y)

# # ## Dimension reduction - LSA - SVD

# # In[55]:


# from sklearn.decomposition import TruncatedSVD
# from sklearn.preprocessing import scale

# # In[56]:


# svd = TruncatedSVD(n_components=100)
# # scale(X_matrix.tocsc())
# svdMatrix = svd.fit_transform(X_matrix)

# # In[57]:


# feature_set_reduced = [(dict(enumerate(x)), y) for (x, y) in zip(svdMatrix, Y)]

# # In[58]:


# random.shuffle(feature_set_reduced)
# half = int(len(feature_sets) / 2)
# train_set, test_set = feature_sets[:half], feature_sets[half:]
# half

# # # training

# # In[59]:


# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(nltk.classify.accuracy(classifier, test_set))

# # # get feature matrix

# # In[60]:


# X, Y = [x[0] for x in test_set], [x[1] for x in test_set]

# # In[61]:


# from sklearn.datasets import fetch_20newsgroups
# from sklearn.feature_selection import mutual_info_classif
# from sklearn.feature_extraction.text import CountVectorizer

# # In[62]:


# X[0]

# # In[63]:


# cv_gain = CountVectorizer(max_df=0.95, min_df=2,
# max_features=10000)

# # In[64]:


# all_keys = [set(x.keys()) for x in X]

# # In[65]:


# import functools

# all_fs = functools.reduce(lambda a, b: a.union(b), all_keys)
# all_fs = list(all_fs)

# # In[66]:


# len(all_fs)


# # In[67]:


# def get_int(val):
# if isinstance(val, int):
# return val
# if isinstance(val, float):
# return val
# vals = {'Yes': 1, 'No': 0, 'middle': 1, 'long': 2, 'short': 0, 'good': 1, 'bad': 0}
# return vals[val]


# # In[68]:


# # X_matrix=[]
# #
# # for x in X:
# #    row=[]
# #    for key in all_fs:
# #        if key in x:
# #            row.append(get_int(x[key]))
# #        else:
# #            row.append(0)
# #    X_matrix.append(row)


# # In[69]:


# import scipy

# # In[70]:


# row = []
# x = X[0]

# for key in all_fs:
# if key in x:
# row.append(get_int(x[key]))
# else:
# row.append(0)

# X_matrix = scipy.sparse.lil_matrix([row])

# i = 0
# for x in X[1:]:
# row = []
# for key in all_fs:
# if key in x:
# row.append(get_int(x[key]))
# else:
# row.append(0)
# X_matrix = scipy.sparse.vstack((X_matrix, scipy.sparse.lil_matrix([row])))
# i += 1
# # if i==1000:
# # break

# # In[71]:


# len(X)

# # In[72]:


# X_matrix

# # # information gaion

# # In[73]:


# res_gain = list(zip(all_fs, mutual_info_classif(X_matrix, Y, discrete_features=True)))

# # In[74]:


# # res_gain


# # In[75]:


# [(x, y) for (x, y) in res_gain if y > 0.0005]

# # In[76]:


# [(x, y) for (x, y) in res_gain if y > 0.001]

# # In[77]:


# sorted([(x, y) for (x, y) in res_gain if x[:3] == '@@@'])