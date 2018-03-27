

class Model(object):
    """
    Compute correlation model

    in corpus_word_dict, dict of words and nb of appearances in segmented of one algo (or freq for recall, to see; for now, nb)
    in reports_words_dict, dict of words and proportion of children understanding it at one age (or /gold w/ miss inc, to see)
    """
    def __init__(self, corpus_words_dict, reports_words_dict):

        self._slope = 0
        self._intercept = 0
        self._r_value = 0
        self.p_value = 0
        self._std_err = 0

        self._corpus = self.to_dataframe(corpus_words_dict, 'word_freq')
        self._reports = self.to_dataframe(reports_words_dict, 'understanding_prop')

        self._data = self.intersect()

        self._nb_infant_by_age = 0 # needed if logistic
        self._test_size = 0

        self._lin_reg = {'slope' : 0, 'intercept' : 0, 'r_value' : 0, 'r2_value' : 0, 'p_value' : 0, 'std_err' : 0}
        self._log_reg = {'r2_value' : 0, 'std_err' : 0}
        # self._results = {}

    def to_dataframe(self, dico, name):
        return pd.DataFrame(list(dico.items()), columns=['type', name])

    def intersect(self):
        return (pd.merge(self._corpus, self._reports, on='key', how='inner'))

    def compute_linear(self):
        X = np.log(self._data['word_freq'])
        Y = self._data['understanding_prop']

        self._lin_reg['slope'], self._lin_reg['intersect'], self._lin_reg['r_value'], \
        self._lin_reg['p_value'], self._lin_reg['std_err'] = stats.linregress(X,Y)
        self._lin_reg['r2_value'] = self._lin_reg['r_value']*self._lin_reg['r_value'] # r2 = r*r

        return self._lin_reg

    def compute_logistic(self):
        nb_words=len(self._data)
        vec=np.repeat(self._nb_infant_by_age, nb_words)

        X=np.transpose(np.matrix(np.log(self._data['word_freq']))) # LogisticRegression from scikit takes only a matrix as input

        Y=self._data['understanding_prop'].to_frame()
        Y_binary=[]
        for row in Y.itertuples():
            if row[1]> 0.5 :
                Y_binary.append(1)
            else :
                Y_binary.append(0)
        Y_t=np.transpose(np.matrix(Y_binary))
        clf = LogisticRegression(fit_intercept = True , C = 1e9, max_iter=10000, solver='liblinear') # SAG : stochastic average gradiant, useful for big dataset (INRIA) # C : higher it is, the less it penalize

        X_train, X_test, Y_train, Y_test, vec_train, vect_test = \
        train_test_split(X, Y_t, vec,test_size=self._test_size, random_state=np.random.RandomState(42))
        clf.fit(X_train, Y_train, sample_weight=vec_train)
        Y_pred=clf.predict_proba(X_test)

        self._log_reg['r2_value'] = r2_score(Y_test, Y_pred[:,1])
        self._log_reg['std_err'] = mean_squared_error(Y_test, Y_pred[:,1])

        return self._log_reg

    def compute(self, model='linear'):

        if model=='linear':
            self.compute_linear()
        else if model=='logistic':
            self.compute_logistic()

        else :
            # TODO raise error
            print('nope')
