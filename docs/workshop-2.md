**Pre-requisites**

* Ensure pwd is at the root of the project<br/>

* Install required dependenices.<br/>
    > pip install -r requirements.txt

* Create required packages.

    > pip install -e .

* Run the predict and train sequentially.

    > python workshop/common/ReviewProcessor.py

* Note that all the prediction or training functions are present in ReviewProcessor.<br/>

**Tasks**


* Start kafka consumer for prediction.<br/>

    > python workshop/workshop-2/main.py --mode=CONSUMER --topic=test-workshop-2 --task=predict

* Start kafka consumer for training.<br/>

    > python workshop/workshop-2/main.py --mode=CONSUMER --topic=test-workshop-2 --task=train

* Create a kafka producer to produce reviews to `test-workshop-2`.<br/>

    > python workshop/workshop-2/main.py --mode=PRODUCER --topic=test-workshop-2


**Expected**

* Each review is processed independently for prediction as well as training.<br/>