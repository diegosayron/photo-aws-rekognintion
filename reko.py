# PREREQUISITES:
# 0 - Python (Used 3.12.15)
# 1 - Configure the python virtual environment: python -m venv reko 
# 2 - Activate the venv created: .\reko\Scripts\activate
# 3 - Install boto3: pip install boto3 (verify: pip show boto3)
# 4 - Adapt the source code for your scenario: 


import boto3

# Configure S3 client and Rekognition
s3_client = boto3.client('s3')
rekognition_client = boto3.client('rekognition')

# Settings
bucket_name = 'photos-elder'
pasta_com_pessoas = 'with-people/'
folder_without_people = 'without-people/'

def move_image(file_name, destin_folder):
    copy_source = {'Bucket': bucket_name, 'Key': file_name}
    novo_file_name = destin_folder + file_name.split('/')[-1]
    s3_client.copy_object(CopySource=copy_source, Bucket=bucket_name, Key=novo_file_name)
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
                move_image(file_name, pasta_com_pessoas)
                print(f"Movido para '{pasta_com_pessoas}': {file_name}")
            else:
                move_image(file_name, folder_without_people)
                print(f"Movido para '{folder_without_people}': {file_name}")

if __name__ == "__main__":
    image_processing()
