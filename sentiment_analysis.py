import requests

def sentiment_analyzer(text_to_analyse):
    """
    method that sends argument text to Watson NLP BERT sentiment analysis function to be analyzed
    returns:
    response.text from Watson NLP
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document" : { "text" : text_to_analyse } }
    header = { "grpc-metadata-mm-model-id" : "sentiment_aggregated-bert-workflow_lang_multi_stock" }
    response = requests.post(url, json = myobj, headers = header)
    return response.text
