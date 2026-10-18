from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
      result1 = emotion_detector("I am very angry that no one in customer service responds")
      self.assertEqual(result1["dominant_emotion"], "anger")

      result2 = emotion_detector("The packaging was disgusting")
      self.assertEqual(result2["dominant_emotion"], "disgust")

      result3 = emotion_detector("I had a fear that package would not be delivered on time")
      self.assertEqual(result3["dominant_emotion"], "fear")

      result4 = emotion_detector("I am really happy to recieve the parcel")
      self.assertEqual(result4["dominant_emotion"], "joy")

      result5 = emotion_detector("I am very disappointed because of the late delivery")
      self.assertEqual(result5["dominant_emotion"], "sadness")

if __name__ == '__main__':
    unittest.main()