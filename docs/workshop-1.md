
**Pre-requisites**

* Ensure pwd is at the root of the project<br/>

* Install required dependenices.<br/>
    > pip install -r requirements.txt

* Create required packages.

    > pip install -e .

* Run the predict and train sequentially.<br/>

    > python workshop/common/ReviewProcessor.py

 Note that all the prediction or training functions are present in ReviewProcessor.<br/>

**Tasks**

* Create a kafka producer to produce reviews to `test-workshop-1`.<br/>

    > python workshop/workshop-1/main.py --mode=PRODUCER --topic=test-workshop-1

* Create consumer to consume reviews from topic `test-workshop-1` and predict sentiment on each review.<br/>

    > python workshop/workshop-1/main.py --mode=CONSUMER --topic=test-workshop-1 --consumer_group=test-workshop-1

**Expected**

* Reviews are produced to a topic and prediction is performed on each review.<br/>