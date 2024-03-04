from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    """
    class for unit testing the sentiment_analyzer function 
    of the SentimentAnalysis package
    """
    def test_sentiment_analyzer(self):
        """
        function for unit testing sentiment_analyzer
        tests for postive, negative, and neutral statements
        returns:
        OK or FAILED, the status of unit tests
        """
        #test for positive statement
        result_1 = sentiment_analyzer('I love working with Python.')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')

        #test for negative statement
        result_2 = sentiment_analyzer('I hate working with Python.')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')

        #test for neutral statement
        result_3 = sentiment_analyzer('I am neutral on Python.')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

#run the unit tests
unittest.main()
