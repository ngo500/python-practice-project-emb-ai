""" function that sends data to Watson NLP BERT for sentiment analysis """
import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    method that sends argument text to Watson NLP BERT sentiment analysis function to be analyzed
    returns:
    formatted label and score from Watson NLP
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document" : { "text" : text_to_analyse } }
    header = { "grpc-metadata-mm-model-id" : "sentiment_aggregated-bert-workflow_lang_multi_stock" }
    #send info over POST request and store response
    response = requests.post(url, json = myobj, headers = header, timeout = 10)
    #formated response as json, dictionary of dictionaries
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        #if status 200/OK, store info
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        #elif status 500/error, store None
        label = None
        score = None
    else:
        #status not 200, generic error
        label = None
        score = None
    #return the label and score from the response
    return { 'label' : label, 'score' : score }
