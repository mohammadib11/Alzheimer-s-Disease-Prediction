def GetPrediction(model,inputs : list):
    PredctionResult = model.predict([inputs])
    return PredctionResult