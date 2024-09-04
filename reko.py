# PREREQUISITES:
# 0 - Python (Used 3.12.15)
# 1 - Configure the python virtual environment: python -m venv reko 
# 2 - Activate the venv created: .\reko\Scripts\activate
# 3 - Install boto3: visual studio code - Terminal - type: pip install boto3 (verify: pip show boto3)
# 4 - AWS Account:
#     - CLI account configured in AWS IAM, with permissions for AWS Rekognition and S3 (SAVE and copy the ACCESS KEY ID and Secret Access Key credentials)
#     - Download and install the aws cli (https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
#     - In your PC - Windows cmd or other:
#       - aws configure 
#         - Fill with your credentials and preferences (Access Key ID, Secret Access Key, The region of your created S3 bucket eg. us-east-1, output format: table, etc) 
#     - S3 bucket configured in default mode (non-public and ACLs disabled) named, for example, elders-photos and fill it with some photos
#       - Create two folders inside it: with-people/ and without-people/
# 5 - Adapt the source code to your scenario (and run it!): 


import boto3

# Configure S3 client and Rekognition
s3_client = boto3.client('s3')
rekognition_client = boto3.client('rekognition')

# Settings
bucket_name = 'photos-elder'
folder_with_people = 'with-people/'
folder_without_people = 'without-people/'

def move_image(file_name, destin_folder):
    copy_source = {'Bucket': bucket_name, 'Key': file_name}
    new_file_name = destin_folder + file_name.split('/')[-1]
    s3_client.copy_object(CopySource=copy_source, Bucket=bucket_name, Key=new_file_name)
    s3_client.delete_object(Bucket=bucket_name, Key=file_name)

def verify_people_in_photo(file_name):
    resposta = rekognition_client.detect_labels(
        Image={'S3Object': {'Bucket': bucket_name, 'Name': file_name}},
        MaxLabels=10,
        MinConfidence=80
    )
    
    for label in resposta['Labels']:
        if label['Name'] == 'Person':
            return True
    return False


#Use try catch to improve the code in case of errors
def image_processing():
    resposta = s3_client.list_objects_v2(Bucket=bucket_name)
    
    for objeto in resposta.get('Contents', []):
        file_name = objeto['Key']
        
        if file_name.lower().endswith('.jpg') | file_name.lower().endswith('.png') :
            there_is_people = verify_people_in_photo(file_name)
            
            if there_is_people:
                move_image(file_name, folder_with_people)
                print(f"Moved to '{folder_with_people}': {file_name}")
            else:
                move_image(file_name, folder_without_people)
                print(f"Moved to '{folder_without_people}': {file_name}")

if __name__ == "__main__":
    image_processing()
