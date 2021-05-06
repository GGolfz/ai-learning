class CosineSimilarityModel:
  def __init__(self):
    self.data = []
  def predict(self,X):
    maxind = 0
    maxval = 0
    for i in X:
      for j in range(len(self.data)):
        tempY = self.data[j]['X'].reshape(1,-1)
        cs = cosine_similarity(X,tempY)
        if cs > maxval:
          maxval = cs
          maxind = j
          print(maxval)
          print(self.data[j]['y'])
    return str(self.data[maxind]['y'])
  def fit(self,X,y):
    for i in range(len(X)):
      self.data.append({'X':np.array(X.iloc[i,:]),'y':np.array(y.iloc[i])})
  
