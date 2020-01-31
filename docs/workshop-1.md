
**Pre-requisites**
* Install required dependenices.
`pip install -r requirements.txt`
* Create package.
`pip install -e .`
* Run the predict and train sequentially.
`python workshop/common/ReviewProcessor.py`
 Note that all the prediction or training functions are present in ReviewProcessor.

**Tasks**
* Create a kafka producer to produce reviews to `test-workshop-1`.
   `python workshop/workshop-1/main.py --mode=PRODUCER --topic=test-workshop-1`
* Create consumer to consume reviews from topic `test-workshop-1` and predict sentiment on each review.
   `python workshop/workshop-1/main.py --mode=CONSUMER --topic=test-workshop-1 --consumer_group=test-workshop-1`

**Expected**
* Reviews are produced to a topic and prediction is performed on each review.