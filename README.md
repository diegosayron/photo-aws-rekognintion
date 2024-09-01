# Photo AWS Rekognition
_(and sorting within separate folders)_

My friend Elder is a professional sports photographer. 
He usually leaves his camera automatically taking photos at a sporting event. 
Elder's challenge is to visually and manually sort through the thousands of photos from an event, spending time and often not even doing the task, given the difficulty.

This simple python source code could detect and separate photos with and with no people into two folders (stored in a bucket on aws):
`with-people/`
`without-people/`

And it will certainly save Helder's time at a low cost considering his enormous effort and use of his precious time running this code.

**Batman's belt:**
- The Visual Studio Code + Python installed
- AWS CLI installed and configured with the IAM account that will be created below
- Boto3 installed
- An AWS account
  - S3 bucket configured in default mode (non-public and ACLs disabled) named, for example, `elders-photos` and fill it with some photos
    - Create two folders inside it: with-people/ and without-people/
- CLI account configured in AWS IAM, with permissions for AWS Rekognition and S3
- Source code for this repository
- Half a cup of coffee
- The time of the song **Shine on your crazy diamond - Pink Floyd** to complete this small project.

**Running the Script:**
Having the file, for example: reko.py open, right click on a blank spot in the source code, `run python`, `run the python file in the terminal`

**Improvements**
If you want to further automate the recognition process, consider using this code in an AWS Lambda project.
Any photos uploaded to a bucket can trigger a lambda to classify the content.


If this code helped you, please let me know by clicking the star button to motivate me to create more AI content.






  
